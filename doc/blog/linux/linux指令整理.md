
## 一些按功能分类的指令

### ACL权限控制

查看acl权限

```
getfacle $filename
```

```
[root@localhost /]# getfacl project
#查看/prpject目录的ACL权限
#file: project <-文件名
#owner: root <-文件的属主
#group: tgroup <-文件的属组
user::rwx <-用户名栏是空的，说明是属主的权限
user:st:r-x <-用户st的权限
group::rwx <-组名栏是空的，说明是属组的权限
mask::rwx <-mask权限
other::--- <-其他人的权限
```

设置acl权限

```
setfacle 选项 文件名
```

选项

- -m：设定 ACL 权限。如果是给予用户 ACL 权限，则使用"u:用户名：权限"格式赋予；如果是给予组 ACL 权限，则使用"g:组名：权限" 格式赋予；
- -x：删除指定的 ACL 权限；
- -b：删除所有的 ACL 权限；
- -d：设定默认 ACL 权限。只对目录生效，指目录中新建立的文件拥有此默认权限；
- -k：删除默认 ACL 权限；
- -R：递归设定 ACL 权限。指设定的 ACL 权限会对目录下的所有子文件生效；

参考地址：http://c.biancheng.net/view/863.html

### 内核模块

insmod 与 modprobe 都是载入 kernel module，不过一般差别于 modprobe 能够处理 module 载入的相依问题。

比方你要载入 a module，但是 a module 要求系统先载入 b module 时，直接用 insmod 挂入通常都会出现错误讯息，不过 modprobe 倒是能够知道先载入 b module 后才载入 a module，如此相依性就会满足。

不过 modprobe 并不是大神，不会厉害到知道 module 之间的相依性为何，该程式是读取 /lib/modules/2.6.xx/modules.dep 档案得知相依性的。而该档案是透过 depmod 程式所建立。

#### lsmod

#### rmmod

参数：
-f ：强制将该模组移除掉，不论是否正被使用；
-w ：若该模组正被使用，则 rmmod 会等待该模组被使用完毕后，才移除他！

#### insmod

#### modprobe

 -a或--all 　载入全部的模块。
 -c或--show-conf 　显示所有模块的设置信息。
 -d或--debug 　使用排错模式。
 -l或--list 　显示可用的模块。
 -r, --remove //若在命令指定模块,则删除指定模块,否则,指定"自动清除"模式 
 -t或--type 　指定模块类型。
 -v或--verbose 　执行时显示详细的信息。
 -V或--version 　显示版本信息。
 -help 　显示帮助。
 -C, --config configfile //指定配置文件.默认使用/etc/modules.conf文件为配置文件

-c ：列出目前系统所有的模组！(更详细的代号对应表)
-l ：列出目前在 /lib/modules/`uname -r`/kernel 当中的所有模组完整档名；
-f ：强制载入该模组；
-r ：类似 rmmod ，就是移除某个模组啰～


