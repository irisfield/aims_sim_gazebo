#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node("follow_line_gazebo", anonymous=True)

    twist_pub_1 = rospy.Publisher("/car1/twist_cmd", Twist, queue_size=1)
    twist_pub_2 = rospy.Publisher("/car2/twist_cmd", Twist, queue_size=1)
    twist_pub_3 = rospy.Publisher("/car3/twist_cmd", Twist, queue_size=1)
    twist_pub_4 = rospy.Publisher("/car4/twist_cmd", Twist, queue_size=1)

    vel_msg = Twist()
    vel_msg.linear.x = 5.0

    while (not rospy.is_shutdown()):
        twist_pub_1.publish(vel_msg)
        twist_pub_2.publish(vel_msg)
        twist_pub_3.publish(vel_msg)
        twist_pub_4.publish(vel_msg)

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
