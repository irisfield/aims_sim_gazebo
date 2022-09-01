#!/usr/bin/env python3
import rospy

import tf
#from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, PoseStamped, PoseWithCovarianceStamped, PoseArray, PointStamped

ran_cb = False

def odomCB(msg):
    global ran_cb
    if not ran_cb:
        rospy.loginfo("Publishing transforms...")
        ran_cb = True

    pos = msg.pose.pose.position
    r = msg.pose.pose.orientation
    # rospy.loginfo("Quat: {}".format(r))
    br.sendTransform((pos.x, pos.y, pos.z),
                     (r.x, r.y, r.z, r.w),
                     msg.header.stamp,
                     msg.header.frame_id)


if __name__ == "__main__":
    rospy.init_node("transform_broadcaster")
    odom_topic = rospy.get_param("~odom_topic")

    br = tf.TransformBroadcaster()
    rospy.Subscriber(odom_topic, PoseStamped, odomCB)
    rospy.spin()
