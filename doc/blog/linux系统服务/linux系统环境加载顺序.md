## linux系统环境加载顺序

- 登陆shell(login shell)：
  
  ​    取得 bash 时需要完整的登陆流程的，就称为 login shell
  
  ​    比如通过ssh方式连接，或者由tty1 ~ tty6 登陆，需要输入用户的账号与密码，此时取得的 bash 就称为login shell

- 非登陆shell(non-login shell)：
  
  ​    取得 bash 接口的方法不需要重复登陆的举动
  
  ​    比如你以 X window 登陆 Linux 后， 再以 X 的图形化接口启动终端机，此时该终端接口无需输入账号与密码，则为non-login shell    
  
  ​    比如你在原本的 bash 环境下再次下达 bash 这个命令，同样的也没有输入账号密码， 那第二个 bash (子程序) 也是 non-login shell 

（可以通过 echo $0 查看）

```
###演示环境
[root@system1 ~]# more /etc/redhat-release 
Red Hat Enterprise Linux Server release 7.0 (Maipo)

###当前从ssh登陆到服务器
[root@system1 ~]# tty
/dev/pts/1

# ### Author : Leshami QQ/Weixin : 645746311

###输入 echo $0， 显示结果为 -bash ，即为登陆shell
[root@system1 ~]# echo $0
-bash
[root@system1 ~]# ps
  PID TTY          TIME CMD
77122 pts/1    00:00:00 bash
77157 pts/1    00:00:00 ps

###下面在X windows打开一个终端，如下，显示为/bin/bash，即非登陆shell
[root@system1 Desktop]# echo $0
/bin/bash

[root@system1 ~]# ps -ef|grep pts|grep bash
root      73245  73241  0 11:49 pts/0    00:00:00 /bin/bash
root      76511  73245  0 16:19 pts/0    00:00:00 bash
root      77122  77118  0 17:02 pts/1    00:00:00 -bash
root      77158  77118  0 17:03 pts/2    00:00:00 -bash
root      77210  73241  0 17:04 pts/3    00:00:00 /bin/bash
root      77283  77279  0 17:06 pts/4    00:00:00 -bash
root      77332  77122  0 17:06 pts/1    00:00:00 grep --color=auto bash 
###在上传的结果中73245，77210为非登陆shell，77122，77158，77283为登陆shell
```

- 交互式shell(interactive shell) 
  
  ​    交互式模式就是在终端上执行，shell等待你的输入，并且立即执行你提交的命令。这种模式被称作交互式是因为shell与用户进行交互。这种模式也是大多数用户非常熟悉的：登录、执行一些命令、退出。当你退出后，shell也终止了。

- 非交互式shell(non-interactive shell) 
  
  ​    shell也可以运行在另外一种模式：非交互式模式，以shell script(非交互)方式执行。在这种模式 下，shell不与你进行交互，而是读取存放在文件中的命令,并且执行它们。当它读到文件的结尾EOF，shell也就终止了。

```
###如下，执行 echo $-，查看其中的“i”选项（表示interactive shell）
[root@system1 ~]# echo $-
himBH

###如下，为非交互shell
[root@system1 ~]# echo 'echo $-' | bash
hB
```

环境变量的调用顺序



上图列出了登陆shell与非登陆shell读取的不同的shell环境配置文件。 

 其中，实线的的方向是主线流程，虚线的方向则是被调用(或读取)的配置文件  

此外，对于登陆shell，读取~/.bash_profile配置文件时，会做出读取顺序判读，如下

    ~/.bash_profile —> ~/.bash_login  —> ~/.profile  

但 bash 的 login shell 配置只会读取上面三个文件的其中一个， 而读取的顺序则是依照上面的顺序。

也就是说，

如果 ~/.bash_profile 存在，那么其他两个文件不论有无存在，都不会被读取。 

如果 ~/.bash_profile 不存在才会去读取 ~/.bash_login，而前两者都不存在才会读取 ~/.profile 的意思。

在shell登出是会读取 ~/.bash_logout

**属于非登录shell：不需要输入密码的登录及远程 SSH 连接——>  ~/.bashrc（用户文件U2）——>/etc/bashrc（全局文件G2）**

​    如果用户的Shell 不是登录时启动的（比如手动敲下 bash 时启动或者其他不需要输入密码的登录及远程 SSH 连接情况）那么这种非登录 Shell 只会加载 ~`/.bashrc`（用户环境变量文件），并会去找 `/etc/bashrc`（全局环境变量文件），因此如果希望在非登录 Shell 下也可读到设置的环境变量等内容，就需要将变量设定写入 ~`/.bashrc` 或者 `/etc/bashrc`，而不是 ~`/.bash_profile`或`/etc/profile`。

**其他**

1、/etc/profile：系统配置文件，用户登录时读取一次
2、/etc/bash.bashrc：（Ubuntu）系统配置文件，用户登录时读取一次，每次打开一个新终端会话时读取一次。
/etc/bashrc： （Centos）系统配置文件，用户登录时读取一次，每次打开一个新终端会话时读取一次。
3、~/.profile（~/.bash_profile、~/.bash_login）：用户配置文件，用户登录时读取一次
4、~/.bashrc：用户配置文件，用户登录时读取一次，每次打开一个新终端会话时读取一次

对于 ~/.bash_profile、~/.bash_login、~/.profile，如果终端绑定的是 bash，则按照我书写的顺序进行读取（如果存在，就不继续读取）

1、系统配置文件作用于全局，而用户配置文件仅针对当前登录的用户
2、先读取系统配置文件，再读取用户配置文件，用户配置文件的变量和表达式等都继承自系统配置文件
