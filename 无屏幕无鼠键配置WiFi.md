# ����Ļ������ݮ�ɣ�  

### ��һ������SSH����  

������¼��Ϻ����ļ�boot�����½�һ���ļ� ssh ע��ҪСд�Ҳ�Ҫ���κ���չ����  

### �ڶ�������wifi��  

�� boot ������Ҳ������ݮ�ɵ� /boot Ŀ¼���½� wpa_supplicant.conf �ļ�����������ĸ�ʽ�޸�  
```
country=CN  
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev  
update_config=1  
 
network={  
ssid="����������"  
psk="����"  
key_mgmt=WPA-PSK �����wifi���������ʹ��wep�������ֵΪNONE��  
priority=1���������ȼ�������Խ�����ȼ�Խ�ߣ�����Ϊ������  
}  
 
network={  
ssid="�����ssid"  
psk="����"  
key_mgmt=WPA-PSK  
priority=2  
scan_ssid=1 ����������wifiʱ��Ҫָ����ֵΪ1��  
}
```

