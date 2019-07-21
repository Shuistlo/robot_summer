#! /usr/bin/python

import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

#lower and upper bounds are of a colour you want to filter in hsv
#follow https://toolstud.io/color/rgb.php to convert a colour into hsv
def colourFilter(image, lowerBound, upperBound):
	hsv_image = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)
	mask = cv2.inRange(hsv_image, lowerBound, upperBound)
	return cv2.bitwise_and(image, image, mask=mask)
