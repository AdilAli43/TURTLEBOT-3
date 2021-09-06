#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseArray
global listopose

def callback(data):
    global listpose
    rospy.loginfo(data.poses)
    listpose.append(data.poses)
	

def listener():
    
    global listpose
    listpose = []
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/toy_pose_topic', PoseArray, callback)
    
    
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
    
