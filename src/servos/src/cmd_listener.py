#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

frpin = 3
brpin = 5
flpin = 7
blpin = 11

# front right motor
GPIO.setup(frpin, GPIO.OUT)
pwmFR=GPIO.PWM(frpin, 50)
pwmFR.start(0)

# back right motor
GPIO.setup(brpin, GPIO.OUT)
pwmBR=GPIO.PWM(brpin, 50)
pwmBR.start(0)

# front left motor
GPIO.setup(flpin, GPIO.OUT)
pwmFL=GPIO.PWM(flpin, 50)
pwmFL.start(0)

# back left motor
GPIO.setup(blpin, GPIO.OUT)
pwmBL=GPIO.PWM(blpin, 50)
pwmBL.start(0)

def forward():
    rospy.loginfo("forward()")
    GPIO.output(frpin, True)
    pwmFR.ChangeDutyCycle(1)
    GPIO.output(brpin, True)
    pwmBR.ChangeDutyCycle(1)
    GPIO.output(flpin, True)
    pwmFL.ChangeDutyCycle(9)
    GPIO.output(blpin, True)
    pwmBL.ChangeDutyCycle(9)

def backward():
    rospy.loginfo("backward()")
    GPIO.output(frpin, True)
    pwmFR.ChangeDutyCycle(9)
    GPIO.output(brpin, True)
    pwmBR.ChangeDutyCycle(9)
    GPIO.output(flpin, True)
    pwmFL.ChangeDutyCycle(1)
    GPIO.output(blpin, True)
    pwmBL.ChangeDutyCycle(1)

def right():
    rospy.loginfo("right()")
    GPIO.output(frpin, True)
    pwmFR.ChangeDutyCycle(9)
    GPIO.output(brpin, True)
    pwmBR.ChangeDutyCycle(9)
    GPIO.output(flpin, True)
    pwmFL.ChangeDutyCycle(9)
    GPIO.output(blpin, True)
    pwmBL.ChangeDutyCycle(9)

def left():
    rospy.loginfo("left()")
    GPIO.output(frpin, True)
    pwmFR.ChangeDutyCycle(1)
    GPIO.output(brpin, True)
    pwmBR.ChangeDutyCycle(1)
    GPIO.output(flpin, True)
    pwmFL.ChangeDutyCycle(1)
    GPIO.output(blpin, True)
    pwmBL.ChangeDutyCycle(1)

def halt():
    rospy.loginfo("halt()")
    GPIO.output(frpin, False)
    pwmFR.ChangeDutyCycle(0)
    GPIO.output(brpin, False)
    pwmBR.ChangeDutyCycle(0)
    GPIO.output(flpin, False)
    pwmFL.ChangeDutyCycle(0)
    GPIO.output(blpin, False)
    pwmBL.ChangeDutyCycle(0)


def callback(msg):
  rospy.loginfo("Linear: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
  rospy.loginfo("Angular: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))
  
  if msg.linear.x > 0:
    forward()
  elif msg.linear.x < 0:
    backward()
  elif msg.angular.z < 0:
    right()
  elif msg.angular.z > 0:
    left()
  else:
    halt()

def listener():
  rospy.init_node('cmd_listener')
  rospy.Subscriber("/cmd_vel", Twist, callback)
  rospy.spin()

if __name__ == '__main__':
  listener()
