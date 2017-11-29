#!/usr/bin/env python

import rospy
import yaml
from ros_pose_reader.msg import *
from ros_pose_reader.srv import *
from geometry_msgs.msg import Pose2D

pose_list = []

def handle_labeled_pose_list(req):
    pose = LabeledPose("storage_A", Pose2D(1.7, 4.3, 0.1))
    pose2 = LabeledPose("storage_B", Pose2D(4.89, 33.3, -0.2))
    pose3 = LabeledPose("packaging_area_A", Pose2D(12.17, 0.2333, 3.1))
    pose_list.append(pose)
    pose_list.append(pose2)
    pose_list.append(pose3)
    return LabeledPoseListResponse(pose_list)

def main():
    rospy.init_node('read_yaml')
    service = rospy.Service('labeled_pose_list', LabeledPoseList, handle_labeled_pose_list)
    print "Ready to send pose list"
    rospy.spin()


if __name__ == "__main__":
	main()
