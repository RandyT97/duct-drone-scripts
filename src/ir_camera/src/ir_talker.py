#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from itertools import chain

import time
import busio
import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)
publish_rate = 1 # per second

class Dim:
  def __init__(self, label, size, stride):
    self.label = label
    self.size = size
    self.stride = stride
    
def talker():
  pub = rospy.Publisher('ir_data', Float32MultiArray, queue_size = 10)
  rospy.init_node('ir_talker')
  rate = rospy.Rate(publish_rate)

  dat = Float32MultiArray()

  dat.layout.dim.append(MultiArrayDimension("height", 8, 64))
  dat.layout.dim.append(MultiArrayDimension("width", 8, 64))
  dat.layout.data_offset = 0

  while not rospy.is_shutdown():
    rospy.loginfo(amg.pixels)
    answer=[]
    dat.data = [j for sub in amg.pixels for j in sub]
    pub.publish(dat)
    rate.sleep()

if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass
