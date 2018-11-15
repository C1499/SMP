#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Connect: hello@tyrantek.com

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 35000)  # 通道为 12 频率为 50Hz
p.start(0)
while 1:
 try:  
     for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
 except KeyboardInterrupt:
    break
p.stop()
GPIO.cleanup()
