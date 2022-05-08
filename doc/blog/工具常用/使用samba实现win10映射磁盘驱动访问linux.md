## 使用samba实现win10映射磁盘驱动访问linux



**使用**

-----



> 安装samba

```shell
sudo apt install samba
```

这里可能会提示获取dhcp的配置信息，以及安装dhcp-client客户端，确认就好



samba的配置文件一般在

```shell
/etc/samba/smb.conf
```



> 简单配置smb.conf

```shell
#案例
#打开 sudo vim /etc/samba/smb.conf
#最后添加 示例：

[user]     #共享名称database
 
    comment = "comment"  #描述信息
 
    path = /tmp/user1 #共享目录
 
    public = no #关闭所有人可见
 
    writable = yes #是否有写权限
```

自己机器的配置

```shell
[luyi]
    comment = "luyi"
    path = /home/luyi
    writable = yes
```

添加用户并设置密码

```shell 
pdbedit -a luyi
```

最后打开win10的计算机映射网络驱动器

over



```shell
#lz使用的是debian10，samba版本为4.9.5-debian，samba服务名为smbd
#所以启动之类的需要 service smdb start，之前用samba tab出来的一直报错找了半天原因......
```



注意：虚拟机要保证跟宿主机之间可以相互ping通

​			win10宿主机建议开启以下配置：

​				我的电脑右键 --> 管理 --> 服务和应用程序 --> 服务

​				找到TCP/IP NetBIOS Helper，将启动类型修改为自动并且启动它

​			

安装虚拟机，使用workstation吧，vitrualbox一直有问题，后续版本还跟win10不兼容



**资料了解**

-----



​	Samba是一个能让Linux系统应用Microsoft网络通讯协议的软件，而SMB是Server Message Block的缩写，即为服务器消息块 ，SMB主要是作为Microsoft的网络通讯协议，后来Samba将SMB通信协议应用到了Linux系统上，就形成了现在的Samba软件。后来微软又把 SMB 改名为 CIFS（Common Internet File System），即公共 Internet 文件系统，并且加入了许多新的功能，这样一来，使得Samba具有了更强大的功能。

​	......

​	......

​	这里主要介绍一下配置文件，其他更多的自行科学上网查看



**配置文件的大概组成global、homes、printers**

[global] 

> 定义全局的配置

```shell
    workgroup = MYGROUP							#工作组，按win下的理解即可
    											#win默认为WORKGROUP
    											
    server string = Samba Server Version %v
    
    security = user								#security默认(user)用户级别，
    											#详见下关于security级别
    											
    passdb backend = tdbsam						# passdb backend （用户后台），
    											#samba有三种用户后台：
    											#smbpasswd, tdbsam和ldapsam
    											#详见下关于samba三种用户后台
    											
    load printers = yes							#设置打印机相关
    cups options = raw							#设置打印机相关
```

[homes] 

> 共享用户自己的家目录
>
> 针对共享目录个别的设置，只对当前的共享资源起作用
>
> 也就是说，当用户登录到samba服务器上时实际上是进入到了该用户的家目录，用户登陆后，共享名不是homes而是用户自己的标识符，对于单纯的文件共享的环境来说，这部分可以注视掉。

```
    comment = Home Directories

    browseable = no

    writable = yes
```

[printers]

>该部分内容设置打印机共享

```
    comment = All Printers

    path = /var/spool/samba

    browseable = no

    guest ok = no

    writable = no

    printable = yes
```



> 关于security级别

```tex
安全级别解析：

1) share模式：不用进行权限匹配检查即可访问共享资源，安全性比较差；

2) user模式：需要对用户名和密码进行验证，通过后才能访问共享资源，具有一定的安全性；

3) server模式：通过指定的服务器对用户名和密码进行验证，如果不通过，客户端会用user级别访问；

4) domain模式：domain级别的Samba服务器只作为域的成员客户端加入Windows域中，由Windows域控制器来完成对用户名和密码的验证；

5) ads模式：如果Samba服务器以ads方式加入Windows域中，将具备domian级别的所有功能，并且可以完成对用户名和密码的验证工作。
```

> 关于samba三种用户后台

```tex
smbpasswd：该方式是使用smb工具smbpasswd给系统用户（真实用户或者虚拟用户）设置一个Samba 密码，客户端就用此密码访问Samba资源。smbpasswd在/etc/samba中，有时需要手工创建该文件。
	-a：添加
　　 -x：删除
　　 -d：禁用
　　 -e：启用
　　 
　　 -L: 列出相关信息
　　 -v: 与L搭配使用，列出更多信息
　　 -w: 搭配L，使用旧版格式
　　 -r: 修改一个账户的相关信息
　　 -m: 后接机器代码(machine account)，与 domain model 有关！

tdbsam：使用数据库文件创建用户数据库。数据库文件叫passdb.tdb，在/etc/samba中。passdb.tdb用户数据库可使用smbpasswd –a创建Samba用户，要创建的Samba用户必须先是系统用户。也可使用pdbedit创建Samba账户。pdbedit参数很多，列出几个主要的：
	pdbedit –a username：新建Samba账户。
	pdbedit –x username：删除Samba账户。
	pdbedit –L：列出Samba用户列表，读取passdb.tdb数据库文件。
	pdbedit –Lv：列出Samba用户列表详细信息。
	pdbedit –c “[D]”–u username：暂停该Samba用户账号。
	pdbedit –c “[]”–u username：恢复该Samba用户账号。

ldapsam：基于LDAP账户管理方式验证用户。首先要建立LDAP服务，设置“passdb backend = ldapsam:ldap://LDAP Server”
```

> global其他的参数

```shell
netbios name = MYSERVER 	# 设置出现在“网上邻居”中的主机名

hosts allow = 127. 192.168.12. 192.168.13. 	# 用来设置允许的主机，如果在前面加”;”则表示允许所有主机

log file = /var/log/samba/%m.log 	#定义samba的日志，这里的%m是上面的netbios name

max log size = 50 	# 指定日志的最大容量，单位是K
```





 **pdbedit**参数及功能：pdbedit命令是samba的用户管理命令。

| 参数             | 作用                   |
| ---------------- | ---------------------- |
| -a user          | 建立samba的用户user    |
| -r user          | 修改samba的用户user    |
| -x user          | 删除samba的用户user    |
| -L               | 列出用户列表           |
| -Lv              | 列出用户详细信息的列表 |
| -c "[D]" -u user | 暂停该samba用户user    |
| -c "[D]" -u user | 恢复该samba用户user    |

​    ![img](https://img-blog.csdnimg.cn/20190123163756725.png)

