#!/usr/bin/env python

import rospy
from sensor_msgs import Image

def listener():
    rospy.init_node('rgb_camera', anonymous=True)
    rospy.Subscriber("camera", Image, callback)
    rospy.spin()

def callback(data):
    #do somethin
    rospy.loginfo(rospy.get_caller_id() + "we listenign to the camera now and it says %s", data.data)
