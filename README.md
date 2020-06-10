# Visualization of test driving scenario based on ursina
Ursina is an easy to use game engine/framework for python. (https://www.ursinaengine.org/)

![Banner](/docs/top8.jpg)


## Motivation
Safe and efficient driving experience is crucial for autonomous vehicles. Although AVs are equipping with more advanced sensors nowadays, autonomous drving remained challenging in urban environments. This is especially true when driving in the intersection with heavy traffic. Most of the time human drivers tend to be aggressive and it requires highly intelligent motion planning algorithm to safely merge into traffic and select a better lane when needed. This visualization construct this common yet challenging scenario with ursina that allows users to test the performance of motion planning algorithm under different traffic speed, gaps between vehicles and the level of aggressiveness of other vehicles. This may help engineers to better balance the 

![frommobileyes](/docs/sim8.jpg)
## Objectives
  * Test motion planning algorithm
  * panda3d
  * screeninfo, for detecting screen resolution
  * hurry.filesize, for converting bytes to megabytes
  * pillow, for texture manipulation
  * psd-tools, for converting .psd files
  * blender, for converting .blend files

## Vehicle models


## Interactions explained
``` python
from ursina import *            # this will import everything we need from ursina with just one line.

app = Ursina()
ground = Entity(
    model = 'cube',
    color = color.magenta,
    z = -.1,
    y = -3,
    origin = (0, .5),
    scale = (50, 1, 10),
    collider = 'box',
    )

app.run()                       # opens a window and starts the game.
```


* [Minecraft Clone](/samples/minecraft_clone.py)

* [Platformer Game](/samples/platformer.py)


## 基于ursina的城市自动驾驶测试场景可视化
## 设计动机与思路
## 目标

## 测试项

## 场景与模型架构

