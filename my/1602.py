#!/usr/bin/python
 
from lcd1602 import *
from datetime import *
import commands
import time
from subprocess import * 
cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1|head -n1"
#cmd = ifconfig eth0 |grep 'inet' | cut -d: -f2 | awk '{print $2}'|head -n1

def get_ip_info(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def get_time_now():
    #return datetime.now().strftime('    %H:%M:%S\n   %Y-%m-%d')
	return datetime.now().strftime('   %Y-%m-%d   ')

lcd = lcd1602()
 
while(1):
	try:    
    		lcd.clear()
        	ipaddr = get_ip_info(cmd)
		lcd.message('IP %s' % ( ipaddr ) )
       		lcd.message( get_time_now() )
		time.sleep(5)
	except KeyboardInterrupt:
    		print "break"
		break
lcd.clear()
