#! /usr/bin/env python
 
import rospy
from sensor_msgs.msg import LaserScan
 
def listener():
    rospy.init_node('scan_values')
    sub = rospy.Subscriber('scanReader', LaserScan, callback)
    rospy.spin()

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", len(msg.ranges))

if __name__ == '__main__':
    listener()
