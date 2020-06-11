# Visualization of test driving scenario based on ursina
Ursina is an easy to use game engine/framework for python. (https://www.ursinaengine.org/)

![Banner](/docs/top8.jpg) (image from Mobileyes)


## Motivation
Safe and efficient driving experience is crucial for autonomous vehicles. Although AVs are equipping with more advanced sensors nowadays, autonomous drving remained challenging in urban environments. This is especially true when driving in the intersection with heavy traffic. Most of the time human drivers tend to be aggressive and it requires highly intelligent motion planning algorithm to safely merge into traffic and select a better lane when needed. This visualization construct this common yet challenging scenario with ursina that allows users to test the performance of motion planning algorithm under different traffic speed, gaps between vehicles and the level of aggressiveness of other vehicles. This may help engineers to better balance the 

![frommobileyes](/docs/sim8.jpg) (image from Mobileyes)
## Objectives
  * Test if AV can safely merge into traffic
  * Test if AV can leverge risk and benefit while picking a faster lane
  * Test if AV can navigate safely when pedestrian cross the street

## Vehicle models
![twocubes](/docs/car1.jpg) (image from ursina)
To simplify the situaltion, we will use two combined cubes entity in ursina to represent a car

## Interactions explained
![twocubes](/docs/scenario.png)
  * Increase speed of other vehicles
  * Decrease speed of other vehicles
  * Stop/Move the right lane traffic (the one AV originally drive in)
  * Increase the gap between other vehicles
  * Decrease the gap between other vehicles

## 基于ursina的城市自动驾驶测试场景可视化
## 设计动机与思路
## 目标
## 测试项
## 场景与模型架构

