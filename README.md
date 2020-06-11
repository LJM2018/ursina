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

## Objectives
  * Test if AV can safely and efficiently merge into traffic
  * Test if AV can leverge risk and benefit while picking a better lane
  * Test if AV can navigate safely when pedestrian cross the street

## 测试目标
  * 测试自动驾驶汽车是否能安全有效率地汇入车流
  * 测试自动驾驶汽车是否在原车道堵塞或者缓慢时能权衡利弊做出合适的选择
  * Test if AV can navigate safely when pedestrian cross the street

## Vehicle models
![twocubes](/docs/car1.jpg) (image from ursina)
To simplify the situaltion, we will use two combined cubes entity in ursina to represent a car

## Interactions explained
![handdrew](/docs/scenario.jpg)
  * Increase speed of other vehicles
  * Decrease speed of other vehicles
  * Stop/Move the right lane traffic (the one AV originally drive in)
  * Increase the gap between other vehicles
  * Decrease the gap between other vehicles


## 场景与模型架构

