import os
import glob
import subprocess
from ursina.mesh import Mesh
from ursina import application
import pathlib

def load_model(name, path=application.asset_folder):
    for filetype in ('.bam', '.ursinamesh', '.obj', '.blend'):
        for filename in path.glob(f'**/{name}{filetype}'):
            if filetype == '.bam':
                return loader.loadModel(filename)

            if filetype == '.ursinamesh':
                try:
                    with open(filename) as f:
                        m = eval(f.read())
                        return m
                except:
                    print('invalid ursinamesh file:', filename)

            if filetype == '.obj':
                print('found obj', filename)
                m = obj_to_ursinamesh(path=path, name=name, save_to_file=False)
                m = eval(m)
                return m

            if filetype == '.blend':
                print('found blend file:', filename)
                compress_models(path=path, name=name)
                return load_model(name, path)
    # for f in glob(f'**/{name}.blend'):
    #     print('found blend file')
    #     # compress_models(name=name + '.blend')

    return None

blender_path = 'blender'

import platform
if platform.system() == 'Windows':
    # get blender path by getting default program for '.blend' file extention
    import shlex
    import winreg

    class_root = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, '.blend')
    with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r'{}\shell\open\command'.format(class_root)) as key:
        command = winreg.QueryValueEx(key, '')[0]
        blender_path = shlex.split(command)[0]

print('blender_path:', blender_path)


def compress_models(path=application.models_folder, outpath=application.compressed_models_folder, name='*'):

    if not application.compressed_models_folder.exists():
        application.compressed_models_folder.mkdir()

    export_script_path = application.internal_scripts_folder / '_blend_export.py'

    for f in glob.glob(f'{path}/**/{name}.blend'):
        # print(f)
        outfile = outpath / f
        print('converting .blend file to .obj:', outfile)
        subprocess.call(f'''{blender_path} {outfile} --background --python {export_script_path}''')


def obj_to_ursinamesh(
    path=application.compressed_models_folder,
    outpath=application.compressed_models_folder,
    name='*',
    save_to_file=True,
    delete_obj=True
    ):

    for f in path.glob(f'**/{name}.obj'):
        filepath = path / (os.path.splitext(f)[0] + '.obj')
        print('read obj at:', filepath)
        meshstring = ''
        meshstring += 'Mesh('

        with open(filepath, 'r') as file:
            lines = file.readlines()



        verts = list()
        tris = list()

        uv_indices = list()
        uvs = list()
        norm_indices = list()
        norms = list()

        # parse the obj file to a Mesh
        for l in lines:
            if l.startswith('v '):
                vert = [float(v) for v in l[2:].strip().split(' ')]
                vert[0] = -vert[0]
                verts.append(tuple(vert))

            elif l.startswith('vn '):
                n = l[3:].strip().split(' ')
                norms.append(tuple([float(e) for e in n]))

            elif l.startswith('vt '):
                uv = l[3:].strip()
                uv = uv.split(' ')
                uvs.append(tuple([float(e) for e in uv]))

            elif l.startswith('f '):
                l = l[2:]
                l = l.split(' ')


                tri = tuple([int(t.split('/')[0]) for t in l])
                for t in tri:
                    tris.append(t-1)

                try:
                    uv = tuple([int(t.split('/')[1]) for t in l])
                    for t in uv:
                        uv_indices.append(t-1)
                except: # if no uvs
                    pass

                try:
                    n = tuple([int(t.split('/')[2]) for t in l])
                    for t in n:
                        norm_indices.append(t-1)
                except: # if no normals
                    pass

        meshstring += '\nvertices='
        meshstring += str(tuple([verts[t] for t in tris]))

        if uv_indices:
            meshstring += ', \nuvs='
            meshstring += str(tuple([uvs[uid] for uid in uv_indices]))

        if norm_indices:
            meshstring += ', \nnormals='
            meshstring += str(tuple([norms[nid] for nid in norm_indices]))

        meshstring += ''', \nmode='triangle')'''

        if not save_to_file:
            return meshstring

        outfilepath = outpath / (os.path.splitext(f)[0] + '.ursinamesh')
        with open(outfilepath, 'w') as file:
            file.write(meshstring)

        if delete_obj:
            os.remove(filepath)

        print('saved ursinamesh to:', outfilepath)

# faster, but does not apply modifiers
def compress_models_fast(model_name=None, write_to_disk=False):
    print('find models')
    from tinyblend import BlenderFile
    if not application.compressed_models_folder.exists():
        application.compressed_models_folder.mkdir()

    files = os.listdir(application.models_folder)
    compressed_files = os.listdir(application.compressed_models_folder)

    for f in files:
        if f.endswith('.blend'):
            # print('f:', application.compressed_models_folder + '/' + f)
            print('compress______', f)
            blend = BlenderFile(application.models_folder + '/' + f)
            number_of_objects = len(blend.list('Object'))

            for o in blend.list('Object'):
                if not o.data.mvert:
                    continue
                # print(o.id.name.decode("utf-8", "strict"))
                object_name = o.id.name.decode( "utf-8").replace(".", "_")[2:]
                object_name = object_name.split('\0', 1)[0]
                print('name:', object_name)

                vertices= o.data.mvert
                verts = [v.co for v in o.data.mvert]
                verts = tuple(verts)

                file_content = 'Mesh(' + str(verts)

                file_name = ''.join([f.split('.')[0], '.ursinamesh'])
                if number_of_objects > 1:
                    file_name = ''.join([f.split('.')[0], '_', object_name, '.ursinamesh'])
                file_path = os.path.join(application.compressed_models_folder, file_name)
                print(file_path)

                tris = tuple([triindex.v for triindex in o.data.mloop])
                flippedtris = list()
                for i in range(0, len(tris)-3, 3):
                    flippedtris.append(tris[i+2])
                    flippedtris.append(tris[i+1])
                    flippedtris.append(tris[i+0])

                file_content += ', triangles=' + str(flippedtris)

                if o.data.mloopuv:
                    uvs = tuple([v.uv for v in o.data.mloopuv])
                    file_content += ', uvs=' + str(uvs)

                file_content += ''', mode='triangle')'''

                if write_to_disk:
                    with open(file_path, 'w') as file:
                        file.write(file_content)

                return file_content

def ursina_mesh_to_obj(mesh, name='', out_path=application.models_folder, max_decimals=3):
    from ursina.useful import camel_to_snake

    if not name:
        name = camel_to_snake(mesh.__class__.__name__)
    obj = 'o ' + name + '\n'


    for v in mesh.vertices:
        v = [round(e, max_decimals) for e in v]
        obj += f'v {v[0]} {v[1]} {v[2]}\n'

    if mesh.uvs:
        for uv in mesh.uvs:
            uv = [round(e, max_decimals) for e in uv]
            obj += f'vt {uv[0]} {uv[1]}\n'

    obj += 's off\n'

    if mesh.triangles:
        tris = mesh.triangles

        if isinstance(tris[0], tuple): # convert from tuples to flat
            new_tris = list()
            for t in tris:
                if len(t) == 3:
                    new_tris.extend([t[0], t[1], t[2]])
                elif len(t) == 4: # turn quad into tris
                    new_tris.extend([t[0], t[1], t[2], t[2], t[3], t[0]])

            tris = new_tris


    if mesh.mode == 'ngon':
        tris = list()
        for i in range(1, len(mesh.vertices)-1):
            tris.extend((i, i+1, 0))


    # tris must be a list of indices
    for i, t in enumerate(tris):
        if i % 3 == 0:
            obj += '\nf '
        obj += str(t+1)
        if mesh.uvs:
            obj += '/'+str(t+1)
        obj += ' '


    # print(obj)
    with open(out_path / (name + '.obj'), 'w') as f:
        f.write(obj)
        print('saved obj:', out_path / (name + '.obj'))



def compress_internal():
    compress_models(application.internal_models_folder)
    obj_to_ursinamesh(
        application.internal_models_folder / 'compressed',
        application.internal_models_folder / 'compressed',
        )


if __name__ == '__main__':
    compress_internal()
    # from ursina import *
    # app = Ursina()
    # e = Entity(model=Cylinder(16))
    # ursina_mesh_to_obj(e.model, name='quad_export_test')
