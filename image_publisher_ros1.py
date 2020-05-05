#!/usr/bin/env python

import cv2
import rospy
from sensor.msg import Image

image_publisher = rospy.Publisher('image', Image, queue_size=1)
rospy.loginfo("initializing node")
rospy.init_node('image_tutorial')

rospy.loginfo("initializing camera")
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")


while True:
    ret, frame = cam.read()
    if not ret:
        rospy.loginfo("something went wrong. camera is ofline?")
        break
    if rospy.is_shutdown():
        rospy.loginfo("ros is off, closing")
        break
        
    cv2.imshow("image_tutorial", frame)
    pressed = cv2.waitKey(1)
    if pressed == chr(27).encode() or pressed == ord('q'):
        # closing application if esc or q pressed
        rospy.loginfo("closing button pressed, closing")
        break
        
    elif pressed == chr(32).encode():
        # publishing image if space pressed
        rospy.loginfo("sending_image")
        image_publisher.publish(frame)

# closing
cam.release()
cv2.destroyAllWindows()
