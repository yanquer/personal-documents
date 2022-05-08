# nginx

https://www.jianshu.com/u/2cd381f93179

https://www.jianshu.com/p/f81195da5a22



### 操作

#### Master 和 Worker 进程

Nginx包含一个`master`进程和一到多个`worker`进程。如果配置了`缓存`的话，还将包含`缓存加载进程`和`缓存管理进程`。

`master`进程主要负责读取配置文件，并控制管理`workder`进程。

`worker`进程负责处理请求。Nginx基于操作系统的调度机制高效地在`worker`进程间分配请求。可以在`nginx.conf`配置文件中设置`worker`进程的数量，一般设置为服务器的CPU内核数。

#### 管理 Nginx 进程

有两种方式让修改后的配置文件生效：

1. `停止`并`重启`Nginx
2. 给`master`进程发送信号

信号可以通过以下方式发送(nginx是可执行文件):



```undefined
nginx -s signal
```

其中`signal`常用选项如下：

- quit - 优雅的关闭，即处理完当前请求再关闭
- reload - 重新载入配置文件
- reopen - 重新打开日志文件
- stop - 立即关闭

也可以通过Linux的`kill`命令直接发送信号给`master`进程。Nginx的进程ID通常保存在`/usr/local/nginx/logs`或`/var/run`目录下的`nginx.pid`文件中。





默认配置路径

```
/etc/nginx/nginx.conf
```



配置内容

```yaml

# 配置http
http {

	server {	# 服务器配置，可以有多个server
	
		listen 127.0.0.1:8080	# 监听的端口
								# 如果不填写端口，则采用标准端口。
								# 如果不填写ip地址，则监听所有地址。
								# 如果缺少整条listen指令，则标准端口是80/tcp，
								# 默认端口是8000/tcp，由超级用户的权限决定。
		
        # 多个server配置了相同的ip地址和端口，Nginx会匹配server_name指令与请求头部的host字段。			# server_name指令的参数可以是精确的文本、通配符或正则表达式。
		server_name example.org www.example.org;
		
		# 如果有多个server_name匹配host字段，Nginx根据以下规则选择第一个相匹配的server处理请求：
		# 	1、精确匹配
		#	2、以*开始的最长通配符，如 *.example.org
		#	3、以*结尾的最长通配符，如 mail.*
		#	4、第一个匹配的正则表达式（根据在配置文件中出现的先后顺序）
		# 如果找不到任何与host字段相匹配的server_name，Nginx会根据请求端口将其发送给默认的server。
		# 默认server就是配置文件中第一个出现的server，
		# 也可以通过default_server指定某个server为默认server，
		# 如listen 0.0.0.0:8080 default_server
		
		
		# 根据URL将请求发送给不同的代理/处理不同的文件请求。由server指令中的location指令配置规则。
		
		# 匹配以/some/path/开始的请求URI
		location /some/path/ {
            ...
        }
        
        # ~	 用于匹配区分大小写的正则表达式，
        # ~* 用于匹配不区分大小写的正则表达式。
        
        # 匹配任意包含.html或.htm的URI。
        location ~ \.html? {
            ...
        }
        
        # Nginx先匹配前缀字符串，然后再匹配正则表达式。正则表达式拥有较高优先级，
        # 除非使用^~修饰符。在所有前缀字符串中，Nginx会挑选最精确的那个，也就是最长最匹配的那个。
        # 详细匹配过程如下：
        #	1、匹配所有前缀字符串；
        #	2、如果有一个 = 定义的精确匹配前缀字符串，停止继续匹配；
        #	3、如果 ^~ 在最长匹配的前缀字符串之前，将忽略正则表达式；
        #	4、存储最长的匹配前缀字符串；
        #	5、匹配正则表达式；
        #	6、找到第一个相匹配的正则表达，停止匹配过程，并执行该location指令；
        #	7、如果没有正则表达式匹配，则使用第4步存储的最长前缀字符串；
        
        # = 修饰符的典型应用是匹配 /请求。
        # 针对频繁访问/的情况，将location参数设置为= /可以加速处理过程，
        # 因为整个匹配过程在第一条之后就结束了。
        location = / {
            ...
        }
        
        
        # location指令内可以配置如何处理请求：处理静态文档或将请求转发给代理服务器。
        # 在下面的例子中，匹配第一个location的请求可以访问/data目录的文件，
        # 匹配第二个location的请求将被转发到www.example.com服务器。
        location /images/ {
        	# root指令指定了静态文件的文件系统路径，将与请求URI一起构成静态文件的完全路径
            root /data;
        }

        location / {
        	# proxy_pass指令将请求转发到代理服务器，并将代理服务器的响应返回给客户端。
            proxy_pass http://www.example.com;
        }
        
        # sub_filter指令支持重写或修改HTTP请求的响应内容，如替换某个字符串。该指令支持变量和链式替换。
        # 将指向服务器的链接改为指向代理服务器的链接：
        location / {
            sub_filter      /blog/ /blog-staging/;
            sub_filter_once off;
        }
        # 将http请求改为https请求，并将请求头部的本地主机地址改为主机名。
        # sub_filter_once指令用于告诉Nginx是否连续执行location中的sub_filter指令。
        # 注意：被sub_filter指令修改后的内容将不会再被其他sub_filter指令修改。
        location / {
            sub_filter     'href="http://127.0.0.1:8080/'    'href="https://$host/';
            sub_filter     'img src="http://127.0.0.1:8080/' 'img src="https://$host/';
            sub_filter_once on;
        }
        
        # error_page指令用于返回一个自定义错误页面和一个错误代码、
        # 修改响应中的错误代码或重定向到不同的URI。
        # 当Nginx未能找到请求的页面时，不会返回404，而会返回303和一个重定向到新页面指令。
        # 这通常用于处理客户端访问旧地址的情况。
        location /old/path.html {
            error_page 404 =301 http:/example.com/new/path.html;
        }
        
        # 有些网站在处理错误或重定向时，会要求立即返回一个状态码。最简单的方式就是使用return指令
        location /wrong/url {
            return 404;
        }
        # return指令的第一个参数是一个状态码。
        # 第二个是可选参数，可以是重定向的URL（当状态码是301、302、303和307时），
        # 也可以是返回的文本信息。
        location /permanently/moved/url {
            return 301 http://www.example.com/moved/here;
        }
        
        # 处理请求过程中，可以通过rewrite指令重复修改请求的URI。
        # rewrite指令包含2个必填参数和1个可选参数。
        # 第一个参数是请求URI必须匹配的正则表达式。第二个参数是要替换的目标URI。
        # 第三个为可选参数，可以是一个是否继续执行后续rewrite指令的标记，
        # 也可以发送一个重定向指令(状态码是301或302)。
        location /users/ {
            rewrite ^/users/(.*)$ /show?user=$1 break;
        }

	}
	
	# location和server中都可以包含多个rewrite指令。
    # Nginx从上到下依次磁性rewrite指令，每次进入server指令块时，rewrite指令都会被执行一次。
    # Nginx执行完一系列rewrite指令后，根据最新的URI来选择location指令。
    # 如果location中也包含rewrite指令，它们也将被依次执行，执行完毕后将重新选择location。
	server {
        ...
        rewrite ^(/download/.*)/media/(.*)\..*$ $1/mp3/$2.mp3 last;
        rewrite ^(/download/.*)/audio/(.*)\..*$ $1/mp3/$2.ra  last;
        return  403;
        ...
    }
    # 这个例子用于区分两套不同的URI。
    # 类似于/download/some/media/file的URI将被改写为/download/some/mp3/file.mp3。
    # 由于最后的标识last，Nginx将忽略随后的两条指令，然后以新的URI继续处理请求。
    # 同样地，类似于/download/some/audio/file的URI将被改写为/download/some/mp3/file.ra。
    # 如果请求URI都不匹配上述两条rewrite指令，Nginx将返回403错误代码。
    
    # rewrite指令可以包含以下两种参数，用于中断处理过程：
    #	last - 停止执行当前server或location中的rewrite指令，并以新的URI查找新的location；
    #	break - 停止执行当前上下文环境内的rewrite指令，并不以新的URI查找新的location；

	
	# 以下例子中，当访问一个不存在的文件时，Nginx会将请求重定向到http://backend。
	# 由于error_page指令未指定重定向代码，该代码将由重定向后的http://backend返回。
	# 当请求文件未找到时，error_page指令将发起一个内部重定向。
	# $url变量持有当前请求的URI，并被传递给重定向。
	# 假设请求的/images/some/file文件未找到，将被重定向到/fetch/images/some/file，
	# 同时搜索新的location。最终，请求将被第二个location处理，并被代理到http://backend。
	# open_file_cache_errors指令可用于未找到请求文件时，禁止产生错误消息。
	# 在下例中可以忽略，因为错误已被正确处理。
	server {
        ...
        location /images/ {
            # Set the root directory to search for the file
            root /data/www;

            # Disable logging of errors related to file existence
            open_file_cache_errors off;

            # Make an internal redirect if the file is not found
            error_page 404 = /fetch$uri;
        }

        location /fetch/ {
            proxy_pass http://backend/;
        }
    }
	
}
```



##### 使用变量

通过在配置文件中使用变量，可以让Nginx以不同的方式处理请求。变量的值在运行时计算获得，并可作为参数传递给指令。变量必须以`$`开头。变量基于Nginx的状态定义信息，如正被处理请求的属性。

Nginx包含许多预设的变量，如`core HTTP`变量集，也可以使用`set`、`map`和`geo`指令来自定义变量。大多数变量都在运行时计算值，这些值一般都包含某个请求的相关信息。如`$remote_addr`包含了IP地址，而`uri`则包含了当前访问的`URI`。



##### 内置全局变量：

```bash
$args ：这个变量等于请求行中的参数，同$query_string
$content_length ： 请求头中的Content-length字段。
$content_type ： 请求头中的Content-Type字段。
$document_root ： 当前请求在root指令中指定的值。
$host ： 请求主机头字段，否则为服务器名称。
$http_user_agent ： 客户端agent信息
$http_cookie ： 客户端cookie信息
$limit_rate ： 这个变量可以限制连接速率。
$request_method ： 客户端请求的动作，通常为GET或POST。
$remote_addr ： 客户端的IP地址。
$remote_port ： 客户端的端口。
$remote_user ： 已经经过Auth Basic Module验证的用户名。
$request_filename ： 当前请求的文件路径，由root或alias指令与URI请求生成。
$scheme ： HTTP方法（如http，https）。
$server_protocol ： 请求使用的协议，通常是HTTP/1.0或HTTP/1.1。
$server_addr ： 服务器地址，在完成一次系统调用后可以确定这个值。
$server_name ： 服务器名称。
$server_port ： 请求到达服务器的端口号。
$request_uri ： 包含请求参数的原始URI，不包含主机名，如：”/foo/bar.php?arg=baz”。
$uri ： 不带请求参数的当前URI，$uri不包含主机名，如”/foo/bar.html”。
$document_uri ： 与$uri相同。
```



##### 关于root与alias

我们在`nginx.conf`里面写一个新的`server`；

```
server {
  listen 6002;
  server_name **.**.**.**;
  gzip on;
  
  location /admin {
    alias /projects/admin/;
    #指定主页
    index index.html;
    #自动跳转
    autoindex on;   
  }
  
  location /react {
    alias /projects/react/;
    #指定主页
    index index.html;
    #自动跳转
    autoindex on;   
  }
  
}
```

这里需要注意的就是`location`中的路径匹配问题，`root` 和 `alias` 的区别；

```
# 错误写法，会报404
location /admin {
    root /projects/admin/;
    #指定主页
    index index.html;
    #自动跳转
    autoindex on;   
}

location /react {
    root /projects/react/;
    #指定主页
    index index.html;
    #自动跳转
    autoindex on;   
}

# 当你访问 http://***/admin
# root ==> 实际指向的是 http://***/admin/projects/admin/, 这个时候肯定找不到index.html
# alias ==> 实际指向的是 http://***/admin, 可以在/projects/admin/找到index.html
```























### 踩过的坑



#### server_name

当配置了多个server时，且某个server有配置server_name时，会优先找server_name，就会访问不到我想要的那个server

另外，apt安装的nginx默认在 /etc/nginx/sites-available/default 下有一个默认的server配置，要避免于这个冲突或者直接删除



#### root

表示路径拼接（一般配置静态资源），比如

```
location /img {
	root /var/img/
}
```

实际经过 root 之后的路径为

/img/var/img



#### alias

表示新路径（从根路径开始），比如

```
location /img {
	alias /var/img/
}
```

实际经过 alias 之后的路径为

/var/img



#### return

return 状态码 字符串

第二个字符串可选，默认访问会以文件的形式下载



#### ~

表示开启正则匹配



#### proxy_pass

反向代理 表示动态请求，需要进行请求转发（如转发到tomcat）（用法与root基本一致）



#### upstream

负载均衡 

反向代理中，我们通过proxy_pass来指定Tomcat的地址，很显然我们只能指定一台Tomcat地址，那么我们如果想指定多台来达到负载均衡呢？

第一，通过**upstream**来定义一组Tomcat，并指定负载策略（IPHASH、加权论调、最少连接），健康检查策略（Nginx可以监控这一组Tomcat的状态）等。

第二，将proxy_pass替换成upstream指定的值即可。

**负载均衡可能带来的问题？**

负载均衡所带来的明显的问题是，一个请求，可以到A server，也可以到B server，这完全不受我们的控制，当然这也不是什么问题，只是我们得注意的是：**用户状态的保存问题，如Session会话信息，不能在保存到服务器上。**