<h2>编译SRS </h2>



```
./configure --with-nginx && make
```




<h2>启动分发hls（m3u8/ts）的nginx。</h2>



```
sudo ./objs/nginx/sbin/nginx
```




<h2>编写SRS配置文件。详细参考HLS分发</h2>

将以下内容保存为文件，譬如conf/hls.conf，服务器启动时指定该配置文件(srs的conf文件夹有该文件)。

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


启动SRS




./objs/srs -c conf/hls.conf







HLS流地址为： http://192.168.1.170/live/livestream.m3u8