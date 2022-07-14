#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node("move_vehicles_test", anonymous=True)

    twist_pub_1 = rospy.Publisher("/car1/twist_cmd", Twist, queue_size=1)
    twist_pub_2 = rospy.Publisher("/car2/twist_cmd", Twist, queue_size=1)
    twist_pub_3 = rospy.Publisher("/car3/twist_cmd", Twist, queue_size=1)
    twist_pub_4 = rospy.Publisher("/car4/twist_cmd", Twist, queue_size=1)

    vel_msg_1 = Twist()
    vel_msg_2 = Twist()
    vel_msg_3 = Twist()
    vel_msg_4 = Twist()

    vel_msg_1.linear.x = 2.0
    vel_msg_2.linear.x = 2.0
    vel_msg_3.linear.x = 2.0
    vel_msg_4.linear.x = 2.0

    rate = rospy.Rate(20)
    while (not rospy.is_shutdown()):
        twist_pub_1.publish(vel_msg_1)
        twist_pub_2.publish(vel_msg_2)
        twist_pub_3.publish(vel_msg_3)
        twist_pub_4.publish(vel_msg_4)
        rate.sleep()

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
