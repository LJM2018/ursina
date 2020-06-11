# Visualization of test driving scenario based on ursina
Ursina is an easy to use game engine/framework for python. (https://www.ursinaengine.org/)
# 基于ursina的城市自动驾驶测试场景可视化
Ursina 是一款使用python语言的易用游戏引擎 (https://www.ursinaengine.org/)
![Banner](/docs/top8.jpg) (image from Mobileyes)


## Motivation
Safe and efficient driving experience is crucial for autonomous vehicles. Although AVs are equipping with more advanced sensors nowadays, autonomous drving remained challenging in urban environments. This is especially true when driving in the intersection with heavy traffic. Under such scenario, most human drivers tend to be aggressive and it requires highly intelligent motion planning algorithm to safely merge into traffic and select a better lane when needed. This visualization construct this common yet challenging scenario with ursina that allows users to test the performance of motion planning algorithm under different traffic speed, gaps between vehicles and the level of aggressiveness of other vehicles. This may help engineers to better balance the algirthm to fit in different situations.

## 设计动机与思路
安全快捷的驾驶体验一直是自动驾驶汽车研究的重中之重。虽然现今的智能汽车都装备了更先进的传感器，在城镇环境下的自动驾驶仍具挑战性，尤其是是在十字路口以及车流密集的环境。在该环境下，大多数人类驾驶员的驾驶行为趋向侵略性。而这也要求运动规划算法足够智能来帮助汽车安全地汇入车流，并在需要时选择一条更快捷的车道。该可视化系统使用ursina来重建这种常见但是具有挑战性的场景，允许用户调整不同车流速度、车与车之间的间隙以及不同驾驶风格来测试其运动规划算法的表现。这可以帮助工程师更好的平衡算法的风格以适应不同的状况。

![frommobileyes](/docs/sim8.jpg) (image from Mobileyes)

## Assumptions & Objectives
Assuming that the ego vehicle knows every parameter in the simulation(speed and gaps of other cars)
  * Test if AV can safely and efficiently merge into traffic
  * Test if AV can leverge risk and benefit while picking a better lane

## 假定情况与测试目标
假定被测试的车辆知道所有模拟中的参数（其他车辆的速度与间距）
  * 测试自动驾驶汽车是否能安全有效率地汇入车流
  * 测试自动驾驶汽车是否在原车道堵塞或者缓慢时能权衡利弊做出合适的选择

## Vehicle models
## 车辆模型
![twocubes](/docs/car1.jpg) (image from ursina)
To simplify the situaltion, we will use two combined cubes entity in ursina to represent a car

为了简化场景，我们可以使用两个ursinane自带的正方体来表示车辆

## Interactions explained
## 交互逻辑
![handdrew](/docs/scenario3.jpg)

After selecting the lane (inside the blue box)that modifications applied to(if no lane selected, changes apply to all), users can change the following settings by clicking:
  1) Increase speed of other vehicles
  2) Decrease speed of other vehicles
  3) Increase the gap between other vehicles
  4) Decrease the gap between other vehicles
  5) Stop/Move the selected lane's traffic

在选择相应的车道后(蓝色框)，所有的改变将应用到该路线上的车辆(如果没有选择，改变会应用于所有车辆)，用户可以通过点击按钮改变以下参数:
  1) 提高车流速度
  2) 降低车流速度
  3) 停止/移动 选择的车道线的车流
  4) 增加车流中车辆的间距（安全距离）
  5) 减少车流中车辆的间距（安全距离）

## Test cases
## 测试用例
  1) If the traffic is ok in lane 2 and no incoming cars from the left, the ego car is expected to maintain its lane and turn right as normal
  
  如果车道2车辆较少并且左方无车辆正在汇入，被测试车辆应该保持其原先的车道并正常右转
  ![handdrew](/docs/test1.jpg)

  2) If there are cars coming from left to merge and there lane 2 is blocked by slow traffic, while traffic in lane 1 is moving faster, the ego car is expected to slowly push so that it can merge into traffic and change its lane to lane 1.
  
  如果左方有车辆汇入，车道2车流行驶缓慢而车道1的车流行驶较快，被测试车辆应缓慢推进直至汇入左边车流并转进车道1
  ![handdrew](/docs/test2.jpg)