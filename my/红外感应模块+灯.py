# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)
print "PIR Module Test (CTRL-C to exit)"
GPIO.setup(13,GPIO.IN) 
GPIO.setup(15, GPIO.OUT)
Current_State = 0
Previous_State = 0
try:
	print "Waiting for PIR to settle ..."
	while GPIO.input(13)==1:
		if GPIO.input(13)== 1:
			GPIO.output(15,GPIO.HIGH)
		Current_State = 0
		print "开始准备..."
	while True :
		Current_State = GPIO.input(13)
		if Current_State==1 and Previous_State==0:
			print "测试有红外对象 "
			GPIO.output(15, GPIO.LOW)
			os.system("sudo python ./rgb.py")
			print 12
			Previous_State=1
		elif Current_State==0 and Previous_State==1:
			print "继续准备中... "
			GPIO.output(15, GPIO.HIGH)
			Previous_State=0
		time.sleep(0.01)
except KeyboardInterrupt:
	print "退出"
GPIO.cleanup()
