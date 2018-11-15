# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

C_LOW_1=        262
C_LOW_1_HALF=   277
C_LOW_2=        294
C_LOW_2_HALF=   311
C_LOW_3=        330
C_LOW_4=        349
C_LOW_4_HALF=   370
C_LOW_5=        392
C_LOW_5_HALF=   415
C_LOW_6=        440
C_LOW_6_HALF=   466
C_LOW_7=        494

C_MID_1=        523
C_MID_1_HALF=   554
C_MID_2=        587
C_MID_2_HALF=   622
C_MID_3=        659
C_MID_4=        698
C_MID_4_HALF=   740
C_MID_5=        784
C_MID_5_HALF=   831
C_MID_6=        880
C_MID_6_HALF=   932
C_MID_7=        988


C_HIGH_1=        1046
C_HIGH_1_HALF=   1109
C_HIGH_2=        1175
C_HIGH_2_HALF=   1245
C_HIGH_3=        1318
C_HIGH_4=        1397
C_HIGH_4_HALF=   1480
C_HIGH_5=        1568
C_HIGH_5_HALF=   1661
C_HIGH_6=        1769
C_HIGH_6_HALF=   1865
C_HIGH_7=        1976

import re
def playstr(mstr):
  cp=r"(L|M|H)(H*)(\d)([\d\.]+)(?:;([\d\.]+))*"
  mstr=re.subn(r"\#.+","",mstr)[0]
  c=re.findall(cp,mstr)
  for i in range(0,len(c),1):
    x='C_'+{'L':'LOW','M':'MID','H':'HIGH'}[c[i][0]]+'_'+c[i][2]
    if c[i][1]: x+='_HALF'
    p = GPIO.PWM(12,globals()[x])
    p.start(80) # dc
    time.sleep(float(c[i][3]))
    p.stop()
    if c[i][4]: time.sleep(float(c[i][4]))
    else: time.sleep(0.1)

try:
  playstr("""

 #低音
  L1.3 L2.3 L3.3 L4.3 L5.3 L6.3 L7.3
 #中音
  M1.3 M2.3 M3.3 M4.3 M5.3 M6.3 M7.3
 #高音
  H1.3 H2.3 H3.3 H4.3 H5.3 H6.3 H7.3
 #警笛
  M1.5 L5.6 M1.5 L5.6
 #一万个舍不得
  M3.1 M3.2 M3.1 M3.2 M5.2;0M3.2 M2.3;1
  M2.2;0 M2.2;.2 M2.2;0 M2.3;0 M5.2;0 M2.1 M3.2

  """)
except KeyboardInterrupt:
  print "退出"
GPIO.cleanup()
