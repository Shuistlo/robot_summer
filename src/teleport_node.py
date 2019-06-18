#!/usr/bin/env python

import rospy
import multi_map_server.srv

class Teleporter:
    def __init__(self):
        #these are just here for reference
	rospy.init_node('the_only_node', anonymous=True)
        self.fifth = "/home/student/catkin_ws/src/robot_summer/maps/5thedited.yaml"
        self.sixth = "/home/student/catkin_ws/src/robot_summer/maps/6thedited.yaml"
        self.seventh = "/home/student/catkin_ws/src/robot_summer/maps/7thedited.yaml"

    def set_map_filename_client(self, floor):
        
        fileName = ""
        if floor == 5:
            fileName = self.fifth
        if floor == 6:
            fileName = self.sixth
        if floor == 7:
            fileName = self.seventh
        rospy.wait_for_service('set_map_filename')
        try:
            set_map_filename = rospy.ServiceProxy('set_map_filename', multi_map_server.srv.set_map_filename)
            response = set_map_filename(fileName)
            return response.success
        except rospy.ServiceException:
            rospy.logerr("{0} service call failed: {1}".format(self.srv_name))
            

if __name__ == "__main__":
	teleporter = Teleporter()
	success = teleporter.set_map_filename_client(6)
	rospy.loginfo("do tell if it works")

