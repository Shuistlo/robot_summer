# This is a tutorial for creating your own world for a Turtlebot given you have a floorplan you know the measurements of

Preliminary knowledge:
1. We are currently using turtlebot_stage to create a map for a turtlebot. The stage package itself can be used to create worlds for different robots. However, should you ever find yourself working with
a different robot, [you need to consider if your robot has the hardware potential to create a more accurate map for itself than using a converted floorplan](http://wiki.ros.org/gmapping#Hardware_Requirements). 
2. You will need the resoluion and scale of the map to accurately create a map. 
3. Maps are handled in the navigation stack by a package called map_server. Black is treated as a solid obstacle, white as free spaces, and grey as unknown. Any other colours will also be treated as unknowns.
4. Yaml and pmg files can be generated from a png of a map. An easy way is via the script detailed in this [youtube video](https://www.youtube.com/watch?v=ySlU5CIXUKE). The map_server itself also has a map_saver functionality.


Steps:
1. Make sure you've created a suitable map from a floor plan. I would advise the following:<br>
		a. Make the map completely black and white if possible. <br>
		b. Remove any non permanent detail including chairs or small tables. <br>
		c. Make the walls thick black lines. <br>
2. There are some relevant instructions on creating a world file from [here](http://wiki.ros.org/turtlebot_stage/Tutorials/indigo/Customizing%20the%20Stage%20Simulator).<br>
		a. The size and pose of the floorplan inside the world file are *very* important. You will need to calculate the size and pose values from the resolution in your yaml file and your known dimensions of the map. (they should just be the dimensions in meters if your resolution is 0.05) The size is the length and height of the map and the pose is the exact middle of the map.<br>
		b. Add some obstacles if you want. <br>
		c. Add in a robot. It is very important that the coordinates of the robot in the world file match the coordinates you give on launch, or your robot will be physically in a different location than where it expects to be <br>
3. You can launch turtlebot_stage like this:
   ```bash
roslaunch turtlebot_stage turtlebot_in_stage.launch map_file:="<path to map file>/map.yaml" world_file:="<path to map file>/map.world" initial_pose_x:=36.5 initial_pose_y:=17 initial_pose_a:=0.0
```


