#!/usr/bin/env python3

import sys
# sys.path.append('/usr/lib/python2.7/dist-packages')
# sys.path.remove()
import rospy
import time
import math

from astar import *


def main():
    rospy.init_node('astar_turtlebot', anonymous=True)

    if(len(sys.argv) > 1):
        start_state = (-1.3, 6.2, 0.1)
        goal_state = (1.3, -6.2, 0.1)
        RPM1 = 10
        RPM2 = 15
        clearance = 5
    else:
        start_state = None
        goal_state = (1.3, -6.2, 0.1)
        RPM1 = 10
        RPM2 = 15
        clearance = 5

    astr = AStar(start_state, RPM1, RPM2, clearance, 0.5, 0.1, 0.1, 30.0) # [RPM1, RPM2, clearance, threshold, step_size, dt, theta_step]
    rospy.spin()

if __name__ == '__main__':
    main()