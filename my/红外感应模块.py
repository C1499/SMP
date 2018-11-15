# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO_PIR = 11
print "PIR Module Test (CTRL-C to exit)"
GPIO.setup(GPIO_PIR,GPIO.IN) 
Current_State = 0
Previous_State = 0
try:
    print "Waiting for PIR to settle ..."
    while GPIO.input(GPIO_PIR)==1:
        Current_State = 0
        print "开始准备..."
    while True :
        Current_State = GPIO.input(GPIO_PIR)
        if Current_State==1 and Previous_State==0:
            print "测试有红外对象 "
            Previous_State=1
        elif Current_State==0 and Previous_State==1:
            print "继续准备中... "
            Previous_State=0
        time.sleep(0.01)
except KeyboardInterrupt:
    print "退出"
GPIO.cleanup()
