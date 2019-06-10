#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
from math import radians


class GoToPose:
    def __init__(self):
        self.goal_sent = False

        # What to do if shut down (e.g. Ctrl-C or failure)
        rospy.on_shutdown(self.shutdown)

        # setting publisher
        rospy.loginfo("setting publisher")
        self.pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
        # 5 hz
        r = rospy.Rate(5)

        spin_local = Twist()
        spin_local.linear.x = 0
        spin_local.angular.z = radians(90)

        # Tell the action client that we want to spin a thread by default
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("Wait for the action server to come up")

        # Allow up to 5 seconds for the action server to come up
        self.move_base.wait_for_server(rospy.Duration(5))

    def goto(self, pos, quat, actionTime):
        # Send a goal
        self.goal_sent = True
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),
                                     Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))
        # Start moving
        self.move_base.send_goal(goal)

        # Allow TurtleBot up to 60 seconds to complete task
        success = self.move_base.wait_for_result(rospy.Duration(actionTime))

        state = self.move_base.get_state()
        result = False

        if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            result = True
        else:
            self.move_base.cancel_goal()

        self.goal_sent = False
        return result

    # not sure if this is necessary
    def shutdown(self):
        self.pub.publish(Twist())
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("Stop")

    def makelargespin(self):
        r = rospy.Rate(5)

        spin_local = Twist()
        spin_local.linear.x = 0
        spin_local.angular.z = radians(91)
        for x in range(0, 90):
            self.pub.publish(spin_local)
            r.sleep()

    def makesmallspin(self):
        r = rospy.Rate(5)

        spin_local = Twist()
        spin_local.linear.x = 0
        spin_local.angular.z = radians(91)
        for x in range(0, 45):
            self.pub.publish(spin_local)
            r.sleep()

    def halfMoon(self):
        r = rospy.Rate(6)
        spin_local = Twist()
        spin_local.linear.x = 0
        spin_local.angular.z = radians(45)
        for x in range(0, 25):
            self.pub.publish(spin_local)
            r.sleep()


    # waits 4 seconds for the door to open
    def awaitDoor(self):
        self.goal_sent = True
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = 1.5  # 1.5 meters
        goal.target_pose.pose.orientation.w = 1.0  # go forward

if __name__ == '__main__':
    try:
        # will spin a few times to localize
		rospy.init_node('nav_test', anonymous=False)
        navigator = GoToPose()
        #navigator.makesmallspin()

        # Customize the following values so they are appropriate for your location

        xText = raw_input("x Coordinate: ")
        yText = raw_input("y Coordinate: ")
        actionTime = raw_input("time to reach goal: ")
        position = {'x': float(xText), 'y': float(yText)}
        quaternion = {'r1': 0.000, 'r2': 0.000, 'r3': 1.000, 'r4': 0.000}

        #position = {'x': 30.7, 'y': 12.5}
       # quaternion = {'r1': 0.000, 'r2': 0.000, 'r3': 1.000, 'r4': 0.000}
        
        rospy.sleep(1)
        rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
        success = navigator.goto(position, quaternion, 60)

        if success:
            rospy.loginfo("GOAL REACHED")
        else:
            rospy.loginfo("GOAL FAILED")

        # Sleep to give the last log messages time to be sent
        rospy.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")

