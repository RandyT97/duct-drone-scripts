#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension

import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4 # not numbered the same as other files. 4 corresponds to pin 7
publish_rate = 0.25 # per second


def talker():
  pub = rospy.Publisher('humidity_data', Float32MultiArray, queue_size = 10)
  rospy.init_node('humidity_sensor')
  rate = rospy.Rate(publish_rate)
  dat = Float32MultiArray()
  dat.layout.dim.append(MultiArrayDimension("length", 2, 2))
  dat.layout.data_offset = 0 

  while not rospy.is_shutdown():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    rospy.loginfo([temperature, humidity])
    dat.data = [temperature, humidity]
    pub.publish(dat)
    rate.sleep()



if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass
