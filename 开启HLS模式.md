<h2>����SRS </h2>



```
./configure --with-nginx && make
```




<h2>�����ַ�hls��m3u8/ts����nginx��</h2>



```
sudo ./objs/nginx/sbin/nginx
```




<h2>��дSRS�����ļ�����ϸ�ο�HLS�ַ�</h2>

���������ݱ���Ϊ�ļ���Ʃ��conf/hls.conf������������ʱָ���������ļ�(srs��conf�ļ����и��ļ�)��

# conf/hls.conf

```
listen              1935;
max_connections     1000;
vhost  __defaultVhost__ {
   hls {
       enabled         on;
       hls_path        ./objs/nginx/html;
    	 hls_fragment    10;
    	hls_window      60;

    }
}
```


����SRS




./objs/srs -c conf/hls.conf







HLS����ַΪ�� http://192.168.1.170/live/livestream.m3u8