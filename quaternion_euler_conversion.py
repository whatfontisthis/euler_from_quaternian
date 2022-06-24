#!/usr/bin/python
import rospy
import math
from tf.transformations import euler_from_quaternion, quaternion_from_euler


'''From quaternion to euler'''
(roll, pitch, yaw) = euler_from_quaternion([0, 0, 0.7, 0.7])  # the conversion
print(roll, pitch, yaw)  # radian
print(math.degrees(roll), math.degrees(pitch), math.degrees(yaw))  # degrees


'''From euler to quaternion'''
[x, y, z, w] = quaternion_from_euler(roll, pitch, yaw)  # the conversion
print([x, y, z, w])
