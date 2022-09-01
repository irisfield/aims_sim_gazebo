#!/usr/bin/env python3

import rospy
import sys
import os
import numpy as np
import argparse
import time
import math
from Queue import PriorityQueue

# Importing messages
from std_msgs.msg import String
from geometry_msgs.msg import Pose, PoseStamped, PoseWithCovarianceStamped, PoseArray, Twist
from nav_msgs.msg import OccupancyGrid, Path
from visualization_msgs.msg import Marker
import jsk_recognition_msgs.msg
import tf
from tf import TransformListener


class OpenLoop:

    def __init__(self, cmds):
        self.cmds = cmds

        #self.turtlebot_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.twist_pub_1 = rospy.Publisher("/car1/twist_cmd", Twist, queue_size=1)

    def track_path(self):

        rate = rospy.Rate(1)

        for cmd in self.cmds:
            vel_msg_1 = Twist()
            vel_msg_1.linear.x = cmd[0][0]
            vel_msg_1.angular.z = -cmd[1][0]
            print("lin: {}, ang: {}".format(vel_msg_1.linear.x, vel_msg_1.angular.z))

            self.twist_pub_1.publish(vel_msg_1)
            rate.sleep()

        vel_msg_1.linear.x = 0
        vel_msg_1.angular.z = 0
        print("lin: {}, ang: {}".format(vel_msg_1.linear.x, vel_msg_1.angular.z))

        self.twist_pub_1.publish(vel_msg_1)
