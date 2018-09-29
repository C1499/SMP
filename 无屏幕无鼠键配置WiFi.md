# 无屏幕连接树莓派：  

### 第一步开启SSH服务：  

镜像烧录完毕后，在文件boot分区新建一个文件 ssh 注意要小写且不要有任何扩展名。  

### 第二步连接wifi：  

在 boot 分区，也就是树莓派的 /boot 目录下新建 wpa_supplicant.conf 文件，按照下面的格式修改  
```
country=CN  
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev  
update_config=1  
 
network={  
ssid="无线网络名"  
psk="密码"  
key_mgmt=WPA-PSK （如果wifi无密码或者使用wep加密则该值为NONE）  
priority=1（连接优先级，数字越大优先级越高，不可为负数）  
}  
 
network={  
ssid="网络的ssid"  
psk="密码"  
key_mgmt=WPA-PSK  
priority=2  
scan_ssid=1 （连接隐藏wifi时需要指定此值为1）  
}
```

