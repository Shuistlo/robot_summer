# robot_summer

Some helpful ROS related guides:

[Easy navigation guide](http://kaiyuzheng.me/documents/navguide.pdf)

[Learning Turtlebot](https://learn.turtlebot.com/)

[leg detection package](http://wiki.ros.org/leg_detector)

[change indigo to kinetic](http://wiki.ros.org/turtlebot/Tutorials/indigo/Turtlebot%20Installation)

# Multi Map Server
changing maps will not work in Stage. We will need to edit Stage if we want it to work in simulation.

please read the multi map server for instructions

[The Repository for the multi map server](https://github.com/Shuistlo/multi_map_server)

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
  
  # Stageros
  1. Use the find command for ros packages to see if you can find the stage_ros package
  ```bash
rospack find stage_ros
```
  If it doesn't appear you'll need to install the package:
  ```bash
sudo apt-get install ros-kinetic-stage_ros
```
 2. Download the maps off of this repository
 3. A world can be generated using three files: a png/pmg image file of the actual map, a yaml file containing map metadata, and a world file describing the world and its dimensions. Feel free to take a look inside each one. I'll include a seperate file for generating your own world if you ever want to do another building.
 4. Launch the turtlebot in stage! *Make sure you edit the following command to suit the location of your files*
   ```bash
roslaunch turtlebot_stage turtlebot_in_stage.launch map_file:="/home/shu/maps/7thedited.yaml" world_file:="/home/shu/maps/7thedited.world" initial_pose_x:=36.5 initial_pose_y:=17 initial_pose_a:=0.0
```
  
  # Problems
  1. Gazebo on a VM seems to crash quite a bit
  2. Stagge possibly doesn't work on VM either. If you are still adamant about using a vm you may try [this](http://wiki.ros.org/turtlebot_stdr) but I wouldn't if I were you.
  3. The multi_map_server is in another repo (see above). This needs to go in the same level as the robot_summer project

