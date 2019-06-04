# robot_summer

Some helpful ROS related guides:

[Easy navigation guide](http://kaiyuzheng.me/documents/navguide.pdf)

[Learning Turtlebot](https://learn.turtlebot.com/)

[leg detection package](http://wiki.ros.org/leg_detector)

[change indigo to kinetic](http://wiki.ros.org/turtlebot/Tutorials/indigo/Turtlebot%20Installation)


# Turtlebot package installation
1. Go get a virtual machine with a Ubunu 16.04 image. (may update this more later) 
2. Follow [this](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment) to install ROS. Make sure you put Kinetic as the <distro>. Make sure you also set up your catkin workspace.
3. In a terminal, 
```bash
sudo apt-get install ros-kinetic-turtlebot ros-kinetic-turtlebot-apps ros-kinetic-turtlebot-interactions ros-kinetic-turtlebot-simulator ros-kinetic-kobuki-ftdi ros-kinetic-ar-track-alvar-msgs
```
4. You should now have the turtlebot packages
5. Make sure you source your bash file
```bash
source devel/setup.bash
```
and if you've set up a catkin workspace,
```bash
source ~/catkin_ws/devel/setup.bash
```
6. In the terminal type
```bash
rospack find t
```
and hit tab twice to display which ros packages are available. Make sure there are turtlebot packages.
7. Attempt to launch gazebo
```bash
roslaunch turtlebot_gazebo turtlebot_world.launch
```

