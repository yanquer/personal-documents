## 指令

（以下排名以字母顺序）

### adjtimex

```tex
    linux系统有两个时钟：一个是由主板电池驱动的“Real Time Clock”也叫做RTC或者叫CMOS时钟，硬件时钟。当操作系统关机的时候，用这个来记录时间，但是对于运行的系统是不用这个时间的。另一个时间是 “System clock”也叫内核时钟或者软件时钟，是由软件根据时间中断来进行计数的，内核时钟在系统关机的情况下是不存在的，所以，当操作系统启动的时候，内核时钟是要读取RTC时间来进行时间同步（有些情况下，内核时钟也可以通过ntp服务器来读取时间） 这两个时钟通常会有一些误差，所以长时间可以导致这两个时钟偏离的比较多，最简单的保持两个时间同步的方法是用软件测出他们之间的误差率，然后用软件进行修正。
————————————————
adjtimex
    -p, –print 输出内核时间变量的值
    -t, –tick val 设置内核时钟计数间隔（微秒）
    -f, –frequency newfreq 设置系统时钟偏移量
    -c, –compare[=count] 比较系统时钟和CMOS时钟
    -i, –interval tim 设置时钟比较间隔时间 (sec)
    -l, –log[=file] 将当前时间记录到文件中
    –host timeserver 查询时间服务器
    -u, –utc 将CMOS时钟设置成UTC
------------------
每次重启NTP服务器之后大约要3－5分钟客户端才能与server建立正常的通讯连接
```

### alias

命令别名

如：

```
alias lm='ls -al | more'
```

使用unalias去除

### apt

#### apt-cache

列出软件的安装来源

```sh
apt-cache madison $soft    # 搜索源里面的可用版本
apt-cache policy $sofy    # 比上面那个详细一点
apt-cache showpkg $soft    # 比上一个更详细，还会列出所有相关的


apt-cache show $soft    # 显示指定包的详情 dpkg -s $soft也可以
```

#### apt-get install

模拟安装

```sh
apt-get install -s $soft 
```

### arp

arp 命令用于显示和修改 IP 到 MAC 转换表

> **arp 命令** 是 Address Resolution Protocol，地址解析协议，是通过解析网络层地址来找寻数据链路层地址的一个网络协议包中极其重要的网络传输协议。而该命令可以显示和修改 arp 协议解析表中的缓冲数据。
> 
> 这个核心协议模块实现RFC826中定义的 Address Resolution Protocol [译注：即TCP/IP的第三层到第一层的地址转换协议]，用于在直接相连的网络中换第二层硬件地址和 Ipv4 协议地址之间的转换。 用户除非想对其进行配置，否则一般不会直接操作这个模块。
> 
> 实际上，它提供对核心中其它协议的服务。
> 
> 用户进程可以使用 packet(7) 的 sockets，收到 ARP 包（译注：一译分组）。 还有一种机制是使用 netlink(7) sockets，在用户空间管理 ARP 缓存的机制。我们也可以通过 ioctl (2) 控制任意 PF_INET socket上的 ARP 表
> 
> ARP 模块维护一个硬件地址到协议地址映射的缓存。这个缓存有大小限制，所以不常用的和旧的记录（Entry）将被垃圾收集器清除（garbage-collected），垃圾收集器永远不能删除标为永久的记录。我们可以使用ioctls直接操纵缓冲， 并且其性状可以用下面定义的 sysctl 调节。
> 
> 如果在限定的时间（见下面的sysctl）内，一条现存映射没有肯定反馈时， 则认为相邻层的缓存记录失效。 为了再次向目标发送数据，ARP将首先试着询问本地arp进程 app_solicit 次，获取更新了的 MAC（介质访问控制）地址。 如果失败，并且旧的MAC地址是已知的，则发送 ucast_solicit 次的 unicast probe。如果仍然失败，则将向网络广播一个新的ARP请求,此时要 有待发送数据的队列
> 
> 如果 Linux 接到一个地址请求，而且该地址指向 Linux 转发的地址，并且接收接口打开了代理 arp 时，Linux 将自动添加一条非永久的代理 arp 记录；如果存在拒绝到目标的路由，则不添加代理 arp 记录。

**语法**

```shell
arp（选项）（参数）
```

**选项**

```shell
-a # 主机 ：显示 arp 缓冲区的所有条目；
-H # 地址类型 ：指定 arp 指令使用的地址类型；
-D # 使用指定接口的硬件地址；
-e # 以 Linux 的显示风格显示 arp 缓冲区中的条目；
-f # 文件 ：设置主机的 IP 地址与 MAC 地址的静态映射。
-n # 以数字方式显示 arp 缓冲区中的条目；
-s<主机><MAC地址> # 主机 MAC 地址 ：设置指定的主机的 IP 地址与 MAC 地址的静态映射；
-d<主机> # 主机 ：从 arp 缓冲区中删除指定主机的 arp 条目；
-i<接口> # 接口 ：指定要操作 arp 缓冲区的网络接口；
-v  # 显示详细的 arp 缓冲区条目，包括缓冲区条目的统计信息；
```

```sh
[root@cs6 ~]# arp -n

Address HWtype HWaddress Flags Mask Iface

10.0.0.1 ether 00:50:56:c0:00:08 C eth0

10.0.0.2 ether 00:50:56:f4:fb:52 C eth0
```

命令说明具体如下。

Address：主机地址。

Hwtype：硬件类型。

Hwaddress：硬件地址。

Flags Mask：记录标志，“C”表示arp高速缓存中的条目，“M”表示静态的arp条目。

lface：网络接口。

### ausearch

> 使用ausearch命令可以搜索审计记录，必须以root用户身份执行ausearch命令。
> 
> 安装
> 
> ```sh
> yum install audit
> #要么 
> up2date install audit
> 
> 
> #debian
> apt install auditd
> ```

**语法格式：**ausearch [参数]

**选项含义**

| **选项**                              | **含义**            |
| ----------------------------------- | ----------------- |
| -f<文件名>                             | 基于文件名的搜索          |
| -c<命令行名称>                           | 基于命令行名称的搜索        |
| -ga<所有组群的ID>                        | 基于所有组群GID的搜索      |
| -ha<主机名>                            | 基于远程主机名的搜索        |
| -ui<用户UID>                          | 基于用户UID的搜索        |
| -n<计算机名称>                           | 基于计算机名称的搜索        |
| -p<进程ID>                            | 基于进程ID的搜索         |
| -tm<终端>                             | 基于终端的搜索           |
| -sv<成功值>                            | 基于系统调用或事件成功值的搜索   |
| -k<键字段>                             | 基于键字段的搜索          |
| -m<消息类型>                            | 基于消息类型的搜索         |
| -pp<父进程ID>                          | 基于父进程ID的搜索        |
| -ul<用户登录ID>                         | 基于用户登录ID的搜索       |
| -x<可执行文件名>                          | 基于可执行文件名的搜索       |
| -a<审计事件ID>                          | 基于审计事件ID的搜索       |
| -ue<有效UID>                          | 基于有效UID的搜索        |
| -ge<有效GID>                          | 基于有效GID的搜索        |
| -session<登录会话ID>                    | 基于登录会话ID的搜索       |
| -sc<系统调用的名称>                        | 基于系统调用的名称或对象编号的搜索 |
| -se<SELinux上下文>                     | 基于任何主体或对象的上下文搜索   |
| -o<SELinux对象上下文>                    | 基于对象上下文的搜索        |
| -ts<开始日期><开始日期>,--start<开始日期><开始日期> | 基于开始时间、开始时间的搜索    |
| -ua<所有用户的UID>                       | 基于所有的用户UID的搜索     |
| -te<结束时间><结束时间>                     | 基于结束时间、结束时间的搜索    |
| -su<SELinux上下文>                     | 基于主题的上下文的搜索       |
| -e<退出代码>                            | 基于系统调用退出代码的搜索     |
| -r                                  | 完全未格式化输出          |

**例**

基于用户root搜索审计记录

```sh
[root@localhost ~]# ausearch  -ui 0
```

基于终端tty1搜索审计记录

```sh
[root@localhost ~]# ausearch -tm tty1
```

基于进程号1779搜索审计记录

```sh
[root@localhost ~]# ausearch -p 1779
```

### awk

选项

- -F fs                fs指定分割符

- -v var=value        赋值一个用户变量，将外部变量传递给awk

- -f script            从脚本文件中读取awk命令

- -m[fr] val        对val值设置内在限制，-mf选项限制分配给val的最大块数目；-mr选项限制记录的最大数目。这两个功能时Bell实验室awk拓展的功能，在标准awk不适用。    

- $n        当前记录的第n个字段，$开头都表示字段

**模式**

- /正则表达式/：使用通配符的拓展集
- 关系表达式：使用运算符进行操作，可以是字符串或数字的比较测试
- 模式匹配表达式：用运算符 ~ （匹配）和 !~ （不匹配）
- BEGIB语句块、pattern语句块、END语句块：参见awk的工作原理

#### awk内置变量（预定义变量）

说明：ANPG表示第一个支持变量的工具，[A]=awk、[N]=nawk、[P]=POSIXawk、[G]=gawk

```shell
 **$n**  当前记录的第n个字段，比如n为1表示第一个字段，n为2表示第二个字段。 
 **$0**  这个变量包含执行过程中当前行的文本内容。
[N]  **ARGC**  命令行参数的数目。
[G]  **ARGIND**  命令行中当前文件的位置（从0开始算）。
[N]  **ARGV**  包含命令行参数的数组。
[G]  **CONVFMT**  数字转换格式（默认值为%.6g）。
[P]  **ENVIRON**  环境变量关联数组。
[N]  **ERRNO**  最后一个系统错误的描述。
[G]  **FIELDWIDTHS**  字段宽度列表（用空格键分隔）。
[A]  **FILENAME**  当前输入文件的名。
[P]  **FNR**  同NR，但相对于当前文件。
[A]  **FS**  字段分隔符（默认是任何空格）。
[G]  **IGNORECASE**  如果为真，则进行忽略大小写的匹配。
[A]  **NF**  表示字段数，在执行过程中对应于当前的字段数。
[A]  **NR**  表示记录数，在执行过程中对应于当前的行号。
[A]  **OFMT**  数字的输出格式（默认值是%.6g）。
[A]  **OFS**  输出字段分隔符（默认值是一个空格）。
[A]  **ORS**  输出记录分隔符（默认值是一个换行符）。
[A]  **RS**  记录分隔符（默认是一个换行符）。
[N]  **RSTART**  由match函数所匹配的字符串的第一个位置。
[N]  **RLENGTH**  由match函数所匹配的字符串的长度。
[N]  **SUBSEP**  数组下标分隔符（默认值是34）。
```

BEGIN末尾的非0数字表示输出

这里非0数字可以理解为true

```sh
echo -e "111\n222" | awk -v a=3 -v val=god 'BEGIN{FS=OFS=","}{$a=val}1'

111,,god
222,,god
```

```shell
#awk中$NF是什么意思？
#pwd
/usr/local/etc
~# echo $PWD | awk -F/ '{print $NF}'
etc
#NF代表：浏览记录的域的个数
#$NF代表  ：最后一个Field(列)
```

- NF    每一行 $0 拥有的字段总数
- NR    目前awk所处理的第几行的数据
- FS    默认的分隔字符

NF 字段个数，（读取的列数）
NR 记录数（行号），从1开始，新的文件延续上面的计数，新文件不从1开始
FNR 读取文件的记录数（行号），从1开始，新的文件重新从1开始计数
FS 输入字段分隔符，默认是空格
OFS 输出字段分隔符 默认也是空格
RS 输入行分隔符，默认为换行符
ORS 输出行分隔符，默认为换行符
————————————————

原文链接：https://blog.csdn.net/qq_41673534/article/details/80252016

[linux：awk之RS、ORS与FS、OFS](https://www.cnblogs.com/fhefh/archive/2011/11/16/2251656.html)

RS：Record Separator，记录分隔符     ----原字符以分隔符分隔开
ORS：Output Record Separate，输出当前记录分隔符                ----原字符以分隔符拼接
FS：Field Separator，字段分隔符
OFS：Out of Field Separator，输出字段分隔符

PS：RS、ORS、FS、OFS的英文解释绝不是这样的，这里只是解释清楚。建议去阅读awk的英文读物，其中解释了缩写的含义。

​    什么是field（字段），什么是record（记录行）？

> 示例：
> 
> 1.txt
> 
> 1. i am a student.
> 2. i like to swim
> 3. hello moto
> 
> 1代表第一个记录行，2代表第二个记录行，3代表第三个记录行。通过观察我们可以知道总共有3个记录行（record）。
> 
> 看看第一行：“i am a student”，这一行的每个单词都是一个字段（field）。“i”是一个字段，“am”是一个字段，“a”是一个字段，“student”是一个字段，该行总共有4个字段。

​    RS与ORS

​    RS：记录行分隔符

> 示例：
> 
> 1.txt
> 
> 1. a\n
> 2. b\n
> 3. c\n
> 4. d\n
> 5. e\n
> 
> 该文本总共有5行，每一行都有一个换行符“\n”。所以每行记录都是以“\n”为一个（换行的）标志。
> 
> 可以用一下方法来理解：
> 
> 找到某某标志，让每个某某后的内容重新变成一行
> 
> 示例
> 
> 1.txt
> 
> a|b|c
> 
> 代码：awk 'BEGIN{ RS="|"; } { print $0 }'
> 
> a
> 
> b
> 
> b

​    ORS：可以看成RS的逆向过程

> 示例
> 
> 1.txt
> 
> a
> 
> b
> 
> c
> 
> 可以这样理解：
> 
> 观察每一行的“换行符号”，然后将“换行符号”替换成你想要的符号。
> 
> awk 'BEGIN{ ORS="----" }{ print $0 }' 1.txt
> 
> a----b----c----

​    FS：字段分隔符

> FS默认值为“ （空格）”,如“hello moto”.
> 
> 在“hello moto”中有一个空格，空格就是hello与moto的分隔符（separator），而hello与moto就为字段（files）。awk以空格来区分。
> 
> 在看看“i----love----you”,如果我们用命令“awk “{ print $1 }””会看到结果为：
> 
> i----love----you
> 
> 如果想打印出三个字母，通过观察可发现“----”为分隔符。
> 
> awk 'BEGIN{ FS="----";}{ print $1,$2,$3 }' filename
> 
> i love you

​    OFS：输出的字段分隔符。

> 这么解释吧，如上例中“i----love----you”，“----”为分隔符(FS)，如果我们想改为用其他符号显示可以这样：
> 
> awk 'BEGIN{ FS="----";OFS="*****" }{ print $1,$2,$3 }' filename
> 
> i*****love*****you
> 
> 其实OFS还有一个例子
> echo "abc" | awk '{ OFS="." } { NF=NF; print NF,$0}'
> 结果
> 1.abc

> PS：RS与ORS可以说成是一个互逆的过程（↔）也可以看成一个替换的过程，但是看成互逆的过程比较好理解；FS与OFS就是一个替换的过程。

总结 RS,ORS,FS,OFS的区别和联系。

平常用的 print $0 等价于 printf $0 ORS

**一，RS与ORS**

1，RS是记录分隔符，默认的分隔符是\n，具体用法看下

```cpp
[root@krlcgcms01 mytest]# cat test1     //测试文件
 111 222
 333 444
 555 666
```

2，RS默认分割符\n

```dart
[root@krlcgcms01 mytest]# awk '{print $0}' test1  //awk 'BEGIN{RS="\n"}{print $0}' test1 这二个是一样的
111 222
333 444
555 666
```

其实你可以把**上面test1文件里的内容理解为，111 222\n333 444\n555 6666，利用\n进行分割**。看下一个例子

3，自定义RS分割符

```ruby
[zhangy@localhost test]$ echo "111 222|333 444|555 666"|awk 'BEGIN{RS="|"}{print $0,RT}'
 111 222 |
 333 444 |
 555 666
```

结合上面一个例子，就很容易理解RS的用法了。

4，RS也可能是正则表达式

```bash
[zhangy@localhost test]$ echo "111 222a333 444b555 666"|awk 'BEGIN{RS="[a-z]+"}{print $1,RS,RT}'
 111 [a-z]+ a
 333 [a-z]+ b
 555 [a-z]+
```

从例3和例4，我们可以发现一点，**当RT是利用RS匹配出来的内容。如果RS是某个固定的值时，RT就是RS的内容**。

5，RS为空时

```dart
[zhangy@localhost test]$ cat -n test2
 1  111 222
 2
 3  333 444
 4  333 444
 5
 6
 7  555 666
[zhangy@localhost test]$ awk 'BEGIN{RS=""}{print $0}' test2
111 222
333 444
333 444
555 666
[zhangy@localhost test]$ awk 'BEGIN{RS="";}{print "<",$0,">"}' test2  //这个例子看着比较明显
< 111 222 >
< 333 444     //这一行和下面一行，是一行
333 444 >
< 555 666 >
```

从这个例子，**可以看出当RS为空时，awk会自动以多行来做为分割符**。

6，ORS记录输出分符符，默认值是\n

**把ORS理解成RS反过程，这样更容易记忆和理解**，看下面的例子。

```dart
[zhangy@localhost test]$ awk 'BEGIN{ORS="\n"}{print $0}' test1  //awk '{print $0}' test1二者是一样的
111 222
333 444
555 666
[zhangy@localhost test]$ awk 'BEGIN{ORS="|"}{print $0}' test1
111 222|333 444|555 666|
```

**二，FS与OFS**

1，FS指定列分割符

```bash
[zhangy@localhost test]$ echo "111|222|333"|awk '{print $1}'
 111|222|333
[zhangy@localhost test]$ echo "111|222|333"|awk 'BEGIN{FS="|"}{print $1}'
 111
```

2，FS也可以用正则

```ruby
[zhangy@localhost test]$ echo "111||222|333"|awk 'BEGIN{FS="[|]+"}{print $1}'
111
```

3，FS为空的时候

```ruby
[zhangy@localhost test]$ echo "111|222|333"|awk 'BEGIN{FS=""}{NF++;print $0}'
1 1 1 | 2 2 2 | 3 3 3
```

**当FS为空的时候，awk会把一行中的每个字符，当成一列来处理**。

4，RS被设定成非\n时，\n会成FS分割符中的一个

```dart
[zhangy@localhost test]$ cat test1
 111 222
 333 444
 555 666
[zhangy@localhost test]$ awk 'BEGIN{RS="444";}{print $2,$3}' test1
 222 333
 666
```

**222和333之间是有一个\n的，当RS设定成444后，222和333被认定成同一行的二列了，其实按常规思想是二行的一列才对**。

5，OFS列输出分隔符

```dart
[zhangy@localhost test]$ awk 'BEGIN{OFS="|";}{print $1,$2}' test1
 111|222
 333|444
 555|666
[zhangy@localhost test]$ awk 'BEGIN{OFS="|";}{print $1 OFS $2}' test1
 111|222
 333|444
 555|666
```

**test1只有二列，如果100列，都写出来太麻烦了吧。**

```ruby
[zhangy@localhost test]$ awk 'BEGIN{OFS="|";}{print $0}' test1
 111 222
 333 444
 555 666
[zhangy@localhost test]$ awk 'BEGIN{OFS="|";}{NF=NF;print $0}' test1
 111|222
 333|444
 555|666
```

为什么第二种方法中的OFS生效呢？个人觉得，**awk觉查到列有所变化时，就会让OFS生效**，没变化直接输出了。

### basename

> 打印目录或者文件的基本名称。basename和dirname命令通常用于shell脚本中的命令替换来指定和指定的输入文件名称有所差异的输出文件名称。

要显示一个shell变量的基本名称，请输入：

```
basename $WORKFILE
```

### bash

也算指令吧

先写这

- -n    仅语法检查
- -v    执行前，先将内容输出（详细输出执行过程）
- -x    将使用的脚本内容显示到屏幕

### blkid

列出装置的uuid

### cd

```bash
# 返回最近一次的目录
cd -
```

### chage

用来修改帐号和密码的有效期限。

**语法**

```shell
chage [选项] 用户名
```

**选项**

```shell
-m：密码可更改的最小天数。为零时代表任何时候都可以更改密码。
-M：密码保持有效的最大天数。
-w：用户密码到期前，提前收到警告信息的天数。
-E：帐号到期的日期。过了这天，此帐号将不可用。
-d：上一次更改的日期。
-i：停滞时期。如果一个密码已过期这些天，那么此帐号将不可用。
-l：例出当前的设置。由非特权用户来确定他们的密码或帐号何时过期。
```

我的服务器root帐户密码策略信息如下：

```shell
[root@linuxde ~]# chage -l root
最近一次密码修改时间                    ： 3月 12, 2013
密码过期时间                            ：从不
密码失效时间                           ：从不
帐户过期时间                           ：从不
两次改变密码之间相距的最小天数          ：0
两次改变密码之间相距的最大天数          ：99999
在密码过期之前警告的天数                ：7
```

我可以通过如下命令修改我的密码过期时间：

```shell
[root@linuxde ~]# chage -M 60 root
[root@linuxde ~]# chage -l root
最近一次密码修改时间                          ： 3月 12, 2013
密码过期时间                                       ： 5月 11, 2013
密码失效时间                                       ：从不
帐户过期时间                                       ：从不
两次改变密码之间相距的最小天数          ：0
两次改变密码之间相距的最大天数          ：60
在密码过期之前警告的天数                    ：9
```

然后通过如下命令设置密码失效时间：

```shell
[root@linuxde ~]# chage -I 5 root
[root@linuxde ~]# chage -l root
最近一次密码修改时间                          ： 3月 12, 2013
密码过期时间                                  ： 5月 11, 2013
密码失效时间                                  ： 5月 16, 2013
帐户过期时间                                  ：从不
两次改变密码之间相距的最小天数          ：0
两次改变密码之间相距的最大天数          ：60
在密码过期之前警告的天数                 ：9
```

从上述命令可以看到，在密码过期后5天，密码自动失效，这个用户将无法登陆系统了。

### chattr

Linux chattr命令用于改变文件属性。

这项指令可改变存放在ext2文件系统上的文件或目录属性，这些属性共有以下8种模式：

1. a：让文件或目录仅供附加用途。
2. b：不更新文件或目录的最后存取时间。
3. c：将文件或目录压缩后存放。
4. d：将文件或目录排除在倾倒操作之外。
5. i：不得任意更动文件或目录。
6. s：保密性删除文件或目录。
7. S：即时更新文件或目录。
8. u：预防意外删除。

**语法**

```
chattr [-RV][-v<版本编号>][+/-/=<属性>][文件或目录...]
```

**参数**

　　-R 递归处理，将指定目录下的所有文件及子目录一并处理。

　　-v<版本编号> 设置文件或目录版本。

　　-V 显示指令执行过程。

　　+<属性> 开启文件或目录的该项属性。

　　-<属性> 关闭文件或目录的该项属性。

　　=<属性> 指定文件或目录的该项属性。

**实例**

用chattr命令防止系统中某个关键文件被修改：

```
chattr +i /etc/resolv.conf
lsattr /etc/resolv.conf
```

会显示如下属性

```
----i-------- /etc/resolv.conf
```

让某个文件只能往里面追加数据，但不能删除，适用于各种日志文件：

```
chattr +a /var/log/messages
```

### chown

```tex
#变更文件或目录的拥有者或所属群组
#用户：组：指定所有者和所属工作组。当省略“：组”，仅改变文件所有者；
#文件：指定要改变所有者和工作组的文件列表。支持多个文件和目标，支持shell通配符。
chown -R user:group  file

-f或--quite或——silent：不显示错误信息；
```

### chmod

更改文件/目录权限

##### 对于linux下文件权限的s位和t位的理解

作用：创建s和t权限，是为了让一般用户在执行某些程序时，能够暂时拥有改程序拥有者的权限（体现在x位）。

- SUID是Set User  Id
  
  - 仅对二进制文件（binary）有效（也就是说对于shell脚本或者目录无效）
  - 执行者需要有x权限
  - 仅在执行该权限的过程中有效
  - 执行者将具有该权限拥有者的权限

- SGID是Set Group Id
  
  - 对二进制文件有效（与suid不同的是，可以作用于目录）
  - 执行者需要有x权限
  - 执行者在执行过程中会获得该程序群组的支持

ls -l查看文件格式一共有10位

```sh
9 8 7 6 5 4 3 2 1 0
- r w x r - x r - x

# 这10位中8-6位是文件所有者权限
# 5-3位是同组用户权限
# 2-0位其他用户权限
# 形式为rwx
```

r表示可读，可以读出文件的内容

w表示可写，可以修改文件的内容

x表示可执行，可运行文件

第9位表示文件类型：

```
 p表示命名管道文件

 d表示目录文件

 l表示符号链接文件

 -表示普通文件

 s表示socket文件

 c表示字符设备文件

 b表示块设备文件
```

其实在unix下，文件权限用12个二进制位表示

```sh
11 10 9 8 7 6 5 4 3 2 1 0
 S  G T r w x r w x r w x

# 第11位为SUID位
# 第10位为SGID位
# 第9位为sticky位
```

### chpasswd

读取未加密的密码，然后将加密后的密码写入 /etc/shadow

```sh
echo 'qwe123' | chpasswd
```

### col

- -x    将tab替换为空格

### cmp

Linux cmp命令用于比较两个文件是否有差异。

当相互比较的两个文件完全一样时，则该指令不会显示任何信息。若发现有所差异，预设会标示出第一个不同之处的字符和列数编号。若不指定任何文件名称或是所给予的文件名为"-"，则cmp指令会从标准输入设备读取数据。

**语法**

```
cmp [-clsv][-i <字符数目>][--help][第一个文件][第二个文件]
```

**参数**：

- -c或--print-chars 　除了标明差异处的十进制字码之外，一并显示该字符所对应字符。
- -i<字符数目>或--ignore-initial=<字符数目> 　指定一个数目。
- -l或--verbose 　标示出所有不一样的地方。
- -s或--quiet或--silent 　不显示错误信息。
- -v或--version 　显示版本信息。
- --help 　在线帮助。

**实例**

要确定两个文件是否相同，请输入：

```
cmp prog.o.bak prog.o 
```

这比较 prog.o.bak 和 prog.o。如果文件相同，则不显示消息。如果文件不同，则显示第一个不同的位置；例如：

```
prog.o.bak prog.o differ: char 4, line 1 
```

如果显示消息 cmp: EOF on prog.o.bak，则 prog.o 的第一部分与 prog.o.bak 相同，但在 prog.o 中还有其他数据。

### command

command -v 可以判断一个命令是否支持，如果一个脚本需要，或者还要家if判断

```sh
if command -v python ;then
    echo yes
fi
```

### curl

curl 是常用的命令行工具，用来请求 Web 服务器。它的名字就是客户端（client）的 URL 工具的意思。

它的功能非常强大，命令行参数多达几十种。如果熟练的话，完全可以取代 Postman 这一类的图形界面工具。

不带有任何参数时，curl 就是发出 GET 请求。

> ```bash
> $ curl https://www.example.com
> ```

- -A
  
  `-A`参数指定客户端的用户代理标头，即`User-Agent`。curl 的默认用户代理字符串是`curl/[version]`。
  
  > ```bash
  > $ curl -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' https://google.com
  > ```
  
  上面命令将`User-Agent`改成 Chrome 浏览器。
  
  > ```bash
  > $ curl -A '' https://google.com
  > ```
  
  上面命令会移除`User-Agent`标头。
  
  也可以通过`-H`参数直接指定标头，更改`User-Agent`。
  
  > ```bash
  > $ curl -H 'User-Agent: php/1.0' https://google.com
  > ```

- -b
  
  `-b`参数用来向服务器发送 Cookie。
  
  > ```bash
  > $ curl -b 'foo=bar' https://google.com
  > ```
  
  上面命令会生成一个标头`Cookie: foo=bar`，向服务器发送一个名为`foo`、值为`bar`的 Cookie。
  
  > ```bash
  > $ curl -b 'foo1=bar;foo2=bar2' https://google.com
  > ```
  
  上面命令发送两个 Cookie。
  
  > ```bash
  > $ curl -b cookies.txt https://www.google.com
  > ```
  
  上面命令读取本地文件`cookies.txt`，里面是服务器设置的 Cookie（参见`-c`参数），将其发送到服务器。

- -c
  
  `-c`参数将服务器设置的 Cookie 写入一个文件。
  
  > ```bash
  > $ curl -c cookies.txt https://www.google.com
  > ```
  
  上面命令将服务器的 HTTP 回应所设置 Cookie 写入文本文件`cookies.txt`。

- -d
  
  `-d`参数用于发送 POST 请求的数据体。
  
  > ```bash
  > $ curl -d'login=emma＆password=123'-X POST https://google.com/login
  > # 或者
  > $ curl -d 'login=emma' -d 'password=123' -X POST  https://google.com/login
  > ```
  
  使用`-d`参数以后，HTTP 请求会自动加上标头`Content-Type : application/x-www-form-urlencoded`。并且会自动将请求转为 POST 方法，因此可以省略`-X POST`。
  
  `-d`参数可以读取本地文本文件的数据，向服务器发送。
  
  > ```bash
  > $ curl -d '@data.txt' https://google.com/login
  > ```
  
  上面命令读取`data.txt`文件的内容，作为数据体向服务器发送。

- --data-urlencode
  
  `--data-urlencode`参数等同于`-d`，发送 POST 请求的数据体，区别在于会自动将发送的数据进行 URL 编码。
  
  > ```bash
  > $ curl --data-urlencode 'comment=hello world' https://google.com/login
  > ```
  
  上面代码中，发送的数据`hello world`之间有一个空格，需要进行 URL 编码。

- -e
  
  `-e`参数用来设置 HTTP 的标头`Referer`，表示请求的来源。
  
  > ```bash
  > curl -e 'https://google.com?q=example' https://www.example.com
  > ```
  
  上面命令将`Referer`标头设为`https://google.com?q=example`。
  
  `-H`参数可以通过直接添加标头`Referer`，达到同样效果。
  
  > ```bash
  > curl -H 'Referer: https://google.com?q=example' https://www.example.com
  > ```

- -F
  
  `-F`参数用来向服务器上传二进制文件。
  
  > ```bash
  > $ curl -F 'file=@photo.png' https://google.com/profile
  > ```
  
  上面命令会给 HTTP 请求加上标头`Content-Type: multipart/form-data`，然后将文件`photo.png`作为`file`字段上传。
  
  `-F`参数可以指定 MIME 类型。
  
  > ```bash
  > $ curl -F 'file=@photo.png;type=image/png' https://google.com/profile
  > ```
  
  上面命令指定 MIME 类型为`image/png`，否则 curl 会把 MIME 类型设为`application/octet-stream`。
  
  `-F`参数也可以指定文件名。
  
  > ```bash
  > $ curl -F 'file=@photo.png;filename=me.png' https://google.com/profile
  > ```
  
  上面命令中，原始文件名为`photo.png`，但是服务器接收到的文件名为`me.png`。

- -G
  
  `-G`参数用来构造 URL 的查询字符串。
  
  > ```bash
  > $ curl -G -d 'q=kitties' -d 'count=20' https://google.com/search
  > ```
  
  上面命令会发出一个 GET 请求，实际请求的 URL 为`https://google.com/search?q=kitties&count=20`。如果省略`--G`，会发出一个 POST 请求。
  
  如果数据需要 URL 编码，可以结合`--data--urlencode`参数。
  
  > ```bash
  > $ curl -G --data-urlencode 'comment=hello world' https://www.example.com
  > ```

- -H
  
  `-H`参数添加 HTTP 请求的标头。
  
  > ```bash
  > $ curl -H 'Accept-Language: en-US' https://google.com
  > ```
  
  上面命令添加 HTTP 标头`Accept-Language: en-US`。
  
  > ```bash
  > $ curl -H 'Accept-Language: en-US' -H 'Secret-Message: xyzzy' https://google.com
  > ```
  
  上面命令添加两个 HTTP 标头。
  
  > ```bash
  > $ curl -d '{"login": "emma", "pass": "123"}' -H 'Content-Type: application/json' https://google.com/login
  > ```
  
  上面命令添加 HTTP 请求的标头是`Content-Type: application/json`，然后用`-d`参数发送 JSON 数据。

- -i
  
  `-i`参数打印出服务器回应的 HTTP 标头。
  
  > ```bash
  > $ curl -i https://www.example.com
  > ```
  
  上面命令收到服务器回应后，先输出服务器回应的标头，然后空一行，再输出网页的源码。

- -I
  
  `-I`参数向服务器发出 HEAD 请求，然会将服务器返回的 HTTP 标头打印出来。
  
  > ```bash
  > $ curl -I https://www.example.com
  > ```
  
  上面命令输出服务器对 HEAD 请求的回应。
  
  `--head`参数等同于`-I`。
  
  > ```bash
  > $ curl --head https://www.example.com
  > ```

- -k
  
  `-k`参数指定跳过 SSL 检测。
  
  > ```bash
  > $ curl -k https://www.example.com
  > ```
  
  上面命令不会检查服务器的 SSL 证书是否正确。

- -L
  
  `-L`参数会让 HTTP 请求跟随服务器的重定向。curl 默认不跟随重定向。
  
  > ```bash
  > $ curl -L -d 'tweet=hi' https://api.twitter.com/tweet
  > ```

- --limit-rate
  
  `--limit-rate`用来限制 HTTP 请求和回应的带宽，模拟慢网速的环境。
  
  > ```bash
  > $ curl --limit-rate 200k https://google.com
  > ```
  
  上面命令将带宽限制在每秒 200K 字节。

- -o
  
  `-o`参数将服务器的回应保存成文件，等同于`wget`命令。
  
  > ```bash
  > $ curl -o example.html https://www.example.com
  > ```
  
  上面命令将`www.example.com`保存成`example.html`。

- -O
  
  `-O`参数将服务器回应保存成文件，并将 URL 的最后部分当作文件名。
  
  > ```bash
  > $ curl -O https://www.example.com/foo/bar.html
  > ```
  
  上面命令将服务器回应保存成文件，文件名为`bar.html`。

- -s
  
  `-s`参数将不输出错误和进度信息。
  
  > ```bash
  > $ curl -s https://www.example.com
  > ```
  
  上面命令一旦发生错误，不会显示错误信息。不发生错误的话，会正常显示运行结果。
  
  如果想让 curl 不产生任何输出，可以使用下面的命令。
  
  > ```bash
  > $ curl -s -o /dev/null https://google.com
  > ```

- -S
  
  `-S`参数指定只输出错误信息，通常与`-s`一起使用。
  
  > ```bash
  > $ curl -s -o /dev/null https://google.com
  > ```
  
  上面命令没有任何输出，除非发生错误。

- -u
  
  `-u`参数用来设置服务器认证的用户名和密码。
  
  > ```bash
  > $ curl -u 'bob:12345' https://google.com/login
  > ```
  
  上面命令设置用户名为`bob`，密码为`12345`，然后将其转为 HTTP 标头`Authorization: Basic Ym9iOjEyMzQ1`。
  
  curl 能够识别 URL 里面的用户名和密码。
  
  > ```bash
  > $ curl https://bob:12345@google.com/login
  > ```
  
  上面命令能够识别 URL 里面的用户名和密码，将其转为上个例子里面的 HTTP 标头。
  
  > ```bash
  > $ curl -u 'bob' https://google.com/login
  > ```
  
  上面命令只设置了用户名，执行后，curl 会提示用户输入密码。

- -v
  
  `-v`参数输出通信的整个过程，用于调试。
  
  > ```bash
  > $ curl -v https://www.example.com
  > ```
  
  `--trace`参数也可以用于调试，还会输出原始的二进制数据。
  
  > ```bash
  > $ curl --trace - https://www.example.com
  > ```

- -x
  
  `-x`参数指定 HTTP 请求的代理。
  
  > ```bash
  > $ curl -x socks5://james:cats@myproxy.com:8080 https://www.example.com
  > ```
  
  上面命令指定 HTTP 请求通过`myproxy.com:8080`的 socks5 代理发出。
  
  如果没有指定代理协议，默认为 HTTP。
  
  > ```bash
  > $ curl -x james:cats@myproxy.com:8080 https://www.example.com
  > ```
  
  上面命令中，请求的代理使用 HTTP 协议。

- -X
  
  `-X`参数指定 HTTP 请求的方法。
  
  > ```bash
  > $ curl -X POST https://www.example.com
  > ```
  
  上面命令对`https://www.example.com`发出 POST 请求。

**CURL状态码列表**

| 状态码 | 状态原因        | 解释                                                                     |
| --- | ----------- | ---------------------------------------------------------------------- |
| 0   | 正常访问        |                                                                        |
| 1   | 错误的协议       | 未支持的协议。此版cURL 不支持这一协议。                                                 |
| 2   | 初始化代码失败     | 初始化失败。                                                                 |
| 3   | URL格式不正确    | URL 格式错误。语法不正确。                                                        |
| 4   | 请求协议错误      |                                                                        |
| 5   | 无法解析代理      | 无法解析代理。无法解析给定代理主机。                                                     |
| 6   | 无法解析主机地址    | 无法解析主机。无法解析给定的远程主机。                                                    |
| 7   | 无法连接到主机     | 无法连接到主机。                                                               |
| 8   | 远程服务器不可用    | FTP 非正常的服务器应答。cURL 无法解析服务器发送的数据。                                       |
| 9   | 访问资源错误      | FTP 访问被拒绝。服务器拒绝登入或无法获取您想要的特定资源或目录。最有可 能的是您试图进入一个在此服务器上不存在的目录。          |
| 11  | FTP密码错误     | FTP 非正常的PASS 回复。cURL 无法解析发送到PASS 请求的应答。                                |
| 13  | 结果错误        | FTP 非正常的的PASV 应答，cURL 无法解析发送到PASV 请求的应答。                               |
| 14  | FTP回应PASV命令 | FTP 非正常的227格式。cURL 无法解析服务器发送的227行。                                     |
| 15  | 内部故障        | FTP 无法连接到主机。无法解析在227行中获取的主机IP。                                         |
| 17  | 设置传输模式为二进制  | FTP 无法设定为二进制传输。无法改变传输方式到二进制。                                           |
| 18  | 文件传输短或大于预期  | 部分文件。只有部分文件被传输。                                                        |
| 19  | RETR命令传输完成  | FTP 不能下载/访问给定的文件， RETR (或类似)命令失败。                                      |
| 21  | 命令成功完成      | FTP quote 错误。quote 命令从服务器返回错误。                                         |
| 22  | 返回正常        | HTTP 找不到网页。找不到所请求的URL 或返回另一个HTTP 400或以上错误。 此返回代码只出现在使用了-f/--fail 选项以后。 |
| 23  | 数据写入失败      | 写入错误。cURL 无法向本地文件系统或类似目的写入数据。                                          |
| 25  | 无法启动上传      | FTP 无法STOR 文件。服务器拒绝了用于FTP 上传的STOR 操作。                                  |
| 26  | 回调错误        | 读错误。各类读取问题。                                                            |
| 27  | 内存分配请求失败    | 内存不足。内存分配请求失败。                                                         |
| 28  | 访问超时        | 操作超时。到达指定的超时期限条件。                                                      |
| 30  | FTP端口错误     | FTP PORT 失败。PORT 命令失败。并非所有的FTP 服务器支持PORT 命令，请 尝试使用被动(PASV)传输代替！        |
| 31  | FTP错误       | FTP 无法使用REST 命令。REST 命令失败。此命令用来恢复的FTP 传输。                              |
| 33  | 不支持请求       | HTTP range 错误。range "命令"不起作用。                                          |
| 34  | 内部发生错误      | HTTP POST 错误。内部POST 请求产生错误。                                            |
| 35  | SSL/TLS握手失败 | SSL 连接错误。SSL 握手失败。                                                     |
| 36  | 下载无法恢复      | FTP 续传损坏。不能继续早些时候被中止的下载。                                               |
| 37  | 文件权限错误      | 文件无法读取。无法打开文件。权限问题？                                                    |
| 38  | LDAP可没有约束力  | LDAP 无法绑定。LDAP 绑定(bind)操作失败。                                           |
| 39  | LDAP搜索失败    | LDAP 搜索失败。                                                             |
| 41  | 函数没有找到      | 功能无法找到。无法找到必要的LDAP 功能。                                                 |
| 42  | 中止的回调       | 由回调终止。应用程序告知cURL 终止运作。                                                 |
| 43  | 内部错误        | 内部错误。由一个不正确参数调用了功能。                                                    |
| 45  | 接口错误        | 接口错误。指定的外发接口无法使用。                                                      |
| 47  | 过多的重定向      | 过多的重定向。cURL 达到了跟随重定向设定的最大限额跟                                           |
| 48  | 无法识别选项      | 指定了未知TELNET 选项。                                                        |
| 49  | TELNET格式错误  | 不合式的telnet 选项。                                                         |
| 51  | 远程服务器的SSL证书 | peer 的SSL 证书或SSH 的MD5指纹没有确定。                                           |
| 52  | 服务器无返回内容    | 服务器无任何应答，该情况在此处被认为是一个错误。                                               |
| 53  | 加密引擎未找到     | 找不到SSL 加密引擎。                                                           |
| 54  | 设定默认SSL加密失败 | 无法将SSL 加密引擎设置为默认。                                                      |
| 55  | 无法发送网络数据    | 发送网络数据失败。                                                              |
| 56  | 衰竭接收网络数据    | 在接收网络数据时失败。                                                            |
| 57  |             |                                                                        |
| 58  | 本地客户端证书     | 本地证书有问题。                                                               |
| 59  | 无法使用密码      | 无法使用指定的SSL 密码。                                                         |
| 60  | 凭证无法验证      | peer 证书无法被已知的CA 证书验证。                                                  |
| 61  | 无法识别的传输编码   | 无法辨识的传输编码。                                                             |
| 62  | 无效的LDAP URL | 无效的LDAP URL。                                                           |
| 63  | 文件超过最大大小    | 超过最大文件尺寸。                                                              |
| 64  | FTP失败       | 要求的FTP 的SSL 水平失败。                                                      |
| 65  | 倒带操作失败      | 发送此数据需要的回卷(rewind)失败。                                                  |
| 66  | SSL引擎失败     | 初始化SSL 引擎失败。                                                           |
| 67  | 服务器拒绝登录     | 用户名、密码或类似的信息未被接受，cURL 登录失败。                                            |
| 68  | 未找到文件       | 在TFTP 服务器上找不到文件。                                                       |
| 69  | 无权限         | TFTP 服务器权限有问题。                                                         |
| 70  | 超出服务器磁盘空间   | TFTP 服务器磁盘空间不足。                                                        |
| 71  | 非法TFTP操作    | 非法的TFTP 操作。                                                            |
| 72  | 未知TFTP传输的ID | 未知TFTP 传输编号(ID)。                                                       |
| 73  | 文件已经存在      | 文件已存在(TFTP) 。                                                          |
| 74  | 错误TFTP服务器   | 无此用户(TFTP) 。                                                           |
| 75  | 字符转换失败      | 字符转换失败。                                                                |
| 76  | 必须记录回调      | 需要字符转换功能。                                                              |
| 77  | CA证书权限      | 读SSL 证书出现问题(路径？访问权限？ ) 。                                               |
| 78  | URL中引用资源不存在 | URL 中引用的资源不存在。                                                         |
| 79  | 错误发生在SSH会话  | SSH 会话期间发生一个未知错误。                                                      |
| 80  | 无法关闭SSL连接   | 未能关闭SSL 连接。                                                            |
| 81  | 服务未准备       |                                                                        |
| 82  | 无法载入CRL文件   | 无法加载CRL 文件，丢失或格式不正确(在7.19.0版中增加) 。                                     |
| 83  | 发行人检查失败     | 签发检查失败(在7.19.0版中增加) 。                                                  |

### cut

```
显示行中的指定部分，删除文件中指定字段。
cut（选项）（参数）
    选项
    -b：仅显示行中指定直接范围的内容；
    -c：仅显示行中指定范围的字符；
    -d：指定字段的分隔符，默认的字段分隔符为“TAB”；
    -f：显示指定字段（指定列）的内容；
    -n：与“-b”选项连用，不分割多字节字符；
    --complement：补足被选择的字节、字符或字段；
    --out-delimiter= 字段分隔符：指定输出内容是的字段分割符；
```

### dd

```tex
dd
复制文件并对原文件的内容进行转换和格式化处理

    bs=<字节数>：将ibs（输入）与obs（输出）设成指定的字节数；
    cbs=<字节数>：转换时，每次只转换指定的字节数；
    conv=<关键字>：指定文件转换的方式；
    count=<区块数>：仅读取指定的区块数；
    ibs=<字节数>：每次读取的字节数；
    obs=<字节数>：每次输出的字节数；
    if=<文件>；代表输入文件
    of=<文件>：输出到文件；
    seek=<区块数>：一开始输出时，跳过指定的区块数；
    skip=<区块数>：一开始读取时，跳过指定的区块数；
    --help：帮助；
    --version：显示版本信息。
```

```shell
#例如：
#生成10g的大文件：
dd if=/dev/zero of=test bs=1M count=0 seek=10000    #不占空间
dd if=/dev/zero of=test bs=10G count=1
```

### df

> df，disk free，通过文件系统来快速获取空间大小的信息，当我们删除一个文件的时候，这个文件不是马上就在文件系统当中消失了，而是暂时消失了，当所有程序都不用时，才会根据OS的规则释放掉已经删除的文件， df记录的是通过文件系统获取到的文件的大小，他比du强的地方就是能够看到已经删除的文件，而且计算大小的时候，把这一部分的空间也加上了，更精确了。(当文件系统也确定删除了该文件后，这时候du与df就一致了。)

### diff

文件对比

### du

> du，disk usage,是通过搜索文件来计算每个文件的大小然后累加，du能看到的文件只是一些当前存在的，没有被删除的。他计算的大小就是当前他认为存在的所有文件大小的累加和。

```sh
-s            # 指定文件系统中所有的目录、符号链接和文件使用的块数累加得到该文件系统使用的总块数
```

**与df区别**

```sh
[root@www ~]# du -sh /home
4.7G    /home
[root@www ~]# df -h /home
Filesystem            Size  Used Avail Use% Mounted on
/dev/sda5              15G  4.9G  8.9G  36% /home
[root@www ~]#
```

> df 命令通过查看文件系统磁盘块分配图得出总块数与剩余块数。文件系统分配其中的一些磁盘块用来记录它自身的一些数据，如i节点，磁盘分布图，间接块，超级块等。这些数据对大多数用户级的程序来说是不可见的，通常称为Meta Data。
> 
> du 命令是用户级的程序，它不考虑Meta Data，而df命令则查看文件系统的磁盘分配图并考虑Meta Data。df命令获得真正的文件系统数据，而du命令只查看文件系统的部分情况。

**与ls区别**

> 文件大小的两个概念：
> （1）文件占用磁盘空间的大小
> （2）文件实际的大小
> 
> du -k属于第一种，计算的是文件占用磁盘空间的大小。
> 
> 在电脑的文件系统中，存储是以块(Block)为单位的，不同的系统块的大小不一样，比如说 macOS 一个块的大小是 4096 字节。假设一个文件有 4097 字节，4097-4096=1，这个文件在占用了一个块之后，还有一个字节会占用到一个块，而块与块之间是不共享空间的，也就是说，剩下的 1 字节占用了一个块，这个块还空出 4095 字节，但是无法用于存储其他文件。所以，这个大小为 4097 字节的文件占用了 2 个块。而 du -k 计算的正是每个文件占用块的多少。同理可得，其中必定有部分块是没有占满的，所以和实际的文件大小有差异。
> 
> ls -l查看文件实际大小而非块大小

### dpkg

> debian linux上安装、创建、管理软件包的工具

语法

> -i                安装软件包
> 
> -r                删除软件包
> 
> -P                删除软件包的同时删除其配置文件
> 
> -L                显示软件包关联的文件
> 
> -l                显示已安装软件包列表
> 
> --unpack    解开软件包
> 
> -c                显示软件包内文件列表
> 
> --confiugre    配置软件包
> 
> -s                查看软件包信息，是否已安装之类
> 
> -S                搜索

读取-l的信息| --list输出在

```
man dpkg-query
```

而**不是**

```
man dpkg
```

在这些情况下，dpkg仅充当前端

关于选项 l 的结果解析（可以通过 dpkg -l | head -n 3 查看）

```sh
Desired=Unknown/Install/Remove/Purge/Hold                                     
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)                
```

首字母：

> u    未知
> 
> i    安装
> 
> r    删除/卸载
> 
> p    清除（删除包括配置文件）
> 
> h    ？？？保持？保留？

第二个字母

> n    未安装
> 
> i    安装
> 
> c    仅安装配置文件
> 
> U    已解压
> 
> F    由于某种原因配置失败（半配置）
> 
> H    由于某种原因安装失败（半安装）
> 
> W    等待触发器（程序包正在等待另一个程序包的触发器）
> 
> t    触发挂起（已经触发）

第三个字母

> R    需要重新安装（包损坏 需重装）

1. ii 表示软件正常安装
2. rc表示软件已卸载，可是配置文件还在，可以通过以下命令进行清理。

```sh
dpkg -l | grep ^rc | cut -d' ' -f3 | sudo xargs dpkg --purge
```

### echo

echo(选项)(参数)选项

> -n:不换行输出
> 
> -e：激活转义字符。使用-e选项时，若字符串中出现以下字符，则特别加以处理，而不会将它当成一般文字输出：
> 
> > •\a 发出警告声；
> > •\b 删除前一个字符；
> > •\c 最后不加上换行符号；
> > •\f 换行但光标仍旧停留在原来的位置；
> > •\n 换行且光标移至行首；
> > •\r 光标移至行首，但不换行；
> > •\t 插入tab；
> > •\v 与\f相同；
> > •\\ 插入\字符；
> > •\nnn 插入nnn（八进制）所代表的ASCII字符；

**在脚本中echo自带转义功能**

**关于颜色输出**

```shell
#格式: 
echo -e "\033[字背景颜色;字体颜色m字符串\033[0m" 

#例如 打印红色输出
echo -e "\e[1;31m 内容 \e[0m"
#\e[1;31m 将颜色设置为红色
#\e[0m 将颜色重新置回
#颜色码：重置=0，黑色=30，红色=31，绿色=32，黄色=33，蓝色=34，洋红=35，青色=36，白色=37
```

```tex
字背景颜色范围:40----49 
40:黑 
41:深红 
42:绿 
43:黄色 
44:蓝色 
45:紫色 
46:深绿 
47:白色 

字颜色:30-----------39 
30:黑 
31:红 
32:绿 
33:黄 
34:蓝色 
35:紫色 
36:深绿 
37:白色 

=====================ANSI控制码的说明==========================
\33[0m 关闭所有属性 
\33[1m 设置高亮度 
\33[4m 下划线 
\33[5m 闪烁 
\33[7m 反显 
\33[8m 消隐 
\33[30m -- \33[37m 设置前景色 
\33[40m -- \33[47m 设置背景色 
\33[nA 光标上移n行 
\33[nB 光标下移n行 
\33[nC 光标右移n行 
\33[nD 光标左移n行 
\33[y;xH设置光标位置 
\33[2J 清屏 
\33[K 清除从光标到行尾的内容 
\33[s 保存光标位置 
\33[u 恢复光标位置 
\33[?25l 隐藏光标 
\33[?25h 显示光标

#\e和\033一个效果
```

### edquota

修改用户（群组）的磁盘配额

edit quota 缩写，用于修改用户和群组的配额限制参数，包括磁盘容量和文件个数限制、软限制和硬限制值、宽限时间，该命令的基本格式有以下 3 种：

```sh
[root@localhost ~]# edquota [-u 用户名] [-g 群组名]
[root@localhost ~]# edquota -t
[root@localhost ~]# edquota -p 源用户名 -u 新用户名
```

此命令各常用选项及功能如下：

| 选项     | 功能                             |
| ------ | ------------------------------ |
| -u 用户名 | 进入配额的 Vi 编辑界面，修改针对用户的配置值；      |
| -g 群组名 | 进入配额的 Vi 编辑界面，修改针对群组的配置值；      |
| -t     | 修改配额参数中的宽限时间；                  |
| -p     | 将源用户（或群组）的磁盘配额设置，复制给其他用户（或群组）。 |

例如，以用户 myquota 为例，通过如下命令配置此命令的 Quota：

```sh
[root@localhost ~]# edquota -u myquota
Disk quotas for user myquota (uid 710):
 Filesystem  blocks soft  hard inodes soft hard
 /dev/hda3     80   0   0   10   0   0
```

此命令的输出信息共 3 行，第一章指明了针对哪个用户进行配额限制，第二行是各个配额值的表头，共分为 7 列，其每一列的含义如表 2 所示。

| 表头               | 含义                                               |
| ---------------- | ------------------------------------------------ |
| 文件系统（filesystem） | 说明该限制值是针对哪个文件系统（或分区）；                            |
| 磁盘容量（blocks）     | 此列的数值是 quota 自己算出来的，单位为 Kbytes，不要手动修改；           |
| 磁盘容量的软限制（soft）   | 当用户使用的磁盘空间超过此限制值，则用户在登陆时会收到警告信息，告知用户磁盘已满，单位为 KB； |
| 磁盘容量的硬限制（hard）   | 要求用户使用的磁盘空间最大不能超过此限制值，单位为 KB；                    |
| 文件数量（inodes）     | 同 blocks 一样，此项也是 quota自己计算出来的，无需手动修改；            |
| 文件数量的软限制（soft）   | 当用户拥有的文件数量超过此值，系统会发出警告信息；                        |
| 文件数量的硬限制（hard）   | 用户拥有的文件数量不能超过此值。                                 |

注意，当 soft/hard 为 0 时，表示没有限制。另外，在 Vi（或 Vim）中修改配额值时，填写的数据无法保证同表头对齐，只要保证此行数据分为 7 个栏目即可。

【例 1】 修改用户 myquota 的软限制值和硬限制值。

```sh
[root@localhost ~]# edquota -u myquota
Disk quotas for user myquota (uid 710):
 Filesystem  blocks  soft  hard inodes soft hard
 /dev/hda3     80 250000 300000   10   0   0
```

【例 2】 修改群组 mygrpquota 的配额。

```sh
[root@localhost ~]# edquota -g mygrpquota
Disk quotas for group mygrpquota (gid 713):
 Filesystem  blocks  soft   hard inodes soft hard
 /dev/hda3    400 900000 1000000   50   0   0
```

【例 3】修改宽限天数。

```sh
[root@localhost ~]# edquota -t
Grace period before enforcing soft limits for users:
Time units may be: days, hours, minutes, or seconds
 Filesystem     Block grace period   Inode grace period
 /dev/hda3        14days         7days
```

### env

列出目前shell环境下的所有环境变量及其内容

### expand

将两个文件相同行的数据粘在一起，以空格隔开

### export

导入一个可以在当前shell以及子shell中使用的变量

### expr

```shell
#Linux下的数字运算，例如
expr 1 + 1        #输出2
```

### expect

> 通过expect可以实现将交互式的命令变为非交互式执行，不需要人为干预(手动输入)

用法：

| option         | 含义                                                 |
| -------------- | -------------------------------------------------- |
| set timeout 30 | 设置超时时间30s                                          |
| spawn ${cmd}   | spawn是执行expect之后后执行的内部命令开启一个会话 #功能:用来执行shell的交互命令  |
| expect         | 相当于捕捉                                              |
| send           | 执行交互动作，将交互要执行的命令进行发送给交互指令，命令字符串结尾要加上“\r”，#---相当于回车 |
| interact       | 执行完后保持交互状态，需要等待手动退出交互状态，如果不加这一项，交互完成会自动退出          |
| exp_continue   | 继续执行接下来的操作                                         |

实战非交互式ssh连接：

```sh
[root@qfedu script]# vim test.sh

#!/bin/sh

expect -c "
    set timeout 10
    spawn ssh root@localhost
    expect {
        \"yes/no\" { send \"yes\r\"; exp_continue }
        \"password:\" { send \"root\r\" }
    }
"
#注意花括号前一定要有空格

[root@qfedu script]# chmod +x test.sh

[root@qfedu script]# ./test.sh

spawn ssh root@localhost

root@localhost's password:

Last login: Fri Aug 28 16:57:09 2019

#如果添加interact参数将会等待我们手动交互进行退出。如果不加interact参数在登录成功之后会立刻退出。
```

### file

```tex
查看文件信息
    -b：列出辨识结果时，不显示文件名称； binary为二进制
```

### find

```shell
-type                            #指定类型
find / -inum  inodenum            #查找指定inodenum
```

与时间有关系的选项

- -mtime
  - -mtime n    ：n为数字，表示n天之前的【一天之内】被改动过的文件
  - -mtime +n    ：列出n天之前被改动过的文件【不包含n天】
  - -mtime -n    ：列出n天之后被改动过的文件【包含n天】
- -newer file    file作为一个存在的文件，列出比file更新的文件

### flock

```tex
flock是Linux下的文件锁。
当多个进程可能会对同样的数据执行操作时，这些进程需要保证其它进程没有也在操作，以免损坏数据。

    -s,--shared：获取一个共享锁，在定向为某文件的FD上设置共享锁而未释放锁的时间内，
    其他进程试图在定向为此文件的FD上设置独占锁的请求失败，
    而其他进程试图在定向为此文件的FD上设置共享锁的请求会成功。

    -x，-e，--exclusive：获取一个排它锁，或者称为写入锁，为默认项。

    -u，--unlock：手动释放锁，一般情况不必须，
    当FD关闭时，系统会自动解锁，此参数用于脚本命令一部分需要异步执行，一部分可以同步执行的情况。

    -n，--nb, --nonblock：非阻塞模式，当获取锁失败时，返回1而不是等待。

    -w, --wait, --timeout seconds：设置阻塞超时，
    当超过设置的秒数时，退出阻塞模式，返回1，并继续执行后面的语句。

    -o, --close：表示当执行command前关闭设置锁的FD，以使command的子进程不保持锁。

    -c, --command command：在shell中执行其后的语句。
```

### free

```tex
free    #显示内存的使用情况
    -b # 以Byte为单位显示内存使用情况；
    -k # 以KB为单位显示内存使用情况；
    -m # 以MB为单位显示内存使用情况；
    -g # 以GB为单位显示内存使用情况。 
    -o # 不显示缓冲区调节列；
    -s<间隔秒数> # 持续观察内存使用状况；
    -t # 显示内存总和列；
    -V # 显示版本信息。
```

### grep

```shell
-E                #在扩展正则模式下
-P                #在Perl正则模式下
-V                #将不匹配的过滤出来
-r/-R            #递归查找
-q                #安静模式，不在屏幕上输出
-i                #忽略大小写
-n                #增加行号
-o                #只输出文件中匹配到的部分
-m <num> --max-count=<num> # 找到num行结果后停止查找，用来限制匹配行数

--color            #红色输出吧
```

### head

```tex
显示文件的开头部分。
    -n, --lines=[-]NUM    显示前NUM行而不是默认的10行；
                        如果NUM前有"-"，那么会打印除了文件末尾的NUM行以外的其他行。
```

### host

查出某个主机的ip

用法

```
host [-a] hostname [server]
```

选项与参数

```
-a            列该主机详细的各项主机名设定数据
[server]    可以使用非为 /etc/resolv.cnf 的DNS 服务器
```

### iotop

**iotop命令** 是一个用来监视磁盘I/O使用状况的top类工具。iotop具有与top相似的UI，其中包括PID、用户、I/O、进程等相关信息。Linux下的IO统计工具如iostat，nmon等大多数是只能统计到per设备的读写情况，如果你想知道每个进程是如何使用IO的就比较麻烦，使用iotop命令可以很方便的查看。

iotop使用Python语言编写而成，要求Python2.5（及以上版本）和Linux kernel2.6.20（及以上版本）。iotop提供有源代码及rpm包，可从其官方主页下载。

**选项**

```shell
-o：只显示有io操作的进程
-b：批量显示，无交互，主要用作记录到文件。
-n NUM：显示NUM次，主要用于非交互式模式。
-d SEC：间隔SEC秒显示一次。
-p PID：监控的进程pid。
-u USER：监控的进程用户。
-t, --time 加上时间戳，非交互非模式。
```

**iotop常用快捷键：**

1. 左右箭头：改变排序方式，默认是按IO排序。
2. r：改变排序顺序。
3. o：只显示有IO输出的进程。
4. p：进程/线程的显示方式的切换。
5. a：显示累积使用量。
6. q：退出。

### ip

新版本查看网络状态

##### ip r

查看路由信息

##### ip a

查看网卡信息

参数详解：

> 1. lo：全称loopback，是回环地址，经常被分配到127.0.0.1地址上，用于本机通信，经过内核处理后直接返回，不会在任何网络中出现。
> 
> 2. eth0：网卡名，如果有多块网卡，会有多个eth 或其它名称。
>    
>    link/ether：这个是MAC地址，唯一的，一块网卡一个MAC。
>    
>    inet：网卡上绑定的IP地址，通常所说的IPV4，一块网卡可以绑定多个IP地址。在绑定IP地址时注意：windows主机会提示IP地址冲突，而linux主机无任何提示，在添加新的IP地址时务必检测一下新地址是否和原有地址冲突，避免造成访问不可用。常用检测命令：ping或arping IP；
>    
>    inet6：IPV6地址，暂时没有，预留。
> 
> 3. 网络设备状态标识：<BROADCAST,MULTICAST,UP,LOWER_UP>
>    
>    UP：网卡处于启动状态。
>    
>    BROADCAST：网卡有广播地址，可以发生广播包。
>    
>    MULTICAST：网卡可以发生多播包。
>    
>    LOWER_UP：L1是启动的，即网线是插着的。

`<BROADCAST,MULTICAST,UP,LOWER_UP>` 这个配置串告诉我们：

```text
BROADCAST   该接口支持广播
MULTICAST   该接口支持多播
UP          网络接口已启用
LOWER_UP    网络电缆已插入，设备已连接至网络
```

列出的其他值也告诉了我们很多关于接口的知识，但我们需要知道 `brd` 和 `qlen` 这些词代表什么意思。 所以，这里显示的是上面展示的 `ip` 信息的其余部分的翻译。

```text
mtu 1500                                    最大传输单位（数据包大小）为1,500字节
qdisc pfifo_fast                            用于数据包排队
state UP                                    网络接口已启用
group default                               接口组
qlen 1000                                   传输队列长度
link/ether 00:1e:4f:c8:43:fc                接口的 MAC（硬件）地址
brd ff:ff:ff:ff:ff:ff                       广播地址
inet 192.168.0.24/24                        IPv4 地址
brd 192.168.0.255                           广播地址
scope global                                全局有效
dynamic enp0s25                             地址是动态分配的
valid_lft 80866sec                          IPv4 地址的有效使用期限
preferred_lft 80866sec                      IPv4 地址的首选生存期
inet6 fe80::2c8e:1de0:a862:14fd/64          IPv6 地址
scope link                                  仅在此设备上有效
valid_lft forever                           IPv6 地址的有效使用期限
preferred_lft forever                       IPv6 地址的首选生存期
```

用法

```sh
ip [option] [动作] [指令]
```

选项与参数

```
-s        显示该装置的统计数据
    link    关于设备的相关设定，包括MTU Mac地址等
    addr/address    关于额外的ip协议。例如多ip的达成
    route    与路由相关的设定
```

link

```
show    仅显示出与这个装置相关的内容
set        可以开始设定项目，device指的是eth0等界面代号
        up|down    启动或者关闭某个接口
        address    如果这个装置可以修改mac地址，用这个修改
        name    命名
        mtu        最大传输单元
```

address

```
show    显示接口ip信息
add|del    添加/删除相关设定
        ip    主要就是网域的设定
        dev    这个ip参数设定的接口 如eth0，包含的参数如下
            broadcast    设定广播地址，如果设定值是+，表示自动设置
            label        装置的别名 例如 eth0:0
            scope        这个界面的领域，有以下几类
                global        允许来自所有来源的联机
                site        仅支持ipv6    仅允许本主机的联机
                link        仅允许本装置自我联机
                host        仅允许主机内部联机
```

route

```
show    单纯显示路由表，也可以使用list
add|del
    IP|网域    可以使用192.168.170.0/24这样的网域或者单纯的ip
    via        从那个gateway出去，不一定需要
    dev        由那个装置连接出去，需要
    mtu        额外设定MTU的数值
```

### iptables

遇到问题 --sport一直不能识别，百度也没查到原因

询问才知道。需要配合指定协议与multiport来匹配多端口才可以

端口如果使用 冒号 表示连续端口

> iptables其实不是真正的防火墙，可以理解为一个客户端代理，用户通过iptables这个代理，将用户的安全设定到对应的安全框架，而这个安全框架才是真正的防火墙，这个框架是 netfilter
> 
> netfilter 才是防火墙真正的安全框架，位于内核空间
> 
> netfilter/iptables 组成linux平台下的包过滤防火墙。免费，可以替代昂贵的商业防火墙解决方案，完成封包过滤、封包重定向、网络地址转换（NAT）等功能。
> 
> netfilter 是linux操作系统核心层内部的一个数据包处理模块，具有如下功能：
> 
> - 网络地址转换（network address translate）
> - 数据包内容修改
> - 以及数据包过滤的防火墙功能
> 
> 虽然使用 service iptables restart 来启动服务，更准确的说，iptables并没有一个守护进程，所以并不算是真正意义上的服务，而应该是内核提供的服务。

**命令**

```shell
iptables

    -P                #设置默认策略:iptables -P INPUT (DROP
    -F                #清空规则链
    -L                #查看规则链
    -A                #在规则链的末尾加入新规则
    -I                #num 在规则链的头部加入新规则
    -D                #num 删除某一条规则
    -s                #匹配来源地址IP/MASK，加叹号"!"表示除这个IP外。
    -d                #匹配目标地址
    -i                #网卡名称 匹配从这块网卡流入的数据
    -o                #网卡名称 匹配从这块网卡流出的数据
    -p                #匹配协议,如tcp,udp,icmp
    --dport num        #匹配目标端口号
    --sport num        #匹配来源端口号
    -n                 #表示不对 IP 地址进行反查，加上这个参数显示速度将会加快。
    -v                 #表示输出详细信息，包含通过该规则的数据包数量、总字节数以及相应的网络接口。
    -m                # 表示使用模块
```

可参考博客：https://www.zsythink.net/archives/1199

**iptables的使用模板大致为**

```shell
iptables -t 表名 <-A/I/D/R> 规则链名 [规则号] <-i/o 网卡名> -p 协议名 <-s 源IP/源子网> --sport 源端口 <-d 目标IP/目标子网> --dport 目标端口 -j 动作

#-A 指定链的末尾新增一个指定的规则
#-I    链的指定位置插入一条或多条规则
#-D 指定链的chain中删除一条或者多条规则
#-R num 替换/修改第几条规则

#-P 设置默认规则

# 例
iptables -t nat -A PERROUTING -p tcp -s 10.10.10.10 --sport 67 -d 10.10.10.11 --dport 67 -j ACCEPT

#这里如果是多端口可能会出现不能识别sport的情况 需搭配multiport
#multiport多端口，“，”表示或，“：”表示区间
iptables -t nat -A PERROUTING -p tcp -s 10.10.10.10 -m multiport --sport 67，68 -d 10.10.10.11 --dport 67 -j ACCEPT
```

**iptables默认链**

```shell
INPUT            #处理输入数据包
OUTPUT            #处理输出数据包
FORWARD            #处理转发数据包
PERROUTING        #用于目标地址转换（DNAT）
POSTROUTING        #用于源地址转换（SNAT）
```

**过滤框架**

![Linux命令](https://img-blog.csdnimg.cn/img_convert/ce49aedfc45c82ef6a6f261c82af07a4.gif)

如果是外部主机发送数据包给防火墙本机，数据将会经过 PREROUTING 链与 INPUT 链；如果是防火墙本机发送数据包到外部主机，数据将会经过 OUTPUT 链与 POSTROUTING 链；如果防火墙作为路由负责转发数据，则数据将经过 PREROUTING 链、FORWARD 链以及 POSTROUTING 链。

**四种表**

```shell
filter    #过滤功能，只能作用在三个链上面：INPUT,FORWARD,OUTPUT
nat        #地址转换，只能作用在：PREROUTING,OUTPUT,POSTROUTING(centos 7中还有INPUT)
mangle    #修改报文原数据，五个链都可以
raw        #关闭nat启用的追踪机制，PREROUTING,OUTPUT
```

换种方式

```
# 链                表
prerouting        raw --> mangle --> nat
input            mangle --> filter (centos7 has nat, 6 not)
forward            mangle --> filter
output            raw --> mangle --> nat --> filter
postrouting        mangle --> nat
```

**-j 的几种动作**

```shell
ACCEPT        #接收数据包
DROP        #丢弃数据包
REDIRECT    #重定向，映射,透明代理
SNAT        #源地址转换
DNAT        #目标地址转换
MASQUERADE    #IP伪装（NAT），用于ADSL
LOG            #日志记录
```

**常用的一些命令**

```shell
iptables -F        #清空所有的防火墙规则
iptables -nvL    #查看三个链

iptables -X INPUT  # 删除指定的链，这个链必须没有被其它任何规则引用，而且这条上必须没有任何规则。
                   # 如果没有指定链名，则会删除该表中所有非内置的链。
iptables -Z INPUT  # 把指定链，或者表中的所有链上的所有计数器清零。

iptables -L [-t 表名] [链名]    #列出已设置的规则
```

**-m的一些模块**

​    **multiport**: 多端口匹配

可用于匹配非连续或连续端口；最多指定15个端口；
实例

```shell
iptables -A INPUT -p tcp -m multiport --dport 22,80 -j ACCEPT
iptables -A OUTPUT -p tcp -m multiport --sport 22,80 -j ACCEPT
```

​    

​    **iprange**: 匹配指定范围内的地址

匹配一段连续的地址而非整个网络时有用
实例：

```shell
iptables -A INPUT -p tcp -m iprange --src-range 192.168.118.0-192.168.118.60 --dport 22 -j ACCEPT
iptables -A OUTPUT -p tcp -m iprange --dst-range 192.168.118.0-192.168.118.60 --sport 22 -j ACCEPT
```

**    string**: 字符串匹配，能够检测报文应用层中的字符串

字符匹配检查高效算法：kmp, bm 
能够屏蔽非法字符
实例：

```shell
#注意该条规则需要添加到OUTPUT链，当服务端返回数据报文检查到有关键字"sex"时，则丢弃该报文，可用于web敏感词过滤
iptables -A OUTPUT -p tcp --dport 80 -m string --algo kmp --string "sex" -j DROP
```

​    **connlimit**: 连接数限制，对每IP所能够发起并发连接数做限制；

实例：

默认INPUT 为 DROP. 每个ip对ssh服务的访问最大为3个并发连接，超过则丢弃

```
iptables -A INPUT -p tcp  --dport 22 -m connlimit ! --connlimit-above 3 -j ACCEPT
```

​    **limit**: 速率限制
limit-burst: 设置默认阀值

默认放行10个，当到达limit-burst阀值后，平均6秒放行1个

```
iptables -A INPUT -p icmp -m limit --limit 10/minute --limit-burst 10 -j ACCEPT
```

​    **state**: 状态检查

连接追踪中的状态：
    NEW: 新建立一个会话
    ESTABLISHED：已建立的连接
    RELATED: 有关联关系的连接
    INVALID: 无法识别的连接

```shell
#放行ssh的首次连接状态
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -j ACCEPT   
```

​    详细点

▪ INVALID：无效的封包，例如数据破损的封包状态

▪ ESTABLISHED：已经联机成功的联机状态；

▪ NEW：想要新建立联机的封包状态；

▪ RELATED：这个最常用！表示这个封包是与我们主机发送出去的封包有关， 可能是响应封包或者是联机成功之后的传送封包！这个状态很常被设定，因为设定了他之后，只要未来由本机发送出去的封包，即使我们没有设定封包的 INPUT 规则，该有关的封包还是可以进入我们主机， 可以简化相当多的设定规则。

​     **其他**

iptables-save：批量导出Linux防火墙规则，

> ​    直接执行：显示当前启用的所有规则，按raw、mangle、nat、filter顺序列出
> 
> ​    -c    指定在还原iptables表时候，还原当前的数据包计数器和字节计数器的值；
> 
> ​    -t    指定表
> 
> ​            “#”号开头的表示注释；“*表名”表示所在的表；
> 
> ​            “：链名默认策略”表示相应的链及默认策略，具体的规则部分省略了命令名“iptables”；
> 
> ​            “COMMIT”表示提交前面的规则设置；

```sh
# 这是注释
*nat
# 这表示下面这些是nat表中的配置
:PREROUTING ACCEPT [5129516:445315174]
# :PREROUTING ACCEPT，表示nat表中的PREROUTING 链默认报文策略是接受（匹配不到规则继续） ，

# [5129516:445315174] 即[packet, bytes]，表示当前有5129516个包(445315174字节)经过nat表的PREROUTING 链
:INPUT ACCEPT [942957:151143842]
:OUTPUT ACCEPT [23898:3536261]
:POSTROUTING ACCEPT [23898:3536261]
-- 解释同上
:DOCKER - [0:0]
-- 解释同上（此条是自定义链）
---------- 下面开始按条输出所有规则----------
[4075:366986] -A PREROUTING -m addrtype --dst-type LOCAL -j DOCKER
-- [4075:366986]即[packet, bytes]，表示经过此规则的包数，字节数。 后面部分则是用iptables命令配置此规则的命令（详解选项可参考iptables帮助）。
[0:0] -A OUTPUT ! -d 127.0.0.0/8 -m addrtype --dst-type LOCAL -j DOCKER
[0:0] -A POSTROUTING -s 172.17.0.0/16 ! -o docker0 -j MASQUERADE
[2:188] -A POSTROUTING -s 192.168.122.0/24 -d 224.0.0.0/24 -j RETURN
[0:0] -A POSTROUTING -s 192.168.122.0/24 -d 255.255.255.255/32 -j RETURN
[0:0] -A POSTROUTING -s 192.168.122.0/24 ! -d 192.168.122.0/24 -p tcp -j MASQUERADE --to-ports 1024-65535
[0:0] -A POSTROUTING -s 192.168.122.0/24 ! -d 192.168.122.0/24 -p udp -j MASQUERADE --to-ports 1024-65535
[0:0] -A POSTROUTING -s 192.168.122.0/24 ! -d 192.168.122.0/24 -j MASQUERADE
[0:0] -A DOCKER -i docker0 -j RETURN
--以上规则同第一条规则的解释
COMMIT
-- 应用上述配置
# Completed on Tue Jan 15 15:42:32 2019
```

iptables-restore：批量导入Linux防火墙规则

> ```shell
> #例如
> iptables-restore < /tmp/iptables.txt    #将/tmp/iptables.txt规则写入iptables
> ```
> 
> `备份恢复时，iptables-save、iptables-restore两个都需要搭配重定向符使用`

### join

处理两个文件之间的数据

- -t    join默认以空格符分隔数据，并且比对第一个字段的数据
  
  如果忽略两个文件相同，则将两笔数据联成一行，且第一个字段放在第一个

- -i    忽略大小写

- -1    数字的1，表示第一个文件要用哪个字段来分析

- -2    数字的2，表示第二个文件要用哪个字段分析

### locale

不带参数是查看已设置字符集

-a 查看已安装有字符集

### locale-gen

默认情况下，为基于 libc 的程序的本地化提供基本支持的 locale 包不包含每种支持语言的可用本地化文件。由于此类文件的巨大大小以及 libc 支持的大量语言，此限制变得必要。因此，Debian 使用了一种特殊的机制，我们在目标主机上准备实际的本地化文件并仅分发它们的模板。

**locale-gen**是一个程序，它读取文件 **/etc/locale.gen**并为所选的本地化配置文件调用 **localedef**。修改**/etc/locale.gen**文件后运行**locale-gen**。

**/etc/locale.gen**

主配置文件，具有简单的格式：每行不为空且不以 # 开头的行都被视为要构建的语言环境定义。
 **/var/lib/locales/supported.d/**

包含语言包提供的 locale.gen 片段的目录。不要手动编辑这些，它们将在包升级时被覆盖。

名字：

​      locale-gen - 编译本地定义文件的一个列表

简介：

​      locale-gen [options] [locale] [language]

描述：

​      编译本地文件需要50M的磁盘容量，并却大部分用户仅需要很少的locales. 为了节省磁盘容量，编译的locale 文件不在Locales包中发布，但是当这些包通过运行locale-gen程序安装的时候，可选的locales是自动产生的。

​      如果languages和locales的一个列表被具体到一个参数，那么locale-gen 仅仅产生这些具体的locales，并添加新的一些到/var/lib/locales/supported.d/local文件中。否则产生所有的支持的locales.

​      locale 数据文件可以存储在一个单一的二进制文件（/usr/lib/locale/locale-archive） ，或者在一个更深的树形结构下的个人文件/usr/lib/locale/<locale_name>/LC_*. 但是不像locales包，当运行locale-gen时，编译的locale definitions不被移除，如果locale源代码文件修改了，locales 才可以在一次编译。

选项：

​     这些选项覆盖了/etc/belocs/locale-gen.conf下的设置

​     --help 一些帮助信息和退出

​     --purge 在运行之前，移除所有存在的locales

​     --no-purge 与上相反

​     --archive 当这个选项被设置，Locale数据是被存储在单一的文档/usr/lib/locale/locale-archive

​     --no-archive

​     --aliases=FILE locale 别名从FILE文件中读出

文件：

​     /var/lib/locales/supported.d/*  列出了所有要产生的Locales。文件格式和/usr/share/i18n/SUPPORTED 相似。

​     /etc/belocs/locale-gen.conf 自定义编译的locale文件怎么存储到磁盘上。

​     /usr/lib/locale/<locale-name>/LC_* 编译Locale数据

​     /usr/lib/locale/locale-archive 产生包含编译的locale数据的归档，如果--archive 被设置

​     /var/lib/belocs 用于追踪在Locale源码文件变化的目录

环境变量：
    这些环境变量影响到每一个对所有的locale-aware程序的Locale类别

​    

LC_CTYPE

​        Character classification and case conversion.
 LC_COLLATE

​        Collation order.

LC_TIME

​        Date and time formats.

​    LC_NUMERIC

​        Non-monetary numeric formats.

​    LC_MONETARY

​        Monetary formats.

LC_MESSAGES

​        Formats of informative and diagnostic messages and
​        interactive responses.

​    LC_PAPER

​        Paper size.

​    LC_NAME

​        Name formats.

​    LC_ADDRESS

​        Address formats and location information.

LC_TELEPHONE

​        Telephone number formats.

​    LC_MEASUREMENT

​        Measurement units (Metric or Other).

​    LC_IDENTIFICATION

​        Metadata about the locale information.

​    This environment variable can switch against multiple locale database:

​    LOCPATH

​        The directory where locale data is stored. By default, /usr/lib/locale is used.

### lsblk

列出所有储存装置

- -d    仅列出磁盘本身，不列出分区数据
- -f    同时列出磁盘内的文件系统名称
- -i    使用ASCII的线段输出，不适用复杂编码
- -m    同时输出该装置在 /dev 下的权限信息
- -p    列出该装置的完整文件名，而不是仅列出最后的名字
- -t    列出该磁盘装置的详细数据，包括磁盘队列机制、预读写的数据量大小等

### ln

> 用来为文件创建链接，链接类型分为硬链接和符号链接两种，默认的链接类型是硬链接。如果要创建符号链接必须使用"-s"选项。

注意：符号链接文件不是一个独立的文件，它的许多属性依赖于源文件，所以给符号链接文件设置存取权限是没有意义的。

```
    --backup[=CONTROL]  为每个已存在的目标文件创建备份文件
-b        类似--backup，但不接受任何参数
-d, -F, --directory   创建指向目录的硬链接(只适用于超级用户)
-f, --force     强行删除任何已存在的目标文件
-i, --interactive           覆盖既有文件之前先询问用户；
-L, --logical               取消引用作为符号链接的目标
-n, --no-dereference        把符号链接的目的目录视为一般文件；
-P, --physical              直接将硬链接到符号链接
-r, --relative              创建相对于链接位置的符号链接
-s, --symbolic              对源文件建立符号链接，而非硬链接；
-S, --suffix=SUFFIX         用"-b"参数备份目标文件后，备份文件的字尾会被加上一个备份字符串，预设的备份字符串是符号“~”，用户可通过“-S”参数来改变它；
-t, --target-directory=DIRECTORY  指定要在其中创建链接的DIRECTORY
-T, --no-target-directory   将“LINK_NAME”视为常规文件
-v, --verbose               打印每个链接文件的名称
    --help    显示此帮助信息并退出
    --version   显示版本信息并退出
```

### lpr

将文件发送给指定打印机进行打印

###### 补充说明

**lpr命令** 用于将文件发送给指定打印机进行打印，如果不指定目标打印机，则使用默认打印机。

###### 语法

```shell
lpr(选项)(参数)
```

###### 选项

```shell
-E：与打印服务器连接时强制使用加密；
-H：指定可选的打印服务器；
-C：指定打印任务的名称；
-P：指定接受打印任务的目标打印机；
-U：指定可选的用户名；
-#：指定打印的份数；
-h：关闭banner打印；
-m：打印完成后发送E-mail；
-r：打印完成后删除文件。
```

###### 参数

文件：需打印的文件。

###### 实例

将man1和man2送到打印机lp进行打印：

```shell
lpr -P lp man1 man2
```

### ls

```shell
-l        #详细信息
-t        #按时间排序
-i        #输出innode信息
--block-size    # --block-size=m 以M为单位 --block-size=G 以G为单位
```

**“`ls -l`”输出的第一个字符列表**

| 字符  | 说明     |
| --- | ------ |
| -   | 普通文件   |
| d   | 目录     |
| l   | 符号链接   |
| c   | 字符设备节点 |
| b   | 块设备节点  |
| p   | 命名管道   |
| s   | 套接字    |

### lsof

```shell
#强大的查询工具，-i几乎万能（自吹）

#关键选项
#默认 : 没有选项，lsof列出活跃进程的所有打开文件
#组合 : 可以将选项组合到一起，如-abc，但要当心哪些选项需要参数
-a            #结果进行“与”运算（而不是“或”）
-l            #在输出显示用户ID而不是用户名
-h            #获得帮助
-t            #仅获取进程ID
-U            #获取UNIX套接口地址
-F            #格式化输出结果，用于其它命令。
            #可以通过多种方式格式化，如-F pcfn（用于进程id、命令名、文件描述符、文件名，并以空终止）
-i            #条件查询连接     -i（4,6，协议，：端口，@ip）
-c            #查看指定的命令正则使用的文件与网络连接    -c vim
-u            #显示指定用户打开了什么     -u user
            #消灭指定用户的所有东西    kill -9 `lsof -t -u luyi`
-p            #指定进程ID(pid)已经打开的文件    -p 643
+d            #查看某目录文件信息    不加d也可以，但是可能不全
+D            #递归查看某目录文件信息

#更详细的描述
#以及
#恢复被删除的文件，某种情况可参考下面
#https://www.cnblogs.com/sparkbj/p/7161669.html
```

### mail

发送信息

```sh
main -s '$标题' $username@$host < $file
```

### mkdir

```shell
#创建文件夹
-p     #如果没有则创建（多级目录的情况）
    #如果有 不作操作不报错

-v    #创建时输出
```

### 

### mkfifo

创建一个命令管道（FIFO）文件

可以通过 stdbuf -oL 来行缓冲读取

### mount

```
mount命令

1.功能：文件挂载

2.格式：mount [-参数] [设备名称] [挂载点]

3.常用选项：

-a ：安装在/etc/fstab文件中类出的所有文件系统。
-f ：伪装mount，作出检查设备和目录的样子，但并不真正挂载文件系统。
-n ：不把安装记录在/etc/mtab 文件中。
-r ：”将文件系统安装为只读。
-v ：详细显示安装信息。
-w：将文件系统安装为可写，为命令默认情况。
-t <文件系统类型> ：指定设备的文件系统类型，常见的有：
   ext2 是linux目前常用的文件系统
   msdos MS-DOS的fat，就是fat16
   vfat windows98常用的fat32
   nfs 网络文件系统
   iso9660 CD-ROM光盘标准文件系统
   ntfs windows NT/2000/XP的文件系统
   auto 自动检测文件系统
-o <选项> ：指定挂载文件系统时的选项，有些也可写到在 /etc/fstab 中。常用的有：
   defaults 使用所有选项的默认值（auto、nouser、rw、suid）
   auto/noauto 允许/不允许以 –a选项进行安装
   dev/nodev 对/不对文件系统上的特殊设备进行解释
   exec/noexec 允许/不允许执行二进制代码
   suid/nosuid 确认/不确认suid和sgid位
   user/nouser 允许/不允许一般用户挂载
   codepage=XXX 代码页
   iocharset=XXX 字符集
   ro 以只读方式挂载
   rw 以读写方式挂载
   remount 重新安装已经安装了的文件系统
   loop 挂载“回旋设备”以及“ISO镜像文件”
```

### mydumper

```bash
-B, --database              要备份的数据库，不指定则备份所有库
-T, --tables-list           需要备份的表，名字用逗号隔开
-o, --outputdir             备份文件输出的目录
-s, --statement-size        生成的insert语句的字节数，默认1000000
-r, --rows                  将表按行分块时，指定的块行数，指定这个选项会关闭 --chunk-filesize
-F, --chunk-filesize        将表按大小分块时，指定的块大小，单位是 MB
-c, --compress              压缩输出文件
-e, --build-empty-files     如果表数据是空，还是产生一个空文件（默认无数据则只有表结构文件）
-x, --regex                 是同正则表达式匹配 'db.table'
-i, --ignore-engines        忽略的存储引擎，用都厚分割
-m, --no-schemas            不备份表结构
-k, --no-locks              不使用临时共享只读锁，使用这个选项会造成数据不一致
--less-locking              减少对InnoDB表的锁施加时间（这种模式的机制下文详解）
-l, --long-query-guard      设定阻塞备份的长查询超时时间，单位是秒，默认是60秒（超时后默认mydumper将会退出）
--kill-long-queries         杀掉长查询 (不退出)
-b, --binlogs               导出binlog
-D, --daemon                启用守护进程模式，守护进程模式以某个间隔不间断对数据库进行备份
-I, --snapshot-interval     dump快照间隔时间，默认60s，需要在daemon模式下
-L, --logfile               使用的日志文件名(mydumper所产生的日志), 默认使用标准输出
--tz-utc                    跨时区是使用的选项，不解释了
--skip-tz-utc               同上
--use-savepoints            使用savepoints来减少采集metadata所造成的锁时间，需要 SUPER 权限
--success-on-1146           Not increment error count and Warning instead of Critical in case of table doesn't exist
-h, --host                  连接的主机名
-u, --user                  备份所使用的用户
-p, --password              密码
-P, --port                  端口
-S, --socket                使用socket通信时的socket文件
-t, --threads               开启的备份线程数，默认是4
-C, --compress-protocol     压缩与mysql通信的数据
-V, --version               显示版本号
-v, --verbose               输出信息模式, 0 = silent, 1 = errors, 2 = warnings, 3 = info, 默认为 2
```

### myloader

```bash
-d, --directory                   备份文件的文件夹
-q, --queries-per-transaction     每次事物执行的查询数量，默认是1000
-o, --overwrite-tables            如果要恢复的表存在，则先drop掉该表，使用该参数，需要备份时候要备份表结构
-B, --database                    需要还原的数据库
-e, --enable-binlog               启用还原数据的二进制日志
-h, --host                        主机
-u, --user                        还原的用户
-p, --password                    密码
-P, --port                        端口
-S, --socket                      socket文件
-t, --threads                     还原所使用的线程数，默认是4
-C, --compress-protocol           压缩协议
-V, --version                     显示版本
-v, --verbose                     输出模式, 0 = silent, 1 = errors, 2 = warnings, 3 = info, 默认为2
```

### netstat

```tex
打印Linux中网络系统的状态信息
    -a或--all：显示所有连线中的Socket；
    -A<网络类型>或--<网络类型>：列出该网络类型连线中的相关地址；
    -c或--continuous：持续列出网络状态；
    -C或--cache：显示路由器配置的快取信息；
    -e或--extend：显示网络其他相关信息；
    -F或--fib：显示FIB；
    -g或--groups：显示多重广播功能群组组员名单；
    -h或--help：在线帮助；
    -i或--interfaces：显示网络界面信息表单；
    -l或--listening：显示监控中的服务器的Socket；
    -M或--masquerade：显示伪装的网络连线；
    -n或--numeric：直接使用ip地址，而不通过域名服务器；
    -N或--netlink或--symbolic：显示网络硬件外围设备的符号连接名称；
    -o或--timers：显示计时器；
    -p或--programs：显示正在使用Socket的程序识别码和程序名称；
    -r或--route：显示Routing Table；
    -s或--statistice：显示网络工作信息统计表；
    -t或--tcp：显示TCP传输协议的连线状况；
    -u或--udp：显示UDP传输协议的连线状况；
    -v或--verbose：显示指令执行过程；
    -V或--version：显示版本信息；
    -w或--raw：显示RAW传输协议的连线状况；
    -x或--unix：此参数的效果和指定"-A unix"参数相同；
    --ip或--inet：此参数的效果和指定"-A inet"参数相同。
```

```shell
#列出所有端口 (包括监听和未监听的)
netstat -a     #列出所有端口
netstat -at    #列出所有tcp端口
netstat -au    #列出所有udp端口                             
#列出所有处于监听状态的 Socket
netstat -l        #只显示监听端口
netstat -lt       #只列出所有监听 tcp 端口
netstat -lu       #只列出所有监听 udp 端口
netstat -lx       #只列出所有监听 UNIX 端口

netstat -antup    #显示所有 及 占用程序名
```

安装

```sh
apt install net-tools
```

内容解释

```
Proto        该联机的封包协议
Recv-Q        非由用户程序连接所复制而来的总 bytes
Send-Q        由远程主机所传送而来，但不具有ACK标志的总bytes数，意指主动联机SYN或其他标志的封包所占的bytes数
Local Address    本地地址
Foreign Address    远程主机地址
stat        状态栏，有以下
    ESTABLISED    已建立的联机的状态
    SYNC_SENT    发出主动联机的联机封包
    SYNC_RECV    接收到一个要求联机的主动联机封包
    FIN_WAIT1    该插槽服务socket已中断，该联机正在断线中
    FIN_WAIT2    该联机已挂断，但正在等待对方主机响应断线确认的封包
    TIME_WAIT    该联机已挂断，但socket还在网络上等待结束
    LISTEN        通常在服务的监听port，可使用 -l查询
```

### nohub

不挂断地运行命令。no hangup的缩写，意即“不挂断”。

nohup运行由 Command参数和任何相关的 Arg参数指定的命令，忽略所有挂断（SIGHUP）信号；

**不挂断的运行，注意没有后台运行功能**。  就是指，用nohup运行命令可以使命令永久的执行下去，和用户终端没有关系，例如我们断开SSH连接都不会影响他的运行，注意了nohup没有后台运行的意思；&才是后台运行

**&是指在后台运行，但当用户推出(挂起)的时候，命令自动也跟着退出**   

那么，我们可以巧妙的吧他们结合起来用就是 nohup COMMAND & 这样就能使命令永久的在后台执行

### nslookup

使用系统配置进行域名解析

用法

```
nslookup [-query=[type]] [hostname|ip]
```

参数

```
-query=type        查询的类型，除了传统的IP与主机名对应外，DNS还有很多信息
```

### ntpdate

```shell
ntpdate -d ip                #检索ip是否可以作为ntp对时服务器
------------------

    -aKeyid    使用 Keyid 来认证全部数据包。
    -b    通过调用 settimeofday 子例程来增加时钟的时间。
    -d    指定调试方式。判断 ntpdate 命令会产生什么结果（不产生实际的结果）。
        结果再现在屏幕上。这个标志使用无特权的端口。
    -eAuthenticationDelay    指定延迟认证处理的时间秒数。
    -kKeyFile    当不使用缺省值 /etc/ntp.keys 文件时，为包含密钥的文件指定一个不同的名称。
    -oVersion    当轮询它的发出数据包时，指定使用的 NTP 版本实现。
                Version 的值可以是 1，2，3。缺省值是 3。
    -pSamples    指定从每个服务器获取的样本的数目。 
                Samples 的值在 1 和 8 之间，并包括 1 和 8。它的缺省值是 4。
    -s    指定日志操作 syslog 设施的使用，而不是使用标准输出。 
        当运行 ntpdate 命令和 cron命令时，它是很有用的。
    -tTimeOut    指定等待响应的时间。给定 TimeOut 的值四舍五入为 0.2 秒的倍数。缺省值是 1 秒。
    -u    指定使用无特权的端口发送数据包。 
        当在一个对特权端口的输入流量进行阻拦的防火墙后是很有益的， 并希望在防火墙之外和主机同步。
        防火墙是一个系统或者计算机，它控制从外网对专用网的访问。
```

### ntpq

ntpq指令使用NTP模式6数据包与NTP服务器通信,能够在允许的网络上查询的兼容的服务器。它以交互模式运行,或者通过命令行参数运行。

此命令的适用范围：RedHat、RHEL、Ubuntu、CentOS、Fedora。

**语法格式：**ntpq [参数]

**常用参数：**

| 选项           | 含义                |
| ------------ | ----------------- |
| -4           | 使用ipv4解析          |
| -6           | 使用ipv6解析          |
| -c [command] | 添加执行的命令到指定主机的命令列表 |
| -d           | 打开调试模式            |
| -i           | 使用交互模式            |
| -n           | 以十进制格式显示主机地址      |
| -p           | 显示服务器同级设备的列表      |

注意设置ntp的时候，server表示对时服务器，restrict表示对服务器做限制

一：restrict选项格式

restrict [ 客户端IP ]  mask  [ IP掩码 ]  [参数]

“客户端IP” 和 “IP掩码” 指定了对网络中哪些范围的计算机进行控制，如果使用default关键字，则表示对所有的计算机进行控制，参数指定了具体的限制内容，常见的参数如下：

◆ ignore：拒绝连接到NTP服务器
◆ nomodiy： 忽略所有改变NTP服务器配置的报文，但可以查询配置信息
◆ noquery： 忽略所有mode字段为6或7的报文，客户端不能改变NTP服务器配置，也不能查询配置信息
◆ notrap： 不提供trap远程登录功能，trap服务是一种远程时间日志服务。
◆ notrust： 不作为同步的时钟源。
◆ nopeer： 提供时间服务，但不作为对等体。
◆ kod： 向不安全的访问者发送Kiss-Of-Death报文。

二：server选项格式

server host  [ key n ] [ version n ] [ prefer ] [ mode n ] [ minpoll n ] [ maxpoll n ] [ iburst ]

其中host是上层NTP服务器的IP地址或域名，随后所跟的参数解释如下所示：

◆ key： 表示所有发往服务器的报文包含有秘钥加密的认证信息，n是32位的整数，表示秘钥号。
◆ version： 表示发往上层服务器的报文使用的版本号，n默认是3，可以是1或者2。

◆ prefer： 如果有多个server选项，具有该参数的服务器有限使用。
◆ mode： 指定数据报文mode字段的值。
◆ minpoll： 指定与查询该服务器的最小时间间隔为2的n次方秒，n默认为6，范围为4-14。

◆ maxpoll：  指定与查询该服务器的最大时间间隔为2的n次方秒，n默认为10，范围为4-14。

◆ iburst： 当初始同步请求时，采用突发方式接连发送8个报文，时间间隔为2秒。

参考：

[ntp服务器restrict和server选项格式](https://blog.csdn.net/wjciayf/article/details/51396144)

### openssl

```shell
#强大的安全套接字层密码库
#利用它的随机功能来生成可以用作密码的随机字母字符串。
openssl rand -base64 10
# nU9LlHO5nsuUvw==

#standard 标准
# digest 消化 摘要
# cipher 加密
```

OpenSSL有两种运行模式：交互模式和批处理模式。

直接输入openssl回车进入交互模式，输入带命令选项的openssl进入批处理模式。

OpenSSL整个软件包大概可以分成三个主要的功能部分：密码算法库、SSL协议库以及应用程序。OpenSSL的目录结构自然也是围绕这三个功能部分进行规划的。 

**对称加密算法**

OpenSSL一共提供了8种对称加密算法，其中7种是分组加密算法，仅有的一种流加密算法是RC4。这7种分组加密算法分别是AES、DES、Blowfish、CAST、IDEA、RC2、RC5，都支持电子密码本模式（ECB）、加密分组链接模式（CBC）、加密反馈模式（CFB）和输出反馈模式（OFB）四种常用的分组密码加密模式。其中，AES使用的加密反馈模式（CFB）和输出反馈模式（OFB）分组长度是128位，其它算法使用的则是64位。事实上，DES算法里面不仅仅是常用的DES算法，还支持三个密钥和两个密钥3DES算法。 

**非对称加密算法**

OpenSSL一共实现了4种非对称加密算法，包括DH算法、RSA算法、DSA算法和椭圆曲线算法（EC）。DH算法一般用户密钥交换。RSA算法既可以用于密钥交换，也可以用于数字签名，当然，如果你能够忍受其缓慢的速度，那么也可以用于数据加密。DSA算法则一般只用于数字签名。 

**信息摘要算法**

OpenSSL实现了5种信息摘要算法，分别是MD2、MD5、MDC2、SHA（SHA1）和RIPEMD。SHA算法事实上包括了SHA和SHA1两种信息摘要算法，此外，OpenSSL还实现了DSS标准中规定的两种信息摘要算法DSS和DSS1。 

**密钥和证书管理**

密钥和证书管理是PKI的一个重要组成部分，OpenSSL为之提供了丰富的功能，支持多种标准。 

首先，OpenSSL实现了ASN.1的证书和密钥相关标准，提供了对证书、公钥、私钥、证书请求以及CRL等数据对象的DER、PEM和BASE64的编解码功能。OpenSSL提供了产生各种公开密钥对和对称密钥的方法、函数和应用程序，同时提供了对公钥和私钥的DER编解码功能。并实现了私钥的PKCS#12和PKCS#8的编解码功能。OpenSSL在标准中提供了对私钥的加密保护功能，使得密钥可以安全地进行存储和分发。 

在此基础上，OpenSSL实现了对证书的X.509标准编解码、PKCS#12格式的编解码以及PKCS#7的编解码功能。并提供了一种文本数据库，支持证书的管理功能，包括证书密钥产生、请求产生、证书签发、吊销和验证等功能。 

事实上，OpenSSL提供的CA应用程序就是一个小型的证书管理中心（CA），实现了证书签发的整个流程和证书管理的大部分机制。

[openssl用法详解](https://www.cnblogs.com/yangxiaolan/p/6256838.html)

### parted

列出磁盘的分区表类型与分区信息

### partprobe

更新linux核心的分区表信息

### passwd

修改密码

### paste

将两个文件相同行的数据粘在一起，以tab隔开

### patch

对比两个文件变化

制作补丁

### ping

主要透过 icmp 封包 探索网络

```
-c 数值        表示执行ping的次数
-n            不进行ip与主机名的反查，直接用ip输出（速度较快）
-s 数值        发出去的 icmp 封包大小，预设为56bytes
-t 数值        TTL的数值，预设是255，每经过一个节点就减一
-W 数值        等待响应对方主机的秒数
-M [do|dont]    主要在侦测网络的MTU数值大小
    do        代表传送一个 DF（Dont Fragment）旗标，让封包不能重新拆包与打包
    dont    代表不要传送 DF标志，表示封包可以在其他主机封包、打包
```

### pkill

当作于管理进程时，pkill 命令和 killall 命令的用法相同，都是通过进程名杀死一类进程，该命令的基本格式如下：

```
[root@localhost ~]# pkill [信号] 进程名
```

pkill 命令常用信号及其含义

| 信号编号 | 信号名  | 含义                                                  |
| ---- | ---- | --------------------------------------------------- |
| 0    | EXIT | 程序退出时收到该信息。                                         |
| 1    | HUP  | 挂掉电话线或终端连接的挂起信号，这个信号也会造成某些进程在没有终止的情况下重新初始化。         |
| 2    | INT  | 表示结束进程，但并不是强制性的，常用的 "Ctrl+C" 组合键发出就是一个 kill -2 的信号。 |
| 3    | QUIT | 退出。                                                 |
| 9    | KILL | 杀死进程，即强制结束进程。                                       |
| 11   | SEGV | 段错误。                                                |
| 15   | TERM | 正常结束进程，是 kill 命令的默认信号。                              |

还可以踢出登陆用户

除此之外，pkill 还有一个更重要的功能，即按照终端号来踢出用户登录，此时的 pkill 命令的基本格式如下：

```
[root@localhost ~]# pkill [-t 终端号] 进程名
```

[-t 终端号] 选项用于按照终端号踢出用户；

学习 killall 命令时，不知道大家发现没有，通过 killall 命令杀死 sshd 进程的方式来踢出用户，非常容易误杀死进程，要么会把 sshd 服务杀死，要么会把自己的登录终端杀死。

所以，不管是使用 kill 命令按照 PID 杀死登录进程，还是使用 killall 命令按照进程名杀死登录进程，都是非常容易误杀死进程的，而使用 pkill 命令则不会，举个例子：

```
[root@localhost ~]# w
#使用w命令查询本机已经登录的用户
20:06:34 up 28 min, 3 users, load average: 0.00, 0.00, 0.00
USER  TTY           FROM LOGIN@  IDLE  JCPU  PCPU WHAT
root ttyl              -  19:47 18:52 0.01s 0.01s -bash
root pts/0 192.168.0.100  19:47 0.00s 0.09s 0.04s w
root pts/1 192.168.0.100  19:51 14:56 0.02s 0.02s -bash
#当前主机已经登录了三个root用户，一个是本地终端ttyl登录，另外两个是从192.168.0.100登陆的远程登录
[root@localhost ~]# pkill -9 -t pts/1
#强制杀死从pts/1虚拟终端登陆的进程
[root@localhost ~]# w
20:09:09 up 30 min, 2 users, load average: 0.00, 0.00,0.00
USER   TTY          FROM LOGIN@  IDLE  JCPU  PCPU WHAT
root  ttyl             -  19:47 21:27 0.01s 0.01s -bash
root pts/0 192.168.0.100  19:47 0.00s 0.06s 0.00s w
#虚拟终端pts/1的登录进程已经被杀死了
```

### pr

将文本文件转换成适合打印的格式

###### 补充说明

**pr命令** 用来将文本文件转换成适合打印的格式，它可以把较大的文件分割成多个页面进行打印，并为每个页面添加标题。

###### 语法

```shell
pr(选项)(参数)
```

###### 选项

```shell
-h<标题>：为页指定标题；
-l<行数>：指定每页的行数。
```

###### 参数

文件：需要转换格式的文件。

### ps

> 用于报告当前系统的进程状态。可以搭配kill指令随时中断、删除不必要的程序。ps命令是最基本同时也是非常强大的进程查看命令，使用该命令可以确定有哪些进程正在运行和运行的状态、进程是否结束、进程有没有僵死、哪些进程占用了过多的资源等等，总之大部分信息都是可以通过执行该命令得到的。

```
-a：显示所有终端机下执行的程序，除了阶段作业领导者之外。
a：显示现行终端机下的所有程序，包括其他用户的程序。
-A：显示所有程序。
-c：显示CLS和PRI栏位。
c：列出程序时，显示每个程序真正的指令名称，而不包含路径，选项或常驻服务的标示。
-C<指令名称>：指定执行指令的名称，并列出该指令的程序的状况。
-d：显示所有程序，但不包括阶段作业领导者的程序。
-e：此选项的效果和指定"A"选项相同。
e：列出程序时，显示每个程序所使用的环境变量。
-f：显示UID,PPIP,C与STIME栏位。
f：用ASCII字符显示树状结构，表达程序间的相互关系。
-g<群组名称>：此选项的效果和指定"-G"选项相同，当亦能使用阶段作业领导者的名称来指定。
g：显示现行终端机下的所有程序，包括群组领导者的程序。
-G<群组识别码>：列出属于该群组的程序的状况，也可使用群组名称来指定。
h：不显示标题列。
-H：显示树状结构，表示程序间的相互关系。
-j或j：采用工作控制的格式显示程序状况。
-l或l：采用详细的格式来显示程序状况。
L：列出栏位的相关信息。
-m或m：显示所有的执行绪。
n：以数字来表示USER和WCHAN栏位。
-N：显示所有的程序，除了执行ps指令终端机下的程序之外。
-p<程序识别码>：指定程序识别码，并列出该程序的状况。
p<程序识别码>：此选项的效果和指定"-p"选项相同，只在列表格式方面稍有差异。
r：只列出现行终端机正在执行中的程序。
-s<阶段作业>：指定阶段作业的程序识别码，并列出隶属该阶段作业的程序的状况。
s：采用程序信号的格式显示程序状况。
S：列出程序时，包括已中断的子程序资料。
-t<终端机编号>：指定终端机编号，并列出属于该终端机的程序的状况。
t<终端机编号>：此选项的效果和指定"-t"选项相同，只在列表格式方面稍有差异。
-T：显示现行终端机下的所有程序。
-u<用户识别码>：此选项的效果和指定"-U"选项相同。
u：以用户为主的格式来显示程序状况。
-U<用户识别码>：列出属于该用户的程序的状况，也可使用用户名称来指定。
U<用户名称>：列出属于该用户的程序的状况。
v：采用虚拟内存的格式显示程序状况。
x：显示所有程序，不以终端机来区分。
X：采用旧式的Linux i386登陆格式显示程序状况。
```

![img](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/875796-20190926175914732-761997808.png)

关于ps 的 stat状态解释

- X    死掉的进程（未开启）
- <    高优先级
- N    低优先级
- L    有些页被锁进内存，有记忆体的分页分配并锁在记忆体内
- s    包含子进程，某一个会话的Leader进程
- \+    位于后台的进程组，属于某个前台组的进程
- l    多线程，克隆线程 multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
- WCHAN    正在等待的进程资源
- D    不可中断的进程，不可中断睡眠（通常是在IO操作）收到信号不唤醒和不可运行，进程必须等待直到有中断发生
- R    正在执行中，正在运行或可运行（在运行队列排队中）
- S    静止状态，可中断睡眠（休眠中，受阻，在等待某个条件的形成或接受到信号）
- T    暂停执行
- Z    僵尸进程，进程已终止，但进程描述符存在，直到父进程调用wait4()系统调用后释放
- W    没有足够的记忆体分页可分配 ，正在换页（2.6内核之前有效）

![image-20220210133849898](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/image-20220210133849898.png)

### pv

Pipe Viewer 显示当前在命令行执行的命令的进度信息，管道查看器

```
-p, --progress           显示进度条
-t, --timer              显示已用时间
-e, --eta                显示预计到达时间 (完成)
-I, --fineta             显示绝对估计到达时间
                         (完成)
-r, --rate               显示数据传输速率计数器
-a, --average-rate       显示数据传输平均速率计数器
-b, --bytes              显示传输的字节数
-T, --buffer-percent     显示正在使用的传输缓冲区百分比
-A, --last-written NUM   显示上次写入的字节数
-F, --format FORMAT      将输出格式设置为FORMAT
-n, --numeric            输出百分比
-q, --quiet              不输出任何信息

-W, --wait               在传输第一个字节之前不显示任何内容
-D, --delay-start SEC    在SEC秒过去之前不显示任何内容
-s, --size SIZE          将估算的数据大小设置为SIZE字节
-l, --line-mode          计算行数而不是字节数 
-0, --null               行以零结尾
-i, --interval SEC       每SEC秒更新一次
-w, --width WIDTH        假设终端的宽度为WIDTH个字符 
-H, --height HEIGHT      假设终端高度为HEIGHT行
-N, --name NAME          在可视信息前面加上名称
-f, --force              将标准错误输出到终端
-c, --cursor             使用光标定位转义序列

-L, --rate-limit RATE    将传输限制为每秒RATE字节
-B, --buffer-size BYTES  使用BYTES的缓冲区大小
-C, --no-splice          从不使用splice()，始终使用读/写
-E, --skip-errors        跳过输入中的读取错误
-S, --stop-at-size       传输--size字节后停止
-R, --remote PID         更新过程PID的设置

-P, --pidfile FILE       将进程ID保存在FILE中 

-d, --watchfd PID[:FD]   监视进程PID,打开的文件FD

-h, --help               显示帮助
-V, --version            显示版本信息
```

### pwck

检查账号文件 /etc/passwd 配置信息是否正确

会与 /etc/shadow 比对

### pwd

print working directory

显示当前路径

```
-P    显示真实路径 而非链接路径
```

### read

用于交互使用

![image-20211127175054717](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/image-20211127175054717.png)

### readlink

> [Linux](http://lib.csdn.net/base/linux)系统中一个常用工具，主要用来找出符号链接所指向的位置。

```sh
-f             #递归跟随给出文件名的所有符号链接以标准化，除最后一个外所有组件必须存在。
            #简单地说，就是一直跟随符号链接，直到非符号链接的文件位置，
            #限制是最后必须存在一个非符号链接的文件。
```

### rename

```sh
#在Debian或者Ubuntu环境下使用的语法是：
rename 's/stringx/stringy/' files

#而在CentOS下或者RedHat下是：
rename stringx stringy files

#rename的参数分为三部分：
#stringx ： 被替换字符串
#stringy ：替换字符串
#files ：匹配的文件列表
```

### rsync

**rsync命令** 是一个远程数据同步工具，可通过LAN/WAN快速同步多台主机间的文件。rsync使用所谓的“rsync算法”来使本地和远程两个主机之间的文件达到同步，这个算法只传送两个文件的不同部分，而不是每次都整份传送，因此速度相当快。 rsync是一个功能非常强大的工具，其命令也有很多功能特色选项，我们下面就对它的选项一一进行分析说明。

**语法**

```shell
rsync [OPTION]... SRC DEST
rsync [OPTION]... SRC [USER@]host:DEST
rsync [OPTION]... [USER@]HOST:SRC DEST
rsync [OPTION]... [USER@]HOST::SRC DEST
rsync [OPTION]... SRC [USER@]HOST::DEST
rsync [OPTION]... rsync://[USER@]HOST[:PORT]/SRC [DEST]
```

对应于以上六种命令格式，rsync有六种不同的工作模式：

1. 拷贝本地文件。当SRC和DES路径信息都不包含有单个冒号":"分隔符时就启动这种工作模式。如：`rsync -a /data /backup`
2. 使用一个远程shell程序(如rsh、ssh)来实现将本地机器的内容拷贝到远程机器。当DST路径地址包含单个冒号":"分隔符时启动该模式。如：`rsync -avz *.c foo:src`
3. 使用一个远程shell程序(如rsh、ssh)来实现将远程机器的内容拷贝到本地机器。当SRC地址路径包含单个冒号":"分隔符时启动该模式。如：`rsync -avz foo:src/bar /data`
4. 从远程rsync服务器中拷贝文件到本地机。当SRC路径信息包含"::"分隔符时启动该模式。如：`rsync -av root@192.168.78.192::www /databack`
5. 从本地机器拷贝文件到远程rsync服务器中。当DST路径信息包含"::"分隔符时启动该模式。如：`rsync -av /databack root@192.168.78.192::www`
6. 列远程机的文件列表。这类似于rsync传输，不过只要在命令中省略掉本地机信息即可。如：`rsync -v rsync://192.168.78.192/www`

**选项**

```shell
-v, --verbose 详细模式输出。
-q, --quiet 精简输出模式。
-c, --checksum 打开校验开关，强制对文件传输进行校验。
-a, --archive 归档模式，表示以递归方式传输文件，并保持所有文件属性，等于-rlptgoD。
-r, --recursive 对子目录以递归模式处理。
-R, --relative 使用相对路径信息。
-b, --backup 创建备份，也就是对于目的已经存在有同样的文件名时，将老的文件重新命名为~filename。可以使用--suffix选项来指定不同的备份文件前缀。
--backup-dir 将备份文件(如~filename)存放在在目录下。
-suffix=SUFFIX 定义备份文件前缀。
-u, --update 仅仅进行更新，也就是跳过所有已经存在于DST，并且文件时间晚于要备份的文件，不覆盖更新的文件。
-l, --links 保留软链结。
-L, --copy-links 想对待常规文件一样处理软链结。
--copy-unsafe-links 仅仅拷贝指向SRC路径目录树以外的链结。
--safe-links 忽略指向SRC路径目录树以外的链结。
-H, --hard-links 保留硬链结。
-p, --perms 保持文件权限。
-o, --owner 保持文件属主信息。
-g, --group 保持文件属组信息。
-D, --devices 保持设备文件信息。
-t, --times 保持文件时间信息。
-S, --sparse 对稀疏文件进行特殊处理以节省DST的空间。
-n, --dry-run现实哪些文件将被传输。
-w, --whole-file 拷贝文件，不进行增量检测。
-x, --one-file-system 不要跨越文件系统边界。
-B, --block-size=SIZE 检验算法使用的块尺寸，默认是700字节。
-e, --rsh=command 指定使用rsh、ssh方式进行数据同步。
--rsync-path=PATH 指定远程服务器上的rsync命令所在路径信息。
-C, --cvs-exclude 使用和CVS一样的方法自动忽略文件，用来排除那些不希望传输的文件。
--existing 仅仅更新那些已经存在于DST的文件，而不备份那些新创建的文件。
--delete 删除那些DST中SRC没有的文件。
--delete-excluded 同样删除接收端那些被该选项指定排除的文件。
--delete-after 传输结束以后再删除。
--ignore-errors 及时出现IO错误也进行删除。
--max-delete=NUM 最多删除NUM个文件。
--partial 保留那些因故没有完全传输的文件，以是加快随后的再次传输。
--force 强制删除目录，即使不为空。
--numeric-ids 不将数字的用户和组id匹配为用户名和组名。
--timeout=time ip超时时间，单位为秒。
-I, --ignore-times 不跳过那些有同样的时间和长度的文件。
--size-only 当决定是否要备份文件时，仅仅察看文件大小而不考虑文件时间。
--modify-window=NUM 决定文件是否时间相同时使用的时间戳窗口，默认为0。
-T --temp-dir=DIR 在DIR中创建临时文件。
--compare-dest=DIR 同样比较DIR中的文件来决定是否需要备份。
-P 等同于 --partial。
--progress 显示备份过程。
-z, --compress 对备份的文件在传输时进行压缩处理。
--exclude=PATTERN 指定排除不需要传输的文件模式。
--include=PATTERN 指定不排除而需要传输的文件模式。
--exclude-from=FILE 排除FILE中指定模式的文件。
--include-from=FILE 不排除FILE指定模式匹配的文件。
--version 打印版本信息。
--address 绑定到特定的地址。
--config=FILE 指定其他的配置文件，不使用默认的rsyncd.conf文件。
--port=PORT 指定其他的rsync服务端口。
--blocking-io 对远程shell使用阻塞IO。
-stats 给出某些文件的传输状态。
--progress 在传输时现实传输过程。
--log-format=formAT 指定日志文件格式。
--password-file=FILE 从FILE中得到密码。
--bwlimit=KBPS 限制I/O带宽，KBytes per second。
-h, --help 显示帮助信息。
```

| OPTION选项            | 功能                                                                                                                                                          |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -a                  | 这是归档模式，表示以递归方式传输文件，并保持所有属性，它等同于-r、-l、-p、-t、-g、-o、-D 选项。-a 选项后面可以跟一个 --no-OPTION，表示关闭 -r、-l、-p、-t、-g、-o、-D 中的某一个，比如-a --no-l 等同于 -r、-p、-t、-g、-o、-D 选项。       |
| -r                  | 表示以递归模式处理子目录，它主要是针对目录来说的，如果单独传一个文件不需要加 -r 选项，但是传输目录时必须加。                                                                                                    |
| -v                  | 表示打印一些信息，比如文件列表、文件数量等。                                                                                                                                      |
| -l                  | 表示保留软连接。                                                                                                                                                    |
| -L                  | 表示像对待常规文件一样处理软连接。如果是 SRC 中有软连接文件，则加上该选项后，将会把软连接指向的目标文件复制到 DEST。                                                                                             |
| -p                  | 表示保持文件权限。                                                                                                                                                   |
| -o                  | 表示保持文件属主信息。                                                                                                                                                 |
| -g                  | 表示保持文件属组信息。                                                                                                                                                 |
| -D                  | 表示保持设备文件信息。                                                                                                                                                 |
| -t                  | 表示保持文件时间信息。                                                                                                                                                 |
| --delete            | 表示删除 DEST 中 SRC 没有的文件。                                                                                                                                      |
| --exclude=PATTERN   | 表示指定排除不需要传输的文件，等号后面跟文件名，可以是通配符模式（如 *.txt）。                                                                                                                  |
| --progress          | 表示在同步的过程中可以看到同步的过程状态，比如统计要同步的文件数量、 同步的文件传输速度等。                                                                                                              |
| -u                  | 表示把 DEST 中比 SRC 还新的文件排除掉，不会覆盖。                                                                                                                              |
| -z                  | 加上该选项，将会在传输过程中压缩。                                                                                                                                           |
| -vazcr              |                                                                                                                                                             |
| --partial           | 保留那些因故没有完全传输的文件，加快随后的再次传输。<br/>参数允许恢复中断的传输。不使用该参数时，`rsync`会删除传输到一半被打断的文件；<br/>使用该参数后，传输到一半的文件也会同步到目标目录，下次同步时再恢复中断的传输。一般需要与`--append`或`--append-verify`配合使用。 |
| --copy-unsafe-links | 仅仅拷贝指向SRC路径目录树以外的链结。                                                                                                                                        |
| --append            | 参数指定文件接着上次中断的地方，继续传输。                                                                                                                                       |
| --append-verify     | 参数跟`--append`参数类似，但会对传输完成后的文件进行一次校验。如果校验失败，将重新发送整个文件。                                                                                                       |
| --bwlimit=KBPS      | 限制 i/o 带宽，KBnytes pre second                                                                                                                                |

以上也仅是列出了 async 命令常用的一些选项，对于初学者来说，记住最常用的几个即可，比如 -a、-v、-z、--delete 和 --exclude。

### rz

在终端下载本地文件

### scp

加密的方式在本地主机和远程主机之间复制文件（基于ssh）

> 用于在Linux下进行远程拷贝文件的命令，和它类似的命令有cp，不过cp只是在本机进行拷贝不能跨服务器，而且scp传输是加密的。可能会稍微影响一下速度。当你服务器硬盘变为只读read only system时，用scp可以帮你把文件移出来。另外，scp还非常不占资源，不会提高多少系统负荷，在这一点上，rsync就远远不及它了。虽然 rsync比scp会快一点，但当小文件众多的情况下，rsync会导致硬盘I/O非常高，而scp基本不影响系统正常使用。

**语法**

```shell
scp(选项)(参数)
```

**选项**

```shell
-1： 强制scp命令使用协议ssh1
-2： 强制scp命令使用协议ssh2
-4： 强制scp命令只使用IPv4寻址
-6： 强制scp命令只使用IPv6寻址
-B： 使用批处理模式（传输过程中不询问传输口令或短语）
-C： 允许压缩。（将-C标志传递给ssh，从而打开压缩功能）
-p：保留原文件的修改时间，访问时间和访问权限。
-q： 不显示传输进度条。
-r： 递归复制整个目录。
-v：详细方式显示输出。scp和ssh(1)会显示出整个过程的调试信息。这些信息用于调试连接，验证和配置问题。
-c cipher： 以cipher将数据传输进行加密，这个选项将直接传递给ssh。
-F ssh_config： 指定一个替代的ssh配置文件，此参数直接传递给ssh。
-i identity_file： 从指定文件中读取传输时使用的密钥文件，此参数直接传递给ssh。
-l limit： 限定用户所能使用的带宽，以Kbit/s为单位。
-o ssh_option： 如果习惯于使用ssh_config(5)中的参数传递方式，
-P port：注意是大写的P, port是指定数据传输用到的端口号
-S program： 指定加密传输时所使用的程序。此程序必须能够理解ssh(1)的选项。
```

**参数**

- 源文件：指定要复制的源文件。
- 目标文件：目标文件。格式为`user@host：filename`（文件名为目标文件的名称）。

### script

- -a 选项 ，在现有输出录制的文件的内容上追加新的内容
- -c选项 ，后面可以加上需要执行的命令，而不是交互式shell上执行的命令
- -r选项 ， 子进程中返回退出代码
- -f选项 ， 如果需要在输出到日志文件的同时，也可以查看日志文件的内容，可以使用 -f 参数。PS:可以用于教学,两个命令行接-f可以实时演示
- -q选项 ，可以使script命令以静默模式运行
- -t选项，指明输出录制的时间数据
- -V选项，输出script的版本信息，然后退出
- -h选项，输出script的help信息，然后退出

### sed

```sh
-n                #或者--quiet或者--silent，仅显示处理后的结果
-e script         #指定sed编辑命令
-i                #直接修改读取的文件内容，而不是输出到终端。
-f                 #直接将 sed 的动作写在一个文件内， -f filename 则可以运行 filename 内的 sed 动作；
-r                 #sed 的动作支持的是延伸型正规表示法的语法。(默认是基础正规表示法语法)

##
# function
# 流式文本编辑器
    a\ # 在当前行下面插入文本。
    i\ # 在当前行上面插入文本。
    c\ # 把选定的行改为新的文本。
    d\ # 删除，删除选择的行。
    p\ #列印，亦即将某个选择的数据印出。通常 p 会与参数 sed -n 一起运行～
    s\ #取代，可以直接进行取代的工作哩！通常这个 s 的动作可以搭配正规表示法！例如 1,20s/old/new/g 就是啦！

    #可以sed加文件名    sed ":a;N;s/\n//g;ta" a.txt
    #sed是按行处理文本数据的，每次处理一行数据后，都会在行尾自动添加trailing newline，其实就是行的分隔符即换行符。
```

例如：

```shell
#-d的使用：
echo -e "123\n234\n342\n" | sed '/^234$/d'    #删除“234”的行（整行删除）
echo -e "123\n234\n342\n" | sed 2d            #删除第二行

#替换空格
echo -e "123\n12\n23" | sed ":a;N;s/\n//g;ta"
# tr "\n" "" 就好了
#N是把下一行加入到当前的hold space模式空间里，使之进行后续处理，最后sed会默认打印hold space模式空间里的内容。也就是说，sed是可以处理多行数据的。
#:a和ta是配套使用，实现跳转功能。t是test测试的意思。
#另外，还有:a和ba的配套使用方式，也可以实现跳转功能。b是branch分支的意思。


#打印4-10行
sed -n '4,10p' file

# 仅匹配字符串
echo "abcde" | sed 's/a\(.*\)e/\1/g'
# bcd      (结果)
# \(...\) 表示仅匹配子串
# \1    表示子串


# 已匹配结果
echo 'qwer' | sed 's/\w\+/"&"/g'
# "qwer"

# 替换单引号 原因暂时没有查到，只找到说加$可以转义bash 
sed $'s/\'//g'
```

注意：sed后面可以不用三个斜杠，只要是三个相同的字符就行，这一点就比较神奇。

新的例子

```sh
# 打印文件以hhh开始的所有行
sed -n '/hhh/,\$p' $file
```

删除空行

```sh
sed '/^\s*$/d' $file
```

**选项**

- -e<script>或--expression=<script> 以选项中指定的script来处理输入的文本文件。
- -f<script文件>或--file=<script文件> 以选项中指定的script文件来处理输入的文本文件。
- -h或--help 显示帮助。
- -n或--quiet或--silent 仅显示script处理后的结果。
- -V或--version 显示版本信息。

### sed命令

```shell
a\ # 在当前行下面插入文本。
i\ # 在当前行上面插入文本。
c\ # 把选定的行改为新的文本。
d # 删除，删除选择的行。
D # 删除模板块的第一行。
s # 替换指定字符
h # 拷贝模板块的内容到内存中的缓冲区。
H # 追加模板块的内容到内存中的缓冲区。
g # 获得内存缓冲区的内容，并替代当前模板块中的文本。
G # 获得内存缓冲区的内容，并追加到当前模板块文本的后面。
l # 列表不能打印字符的清单。
n # 读取下一个输入行，用下一个命令处理新的行而不是用第一个命令。
N # 追加下一个输入行到模板块后面并在二者间嵌入一个新行，改变当前行号码。
p # 打印模板块的行。
P # (大写) 打印模板块的第一行。
q # 退出Sed。
b lable # 分支到脚本中带有标记的地方，如果分支不存在则分支到脚本的末尾。
r file # 从file中读行。
t label # if分支，从最后一行开始，条件一旦满足或者T，t命令，将导致分支到带有标号的命令处，或者到脚本的末尾。
T label # 错误分支，从最后一行开始，一旦发生错误或者T，t命令，将导致分支到带有标号的命令处，或者到脚本的末尾。
w file # 写并追加模板块到file末尾。  
W file # 写并追加模板块的第一行到file末尾。  
! # 表示后面的命令对所有没有被选定的行发生作用。  
= # 打印当前行号码。  
# # 把注释扩展到下一个换行符以前。  
```

#### sed替换标记

```shell
g # 表示行内全面替换。  
p # 表示打印行。  
w # 表示把行写入一个文件。  
x # 表示互换模板块中的文本和缓冲区中的文本。  
y # 表示把一个字符翻译为另外的字符（但是不用于正则表达式）
\1 # 子串匹配标记
& # 已匹配字符串标记
```

#### sed元字符集

```shell
^ # 匹配行开始，如：/^sed/匹配所有以sed开头的行。
$ # 匹配行结束，如：/sed$/匹配所有以sed结尾的行。
. # 匹配一个非换行符的任意字符，如：/s.d/匹配s后接一个任意字符，最后是d。
* # 匹配0个或多个字符，如：/*sed/匹配所有模板是一个或多个空格后紧跟sed的行。
[] # 匹配一个指定范围内的字符，如/[ss]ed/匹配sed和Sed。  
[^] # 匹配一个不在指定范围内的字符，如：/[^A-RT-Z]ed/匹配不包含A-R和T-Z的一个字母开头，紧跟ed的行。
\(..\) # 匹配子串，保存匹配的字符，如s/\(love\)able/\1rs，loveable被替换成lovers。
& # 保存搜索字符用来替换其他字符，如s/love/ **&** /，love这成 **love** 。
\< # 匹配单词的开始，如:/\<love/匹配包含以love开头的单词的行。
\> # 匹配单词的结束，如/love\>/匹配包含以love结尾的单词的行。
x\{m\} # 重复字符x，m次，如：/0\{5\}/匹配包含5个0的行。
x\{m,\} # 重复字符x，至少m次，如：/0\{5,\}/匹配至少有5个0的行。
x\{m,n\} # 重复字符x，至少m次，不多于n次，如：/0\{5,10\}/匹配5~10个0的行。  
```

### set

显示或者设置shell特性及shell变量

```shell
set    -e                #若指令传回值不等于0，则立即退出
    +e                #关闭上面那个，让原脚本继续执行 一般配套使用
    -- <args>        #设置参数 如 set -- h1 h2 ;echo $@,$#
                    #h1 h2,2

    -f                #取消使用通配符
```

> ​    -a 　标示已修改的变量，以供输出至环境变量。
> 　-b 　使被中止的后台程序立刻回报执行状态。
> 　-C 　转向所产生的文件无法覆盖已存在的文件。
> 　-d 　Shell预设会用杂凑表记忆使用过的指令，以加速指令的执行。使用-d参数可取消。
> 　-e 　若指令传回值不等于0，则立即退出shell。　　
> 　-f　 　取消使用通配符。
> 　-h 　自动记录函数的所在位置。
> 　-H Shell 　可利用"!"加<指令编号>的方式来执行history中记录的指令。
> 　-k 　指令所给的参数都会被视为此指令的环境变量。
> 　-l 　记录for循环的变量名称。
> 　-m 　使用监视模式。
> 　-n 　只读取指令，而不实际执行。
> 　-p 　启动优先顺序模式。
> 　-P 　启动-P参数后，执行指令时，会以实际的文件或目录来取代符号连接。
> 　-t 　执行完随后的指令，即退出shell。
> 　-u 　当执行时使用到未定义过的变量，则显示错误信息。
> 　-v 　显示shell所读取的输入值。
> 　-x 　执行指令后，会先显示该指令及所下的参数。
> 　+<参数> 　取消某个set曾启动的参数。

一些常见的的 Linux 系统信号。

```
信号    值        描述
1     SIGHUP    挂起进程
2     SIGINT    终止进程(ctrl+c)
3     SIGQUIT   停止进程
9     SIGKILL   无条件终止进程
15    SIGTERM   尽可能终止进程
17    SIGSTOP   无条件停止进程，但不是终止进程
18    SIGTSTP   停止或暂停进程，但不终止进程(ctrl+z)
19    SIGCONT   继续运行停止的进程
```

————————————————
原文链接：https://blog.csdn.net/qq_55723966/article/details/122304011

一些信号量

```
名称 默认动作 说明

SIGHUP 终止进程 终端线路挂断

SIGINT 终止进程 中断进程

SIGQUIT 建立CORE文件 终止进程，并且生成core文件

SIGILL 建立CORE文件 非法指令

SIGTRAP 建立CORE文件 跟踪自陷

SIGBUS 建立CORE文件 总线错误

SIGSEGV 建立CORE文件 段非法错误

SIGFPE 建立CORE文件 浮点异常

SIGIOT 建立CORE文件 执行I/O自陷

SIGKILL 终止进程 杀死进程

SIGPIPE 终止进程 向一个没有读进程的管道写数据

SIGALarm 终止进程 计时器到时

SIGTERM 终止进程 软件终止信号

SIGSTOP 停止进程 非终端来的停止信号

SIGTSTP 停止进程 终端来的停止信号

SIGCONT 忽略信号 继续执行一个停止的进程

SIGURG 忽略信号 I/O紧急信号

SIGIO 忽略信号 描述符上可以进行I/O

SIGCHLD 忽略信号 当子进程停止或退出时通知父进程

SIGTTOU 停止进程 后台进程写终端

SIGTTIN 停止进程 后台进程读终端

SIGXGPU 终止进程 CPU时限超时

SIGXFSZ 终止进程 文件长度过长

SIGWINCH 忽略信号 窗口大小发生变化

SIGPROF 终止进程 统计分布图用计时器到时

SIGUSR1 终止进程 用户定义信号1

SIGUSR2 终止进程 用户定义信号2

SIGVTALRM 终止进程 虚拟计时器到时

1) SIGHUP 本信号在用户终端连接(正常或非正常)结束时发出, 通常是在终端的控制进程结束时, 通知同一session内的各个作业, 这时它们与控制终端不再关联.

2) SIGINT 程序终止(interrupt)信号, 在用户键入INTR字符(通常是Ctrl-C)时发出

3) SIGQUIT 和SIGINT类似, 但由QUIT字符(通常是Ctrl-)来控制. 进程在因收到SIGQUIT退出时会产生core文件, 在这个意义上类似于一个程序错误信号.

4) SIGILL 执行了非法指令. 通常是因为可执行文件本身出现错误, 或者试图执行数据段. 堆栈溢出时也有可能产生这个信号.

5) SIGTRAP 由断点指令或其它trap指令产生. 由debugger使用.

6) SIGABRT 程序自己发现错误并调用abort时产生.

7) SIGIOT 在PDP-11上由iot指令产生, 在其它机器上和SIGABRT一样.

8) SIGBUS 非法地址, 包括内存地址对齐(alignment)出错. eg: 访问一个四个字长的整数, 但其地址不是4的倍数.

9) SIGFPE 在发生致命的算术运算错误时发出. 不仅包括浮点运算错误, 还包括溢出及除数为0等其它所有的算术的错误.

10) SIGKILL 用来立即结束程序的运行. 本信号不能被阻塞, 处理和忽略.

11) SIGUSR1 留给用户使用

12) SIGSEGV 试图访问未分配给自己的内存, 或试图往没有写权限的内存地址写数据.

13) SIGUSR2 留给用户使用

14) SIGPIPE Broken pipe

15) SIGALRM 时钟定时信号, 计算的是实际的时间或时钟时间. alarm函数使用该信号.

16) SIGTERM 程序结束(terminate)信号, 与SIGKILL不同的是该信号可以被阻塞和处理. 通常用来要求程序自己正常退出. shell命令kill缺省产生这个信号.

17) SIGCHLD 子进程结束时, 父进程会收到这个信号.

18) SIGCONT 让一个停止(stopped)的进程继续执行. 本信号不能被阻塞. 可以用一个handler来让程序在由stopped状态变为继续执行时完成特定的工作. 例如, 重新显示提示符.

作者：peerben
链接：https://www.jianshu.com/p/1a9ea7f4d46e
```

### seq

```tex
以指定增量从首数开始打印数字到尾数
    -f, --format=格式        使用printf 样式的浮点格式
    -s, --separator=字符串   使用指定字符串分隔数字（默认使用：\n）
    -w, --equal-width        在列前添加0 使得宽度相同
```

```shell
#%后面指定数字的位数 默认是%g，%3g那么数字位数不足部分是空格。
#seq -f"%3g" 9 11
9
10
11
```

### sort

```tex
对文本文件中所有行进行排序。
    -n, --numeric-sort             根据数字排序。
    -r, --reverse                  将结果倒序排列。
    -k, --key=KEYDEF               通过一个key排序；KEYDEF给出位置和类型。
```

### ss

查看本地连接

ss命令可以传递的参数：

- -t - 显示TCP端口
- -u - 显示UDP端口
- -n - 不解析主机名
- -l - 显示监听端口
- -p - 显示进程
- -4 - 仅显示IPv4的socket连接

### ssh

```shell
ssh-keygen -t rsa            #生成rsa秘钥
ssh-copy-id user@host        #复制公钥到需要的主机，或其它方式发送公钥过去改名为authorized_keys

#ssh远程登录并执行指令的时候，authorized里的command参数需要加上&/bin/bash保持登陆
#authorized_keys
command="ls -al & /bin/bash"

#更多可见 https://blog.csdn.net/alifrank/article/details/48241699
```

关于authorized_keys与authorized_keys2

authorized_keys vs authorized_keys2

In OpenSSH releases earlier than 3, the sshd man page said:

> The $HOME/.ssh/authorized_keys file lists the RSA keys that are permitted for RSA authentication in SSH protocols 1.3 and 1.5 Similarly, 
> 
> the $HOME/.ssh/authorized_keys2 file lists the DSA and RSA keys that are permitted for public key authentication (PubkeyAuthentication) in SSH protocol 2.0.

也就是说在ssh的3版本之前：

authorized_keys2多支持一个DSA加密算法

中文翻译：

在版本3之前的OpenSSH中，sshd手册页曾经说过：

> $ HOME / .ssh / authorized_keys文件列出了SSH协议1.3和1.5中允许进行RSA身份验证的RSA密钥。类似地，$ HOME / .ssh / authorized_keys2文件列出了允许进行公共密钥身份验证的DSA和RSA密钥（ SSH协议2.0中的PubkeyAuthentication）。

版本3 的[发行公告](http://marc.info/?l=openssh-unix-dev&m=100508718416162&w=2)指出已弃用authorized_keys2，并且所有密钥都应放在authorized_keys文件中。

实际使用过程中openssl 1.1.1的版本中即使只有一个authorized_keys2也可以使用的（其他版本未测试）

登陆日志查看：

```
/var/log/auth.log
/var/log/secure.log
```

其他

```
其他日志
/var/log/message  一般信息和系统信息
/var/log/secure  登陆信息
/var/log/maillog  mail记录
/var/log/utmp 
/var/log/wtmp    登陆记录信息（last命令即读取此日志或者 who /var/log/wtmp）
```

若需要登录执行指令

在公钥文件前加上

```
command="/bin/sh xxx.sh" $pub_key
```

关于rsa格式秘钥在高版本的生成

现在使用命令 ssh-keygen -t rsa  生成ssh，默认是以新的格式生成，id_rsa的第一行变成了“BEGIN OPENSSH PRIVATE KEY” 而不在是“BEGIN RSA PRIVATE KEY”，此时用来msyql、MongoDB，配置ssh登陆的话，可能会报 “Resource temporarily unavailable. Authentication by key (/Users/youname/.ssh/id_rsa) failed (Error -16). (Error #35)” 提示资源不可用，这就是id_rsa 格式不对造成的

解决方法（一）：

使用 ssh-keygen -m PEM -t rsa -b 4096 来生成

-m 参数指定密钥的格式，PEM（也就是RSA格式）是之前使用的旧格式

-b：指定密钥长度；

-e：读取openssh的私钥或者公钥文件；

-C：添加注释；

-f：指定用来保存密钥的文件名；

-i：读取未加密的ssh-v2兼容的私钥/公钥文件，然后在标准输出设备上显示openssh兼容的私钥/公钥；

-l：显示公钥文件的指纹数据；

-N：提供一个新密语；

-P：提供（旧）密语；

-q：静默模式；

-t：指定要创建的密钥类型
————————————————
原文链接：https://blog.csdn.net/lsp84ch80/article/details/87861990

### stdbuf

读取管道文件

```shell
-i    # 调整标准输入流缓冲区
-o    # 调整标准输出流缓冲区
-e    # 标准错误流缓冲区

L    # 行缓冲模式
```

### sudo

```shell
# /etc/sudoers
ALL    ALL=(ALL:ALL) ALL

# ALL        ALL=(ALL:ALL)         ALL
# username    host=(user:group)    cmd 多个cmd规则以逗号分隔
#             也可以仅写一个       设置免密，NOPASSWD:cmd
#                                设置禁止, !cmd


# The first ALL is the users allowed,    + % is group
# The second one is the hosts
# The third one is the user as you are running the command （root:root）user:group
# The last one is the commands allowed

# ALL 表示任何身份、主机、指令
```

### sz

下载终端文件到本地

### tac

跟cat相反

tac命令就是将文件反向输出，刚好和cat输出相反。

**语法格式：**tac [参数] [文件]

**常用参数：**

| -b        | 在行前而非行尾添加分隔标志     |
| --------- | ----------------- |
| -r        | 将分隔标志视作正则表达式来解析   |
| -s        | 使用指定字符串代替换行作为分隔标志 |
| --version | 显示版本信息并退出         |
| --help    | 显示此帮助信息并退出        |

**参考实例**

反向列出test.txt文件的内容：

```sh
[root@linuxcool ~]# cat test.txt 
hello world
hello linuxcool
hello linuxprobe
[root@linuxcool ~]# tac test.txt 
hello linuxprobe
hello linuxcool
hello world
```

### tail

```
显示指定文件的末尾若干行
    -n<N>或——line=<N>：输出文件的尾部N（N位数字）行内容
    -f    显示最新内容
```

### tar

```shell
tar
    -zcvf            #创建新包
    -zxvf            #解压包
    -tf                #查看包内文件列表

    -c                #或--create：建立新的备份文件
    -C                 #-C<目录>：切换工作目录，先进入指定目录再执行压缩/解压缩操作，
    -x                #或--extract或--get：从归档文件中提取文件，可以搭配-C（大写）在特定目录解开
    -z                #或--gzip或--ungzip：通过gzip指令压缩/解压缩文件，文件名最好为*.tar.gz
    -v                #或--verbose：显示指令执行过程
    -f                #-f<备份文件>或--file=<备份文件>：指定备份文件；
    --exclude '*.pyc'    #排除pyc后缀文件
    -d                #记录文件的差别；
    -r                #添加文件到已经压缩的文件；
    -u                #添加改变了和现有的文件到已经存在的压缩文件；
    -j                #通过bzip2指令压缩/解压缩文件，文件名最好为*.tar.bz2；
    -l                #文件系统边界设置；
    -k                #保留原有文件不覆盖；
    -m                #保留文件不被覆盖；
    -w                #确认压缩文件的正确性；
    -p或--same-permissions    #保留原来的文件权限与属性；
    -P或--absolute-names        #使用文件名的绝对路径，不移除文件名称前的“/”号；
    -N <日期格式> 或 --newer=<日期时间>    #只将较指定日期更新的文件保存到备份文件里；
    --remove-files    #归档/压缩之后删除源文件
```

关于报错：`file changed as we read it`

是因为在打包的过程中文件发生了变化，所以导致报错，但是打包依然进行并且有效。在使用tar命令时加上--warning=no-file-changed参数即可不输出报错。

### taskset

> taskset命令用于设置进程（或 线程）的处理器亲和性（Processor Affinity），可以将进程（或 线程）绑定到特定的一个 或 多个CPU上去执行，而不允许将进程（或 线程）调度到其他的CPU上。
> 
> 将进程绑定到指定的CPU上运行，这样可以避免大量的进程切换产生的无效时间。通过 taskset 命令可将某个进程与某个CPU核心绑定，使得其仅在与之绑定的CPU核心上运行。
> 
> 线程是最小的内核执行调度单元，因此，准确地说是将某个线程与某个CPU核心绑定，而非某个进程。
> 
> taskset命令是依据线程PID（TID）查询或设置线程的CPU亲和性（与哪个CPU核心绑定）。

常用参数

| 参数              | 作用                           |
| --------------- | ---------------------------- |
| -a, --all-tasks | 设置或检索所有任务（线程）的CPU相关性对于给定的PID |
| -c, --cpu-list  | 将掩码解释为处理器的数字列表               |
| -p, --pid       | 在现有PID上操作，不要启动新任务            |
| -V, --version   | 显示版本信息                       |
| -h, --help      | 显示帮助信息                       |

例子

```sh
[root@localhost ~]# ps -eLf | grep qemu
root       1389   1339   1389  0    3 14:48 pts/0    00:00:10 /usr/libexec/qemu-kvm -cpu SandyBridge -vnc 0.0.0.0:1 centos1708.img
root       1389   1339   1393  2    3 14:48 pts/0    00:00:36 /usr/libexec/qemu-kvm -cpu SandyBridge -vnc 0.0.0.0:1 centos1708.img
root       1389   1339   1395  0    3 14:48 pts/0    00:00:00 /usr/libexec/qemu-kvm -cpu SandyBridge -vnc 0.0.0.0:1 centos1708.img
root       2638   1409   2638  0    1 15:10 pts/1    00:00:00 grep --color=auto qemu
[root@localhost ~]# taskset -p 1393
pid 1393's current affinity mask: ff
[root@localhost ~]# taskset -p 1389
pid 1389's current affinity mask: ff
```

输出结构处理器亲和性掩码是ff，表示进程（或 线程）可以在Host上让任何一个CPU运行。查看进程（或 线程）允许允许CPU范围使用-c参数。由于我的Host CPU是4核2线程，因此有8颗逻辑CPU。

```sh
[root@localhost ~]# taskset -cp 1393
pid 1393's current affinity list: 0-7
[root@localhost ~]# taskset -cp 1389
pid 1389's current affinity list: 0-7
```

**更改具体某一进程（或 线程）CPU亲和性**

taskset -p  hexadecimal mask PID/LWP

上面1393号线程可以在0~7号CPU之间允许，现在设置掩码0x11（二进制0001 0001），表示可以在0~4号CPU上允许。

```sh
[root@localhost ~]# taskset -p 0x11  1393
pid 1393's current affinity mask: ff
pid 1393's new affinity mask: 11
[root@localhost ~]# taskset -p   1393
pid 1393's current affinity mask: 11
[root@localhost ~]# taskset -cp   1393
pid 1393's current affinity list: 0,4
```

**为具体某一进程（或 线程）CPU亲和性指定一组范围**

使用-c参数

```sh
[root@localhost ~]# taskset -cp 0,3  1393
pid 1393's current affinity list: 0,4
pid 1393's new affinity list: 0,3
[root@localhost ~]# taskset -cp   1393
pid 1393's current affinity list: 0,3
```

### tcpdump

一款sniffer工具，是Linux上的抓包工具，嗅探器

文字接口的封包抓取

```
-a：尝试将网络和广播地址转换成名称；
-c<数据包数目>：收到指定的数据包数目后，就停止进行倾倒操作；
-d：把编译过的数据包编码转换成可阅读的格式，并倾倒到标准输出；
-dd：把编译过的数据包编码转换成C语言的格式，并倾倒到标准输出；
-ddd：把编译过的数据包编码转换成十进制数字的格式，并倾倒到标准输出；
-e：在每列倾倒资料上显示连接层级的文件头；
-f：用数字显示网际网络地址；
-F<表达文件>：指定内含表达方式的文件；
-i<网络界面>：使用指定的网络截面送出数据包 如eth0；
-l：使用标准输出列的缓冲区；
-n：不把主机的网络地址转换成名字；
-N：不列出域名；
-O：不将数据包编码最佳化；
-p：不让网络界面进入混杂模式；
-q ：快速输出，仅列出少数的传输协议信息；
-r<数据包文件>：从指定的文件读取数据包数据；
-s<数据包大小>：设置每个数据包的大小；
-S：用绝对而非相对数值列出TCP关联数；
-t：在每列倾倒资料上不显示时间戳记；
-tt： 在每列倾倒资料上显示未经格式化的时间戳记；
-T<数据包类型>：强制将表达方式所指定的数据包转译成设置的数据包类型；
-v：详细显示指令执行过程；
-vv：更详细显示指令执行过程；
-x：用十六进制字码列出数据包资料；
-w<数据包文件>：把数据包数据写入指定的文件。
```

一个功能强大的命令行数据包分析器，它是通过监听服务器的网卡来获取数据包，所有通过网络访问的数据包都能获取到。它也提供了过滤器的功能，可以获取指定的网络、端口或协议的数据包

**-c** count

*count表示数量。抓取数据包的数量达到count后结束命令，如果不使用-c 参数，会不停的抓取数据包，直到手动停止*

**-C** file_size

*抓取数据包保存到文件时，通过该命令指定文件的大小。文件达到指定大小后，会创建一个在原文件名称后面加上序号的新文件，如：dump.txt，dump.txt1。file_size的单位是b*

**-D**

*列出服务器所有网卡。tcpdump默认监听的是编号最小的那个网卡，一般是eth0。在进行抓包时可以通过 -i 参数指定监听的网卡，any表示监听所有网卡*

**-i** interface

*指定监听的网卡名称，any表示监听所有的网卡*

**-n**

*输出结果中，不把ip转换成主机名（默认显示的是主机名）*

**-q**

*快速输出，只输出简要的数据包信息*

**-r** file

*从文件中获取数据包，不再从网络获取数据包*

**-t**

*不输出时间戳*

**-w** file

*将抓取的数据包保存到文件，-r 参数可以从文件中读取数据包*

**-W** filecount

*指定文件的数量，当文件滚动到指定数量后会从第一个文件开始覆盖*

除了以上参数，还有一些关键字可以用来进行条件过滤，常用关键字如下

**-host**

*过滤主机，如 tcpdump host 192.168.1.110 只抓取经过这个ip的数据包*

**-src**

*用来过滤请求来源方的参数，如：tcpdump src host 192.168.1.110* *只抓取从这个ip过来的数据包*

**-dst**

*用来过滤请求接收方的参数，如：tcpdump dst host 192.168.1.110* *只抓取发送到这个ip的数据包*

**-port**

*过滤端口，如：tcpdump port 8080* *只抓取经过8080端口的数据包*

**-net**

*过滤网络，如：tcpdump net 192.168 只抓取经过这个网段的数据包*

**-and、not、or**

*条件过滤，和字面意思一样。如：tcpdump net 192.168 and port 8080 抓取经过192.168网段并经过8080端口的数据包*

**数据包分析**

抓取的数据包格式如下

![img](https://pic3.zhimg.com/80/v2-a6db11797f41a179ada2d9041ce148a6_720w.jpg)

**20:17:43.496528**

*时间戳，时:分:秒.微秒*

**IP**

*网际网络协议的名称*

**180.101.49.12.http > iZbp14w0b2rs7i1400bjjmZ.42468180.101.49.12.http**

*请求发送方的ip和端口 > 请求接收方的ip和端口。端口有时会显示为某个网络协议，如http、ssh、mysql等*

**Flags [R]**

*flag标识和状态，可选的状态有： [S.] [.] [P.] [F.][R]*

**seq、ack、fin**

*表示tcp协议的3次握手和4次挥手的过程。seq表示请求的序列号，ack是回答的序列号，fin表示完成。这里显示的序列号是相对值，-S参数可以显示绝对值*

**win**

*表示当前窗口的可用大小*

**length**

*表示报文体的长度，从长度可以简单分析是否正确接收了请求*

通过以上结果只能做简单的分析，可以使用-w参数把数据包写入文件，文件中记录的数据包比命令行要详细的多。借助分析工具可以对文件进一步分析，这里推荐使用Wireshark，这个工具是开源的，开箱即用使用简单，这里不做详细介绍了

**常用的命令组合**

抓取8080端口的数据包

```text
tcpdump -i any port 8080 
```

抓取从192.168.1.110发送到192.168.1.111的数据包

```text
tcpdump -i any src host 192.168.1.110 and dst host 192.168.1.111
```

抓取192.168网段除了192.168.1.110的请求的数据包

```text
tcpdump -i any src net 192.168 and 'src host not 192.168.1.110'
```

抓取8080端口的数据包并写入dump.log文件中

```text
tcpdump -i any port 8080 -w dump.log
```

**注意事项**

1.tcpdump需要用管理员权限运行，可以用sudo命令或者root用户

2.抓取的数据包通过length字段只能做一些简单的判断，想要详细分析，需要借助数据包分析工具，如：Wireshark

### telnet

检测端口是否可通

使用

```
telnet [host|ip [port]]
```

### test

判断

```sh
test file -nt file2
```

- -nt    newer than    判断 file1 是否比 file2 新
- -ot    older than    判断 file1 是否比 file2 旧
- -ef    判断 file1 和 file2 是否为同一文件，可用在判断 hard link 的判定。即，判定两个文件是否指向同一个 inode

### time

统计给定命令所花费的总时间

**补充说明** DY

**time命令** 用于统计给定命令所花费的总时间。

**语法**

```shell
time(参数)
```

**参数**

指令：指定需要运行的额指令及其参数。

**实例**

当测试一个程序或比较不同算法时，执行时间是非常重要的，一个好的算法应该是用时最短的。所有类UNIX系统都包含time命令，使用这个命令可以统计时间消耗。例如：

```shell
[root@localhost ~]# time ls
anaconda-ks.cfg  install.log  install.log.syslog  satools  text

real    0m0.009s
user    0m0.002s
sys     0m0.007s
```

输出的信息分别显示了该命令所花费的real时间、user时间和sys时间。

- real时间是指挂钟时间，也就是命令开始执行到结束的时间。这个短时间包括其他进程所占用的时间片，和进程被阻塞时所花费的时间。
- user时间是指进程花费在用户模式中的CPU时间，这是唯一真正用于执行进程所花费的时间，其他进程和花费阻塞状态中的时间没有计算在内。
- sys时间是指花费在内核模式中的CPU时间，代表在内核中执系统调用所花费的时间，这也是真正由进程使用的CPU时间。

shell内建也有一个time命令，当运行time时候是调用的系统内建命令，应为系统内建的功能有限，所以需要时间其他功能需要使用time命令可执行二进制文件`/usr/bin/time`。

使用`-o`选项将执行时间写入到文件中：

```shell
/usr/bin/time -o outfile.txt ls
```

使用`-a`选项追加信息：

```shell
/usr/bin/time -a -o outfile.txt ls
```

使用`-f`选项格式化时间输出：

```shell
/usr/bin/time -f "time: %U" ls
```

`-f`选项后的参数：

| 参数   | 描述                                              |
| ---- | ----------------------------------------------- |
| `%E` | real时间，显示格式为[小时:]分钟:秒                           |
| `%U` | user时间。                                         |
| `%S` | sys时间。                                          |
| `%C` | 进行计时的命令名称和命令行参数。                                |
| `%D` | 进程非共享数据区域，以KB为单位。                               |
| `%x` | 命令退出状态。                                         |
| `%k` | 进程接收到的信号数量。                                     |
| `%w` | 进程被交换出主存的次数。                                    |
| `%Z` | 系统的页面大小，这是一个系统常量，不用系统中常量值也不同。                   |
| `%P` | 进程所获取的CPU时间百分百，这个值等于 `user+system` 时间除以总共的运行时间。 |
| `%K` | 进程的平均总内存使用量（data+stack+text），单位是 `KB`。          |
| `%w` | 进程主动进行上下文切换的次数，例如等待I/O操作完成。                     |
| `%c` | 进程被迫进行上下文切换的次数（由于时间片到期）。                        |

### top

```shell
top                #实时动态地查看系统的整体运行情况
    -b            #以批处理模式操作；
    -c            #显示完整的治命令；
    -d            #屏幕刷新间隔时间；
    -I            #忽略失效过程；
    -s            #保密模式；
    -S            #累积模式；
    -i            #-i<时间>：设置间隔时间；
    -u            #-u<用户名>：指定用户名；
    -p            #-p<进程号>：指定进程；
    -n            #-n<次数>：循环显示的次数。
```

### touch

```shell
touch -t '202110211245.23' te.txt    #指定时间的文件创建
```

### tr

```shell
#tr命令 可以对来自标准输入的字符进行替换、压缩和删除。
tr(选项)(参数)

    #选项
    -c    #或——complerment：取代所有不属于第一字符集的字符；
    -d    #或——delete：删除所有属于第一字符集的字符；
    -s    #或--squeeze-repeats：把连续重复的字符以单独一个字符表示；
    -t    #或--truncate-set1：先删除第一字符集较第二字符集多出的字符。

    #参数
    #字符集1：指定要转换或删除的原字符集。
        #当执行转换操作时，必须使用参数“字符集2”指定转换的目标字符集。
        #但执行删除操作时，不需要参数“字符集2”；
    #字符集2：指定要转换成的目标字符集。


#例如：
tr '\n' ' '            #换行替换为空格
tr -s '\n'            #删除重复的换行
```

例：

```shell
echo "HELLO WORLD" | tr 'A-Z' 'a-z'
hello world
```

### traceroute

Linux traceroute命令用于显示数据包到主机间的路径。

traceroute指令让你追踪网络数据包的路由途径，预设数据包大小是40Bytes，用户可另行设置。

**语法**

```
traceroute [-dFlnrvx][-f<存活数值>][-g<网关>...][-i<网络界面>][-m<存活数值>][-p<通信端口>][-s<来源地址>][-t<服务类型>][-w<超时秒数>][主机名称或IP地址][数据包大小]
```

**参数说明**：

- -d 使用Socket层级的排错功能。

- -T 使用tcp发送

- -U 使用UDP的port 33434 来进行侦测，只是默认设置

- -f<存活数值> 设置第一个检测数据包的存活数值TTL的大小。

- -F 设置勿离断位。

- -g<网关> 设置来源路由网关，最多可设置8个。

- -i<网络界面> 使用指定的网络界面送出数据包。

- -I 使用ICMP回应取代UDP资料信息。

- -m<存活数值> 设置检测数据包的最大存活数值TTL的大小。
  
  TTL表示最大跳数

- -n 直接使用IP地址而非主机名称。

- -p<通信端口> 设置UDP传输协议的通信端口。

- -r 忽略普通的Routing Table，直接将数据包送到远端主机上。

- -s<来源地址> 设置本地主机送出数据包的IP地址。

- -t<服务类型> 设置检测数据包的TOS数值。

- -v 详细显示指令的执行过程。

- -w<超时秒数> 设置等待远端主机回报的时间。

- -x 开启或关闭数据包的正确性检验。

**实例**

显示到达目的地的数据包路由

```
# traceroute www.google.com
traceroute: Warning: www.google.com has multiple addresses; using 66.249.89.99
traceroute to www.l.google.com (66.249.89.99), 30 hops max, 38 byte packets
1 192.168.0.1 (192.168.0.1) 0.653 ms 0.846 ms 0.200 ms
2 118.250.4.1 (118.250.4.1) 36.610 ms 58.438 ms 55.146 ms
3 222.247.28.177 (222.247.28.177) 54.809 ms 39.879 ms 19.186 ms
4 61.187.255.253 (61.187.255.253) 18.033 ms 49.699 ms 72.147 ms
5 61.137.2.177 (61.137.2.177) 32.912 ms 72.947 ms 41.809 ms
6 202.97.46.5 (202.97.46.5) 60.436 ms 25.527 ms 40.023 ms
7 202.97.35.69 (202.97.35.69) 40.049 ms 66.091 ms 44.358 ms
8 202.97.35.110 (202.97.35.110) 42.140 ms 70.913 ms 41.144 ms
9 202.97.35.14 (202.97.35.14) 116.929 ms 57.081 ms 60.336 ms
10 202.97.60.34 (202.97.60.34) 54.871 ms 69.302 ms 64.353 ms
11 * * *
12 209.85.255.80 (209.85.255.80) 95.954 ms 79.844 ms 76.052 ms
   MPLS Label=385825 CoS=5 TTL=1 S=0
13 209.85.249.195 (209.85.249.195) 118.687 ms 120.905 ms 113.936 ms
14 72.14.236.126 (72.14.236.126) 115.843 ms 137.109 ms 186.491 ms
15 nrt04s01-in-f99.1e100.net (66.249.89.99) 168.024 ms 140.551 ms 161.127 ms
```

### trap

指定在接收到信号之后将要采取的动作

```shell
trap "动作" "信号"

#例如，收到0信号执行exit 1
trap "exit 1" 0
```

### ulimit

限制系统最大打开文件数

### uname

```tex
打印当前系统相关信息
    -r或--release：显示操作系统的发行编号
```

### uniq

```tex
忽略重复的行
    -c, --count                在每行开头增加重复次数。
    -d, --repeated             所有邻近的重复行只被打印一次。输出出现次数大于1的内容
    -D                         所有邻近的重复行将全部打印。
    -u                            输出出现次数为1的内容
```

### umount

卸载已经加载的文件系统。利用设备名或挂载点都能umount文件系统，不过最好还是通过挂载点卸载，以免使用绑定挂载（一个设备，多个挂载点）时产生混乱。

```
语法
umount(选项)(参数)
选项
-a：卸除/etc/mtab中记录的所有文件系统；
-h：显示帮助；
-n：卸除时不要将信息存入/etc/mtab文件中；
-r：若无法成功卸除，则尝试以只读的方式重新挂入文件系统；
-t<文件系统类型>：仅卸除选项中所指定的文件系统；
-v：执行时显示详细的信息；
-V：显示版本信息。
参数
文件系统：指定要卸载的文件系统或者其对应的设备文件名。
```

延迟卸载（lazy unmount）会立即卸载目录树里的文件系统，等到设备不再繁忙时才清理所有相关资源。卸载可移动存储介质还可以用eject命令。下面这条命令会卸载[cd](http://man.linuxde.net/cd)并弹出CD：

```
eject /dev/cdrom      卸载并弹出CD 
```

### umask

[![Linux 命令大全](https://www.runoob.com/images/up.gif) Linux 命令大全](https://www.runoob.com/linux/linux-command-manual.html)

Linux umask命令指定在建立文件时预设的权限掩码。

umask可用来设定[权限掩码]。[权限掩码]是由3个八进制的数字所组成，将现有的存取权限减掉权限掩码后，即可产生建立文件时预设的权限。

**语法**

```
umask [-S][权限掩码]
```

**参数说明**：

-S 　以文字的方式来表示权限掩码。

**实例**

使用指令"umask"查看当前权限掩码，则输入下面的命令：

```
$ umask                         #获取当前权限掩码 
```

执行上面的指令后，输出信息如下：

```
0022
```

接下来，使用指令"mkdir"创建一个目录，并使用指令"ls"获取该目录的详细信息，输入命令如下：

```
$ mkdir test1                       #创建目录  
$ ls –d –l test1/                   #显示目录的详细信息  
```

执行上面的命令后，将显示新创建目录的详细信息，如下所示：

```
drwxr-xr-x 2 rootlocal rootlocal 4096 2011-9-19 21:46 test1/ 
```

注意：在上面的输出信息中，"drwxr-xr-x"="777-022=755"。

### uptime

```shell
#能够打印系统总共运行了多长时间和系统的平均负载。
#uptime命令可以显示的信息显示依次为：
#现在时间、系统已经运行了多长时间、目前有多少登陆用户、系统在过去的1分钟、5分钟和15分钟内的平均负载。
uptime -V    #显示uptime命令版本信息

#系统平均负载是指在特定时间间隔内运行队列中的平均进程数。
#每个CPU内核的当前活动进程数不大于3的话，那么系统的性能是良好的。
#如果每个CPU内核的任务数大于5，那么这台机器的性能有严重问题。
```

### useradd

常用的

```
useradd dy1 -m -s /bin/sh -d /home/dy1

-m自动建立用户目录

-c<备注>：加上备注文字。备注文字会保存在passwd的备注栏位中；
-d<登入目录>：指定用户登入时的启始目录；
-D：变更预设值；
-e<有效期限>：指定帐号的有效期限；
-f<缓冲天数>：指定在密码过期后多少天即关闭该帐号；
-g<群组>：指定用户所属的群组；
-G<群组>：指定用户所属的附加群组；
-m：自动建立用户的登入目录；
-M：不要自动建立用户的登入目录；
-n：取消建立以用户名称为名的群组；
-r：建立系统帐号；
-s<shell>：指定用户登入后所使用的shell；
-u<uid>：指定用户id。
```

### userdel

```
-f 强制删除  即使登陆
-r 删除时 删除所有相关文件
```

### watch

周期执行给定的指令

```sh
watch （选项） （参数）
```

选项

```
-n # 或--interval  watch缺省每2秒运行一下程序，可以用-n或-interval来指定间隔的时间。
-d # 或--differences  用-d或--differences 选项watch 会高亮显示变化的区域。 而-d=cumulative选项会把变动过的地方(不管最近的那次有没有变动)都高亮显示出来。
-t # 或-no-title  会关闭watch命令在顶部的时间间隔,命令，当前时间的输出。
-h, --help # 查看帮助文档
```

### wc

```tex
统计文件的字节数、字数、行数
    -c # 统计字节数，或--bytes或——chars：只显示Bytes数；。
    -l # 统计行数，或——lines：只显示列数；。
    -m # 统计字符数。这个标志不能与 -c 标志一起使用。
    -w # 统计字数，或——words：只显示字数。一个字被定义为由空白、跳格或换行字符分隔的字符串。
    -L # 打印最长行的长度。
```

### wget

从指定的URL下载文件。wget非常稳定，它在带宽很窄的情况下和不稳定网络中有很强的适应性，如果是由于网络的原因下载失败，wget会不断的尝试，直到整个文件下载完毕。如果是服务器打断下载过程，它会再次联到服务器上从停止的地方继续下载。这对从那些限定了链接时间的服务器上下载大文件非常有用。

wget支持HTTP，HTTPS和FTP协议，可以使用HTTP代理。所谓的自动下载是指，wget可以在用户退出系统的之后在后台执行。这意味这你可以登录系统，启动一个wget下载任务，然后退出系统，wget将在后台执行直到任务完成，相对于其它大部分浏览器在下载大量数据时需要用户一直的参与，这省去了极大的麻烦。

用于从网络上下载资源，没有指定目录，下载资源回默认为当前目录。wget虽然功能强大，但是使用起来还是比较简单：

1. **支持断点下传功能** 这一点，也是网络蚂蚁和FlashGet当年最大的卖点，现在，Wget也可以使用此功能，那些网络不是太好的用户可以放心了；
2. **同时支持FTP和HTTP下载方式** 尽管现在大部分软件可以使用HTTP方式下载，但是，有些时候，仍然需要使用FTP方式下载软件；
3. **支持代理服务器** 对安全强度很高的系统而言，一般不会将自己的系统直接暴露在互联网上，所以，支持代理是下载软件必须有的功能；
4. **设置方便简单** 可能，习惯图形界面的用户已经不是太习惯命令行了，但是，命令行在设置上其实有更多的优点，最少，鼠标可以少点很多次，也不要担心是否错点鼠标；
5. **程序小，完全免费** 程序小可以考虑不计，因为现在的硬盘实在太大了；完全免费就不得不考虑了，即使网络上有很多所谓的免费软件，但是，这些软件的广告却不是我们喜欢的。

**语法**

```vshell
wget [参数] [URL地址]
```

**选项**

```shell
启动参数：

-V, –-version 显示wget的版本后退出
-h, –-help 打印语法帮助
-b, –-background 启动后转入后台执行
-e, –-execute=COMMAND 执行 `.wgetrc’格式的命令，wgetrc格式参见/etc/wgetrc或~/.wgetrc

记录和输入文件参数：

-o, –-output-file=FILE 把记录写到FILE文件中
-a, –-append-output=FILE 把记录追加到FILE文件中
-d, –-debug 打印调试输出
-q, –-quiet 安静模式(没有输出)
-v, –-verbose 冗长模式(这是缺省设置)
-nv, –-non-verbose 关掉冗长模式，但不是安静模式
-i, –-input-file=FILE 下载在FILE文件中出现的URLs
-F, –-force-html 把输入文件当作HTML格式文件对待
-B, –-base=URL 将URL作为在-F -i参数指定的文件中出现的相对链接的前缀
–-sslcertfile=FILE 可选客户端证书
–-sslcertkey=KEYFILE 可选客户端证书的KEYFILE
–-egd-file=FILE 指定EGD socket的文件名

下载参数：

–-bind-address=ADDRESS 指定本地使用地址(主机名或IP，当本地有多个IP或名字时使用)
-t, –-tries=NUMBER 设定最大尝试链接次数(0 表示无限制).
-O –-output-document=FILE 把文档写到FILE文件中
-nc, –-no-clobber 不要覆盖存在的文件或使用.#前缀
-c, –-continue 接着下载没下载完的文件
–progress=TYPE 设定进程条标记
-N, –-timestamping 不要重新下载文件除非比本地文件新
-S, –-server-response 打印服务器的回应
–-spider 不下载任何东西
-T, –-timeout=SECONDS 设定响应超时的秒数
-w, –-wait=SECONDS 两次尝试之间间隔SECONDS秒
–waitretry=SECONDS 在重新链接之间等待1…SECONDS秒
–random-wait 在下载之间等待0…2*WAIT秒
-Y, –-proxy=on/off 打开或关闭代理
-Q, –-quota=NUMBER 设置下载的容量限制
–limit-rate=RATE 限定下载输率

目录参数：

-nd –-no-directories 不创建目录
-x, –-force-directories 强制创建目录
-nH, –-no-host-directories 不创建主机目录
-P, –-directory-prefix=PREFIX 将文件保存到目录 PREFIX/…
–cut-dirs=NUMBER 忽略 NUMBER层远程目录

HTTP 选项参数：

-–http-user=USER 设定HTTP用户名为 USER.
-–http-passwd=PASS 设定http密码为 PASS
-C, –-cache=on/off 允许/不允许服务器端的数据缓存 (一般情况下允许)
-E, –-html-extension 将所有text/html文档以.html扩展名保存
-–ignore-length 忽略 `Content-Length’头域
-–header=STRING 在headers中插入字符串 STRING
-–proxy-user=USER 设定代理的用户名为 USER
-–proxy-passwd=PASS 设定代理的密码为 PASS
-–referer=URL 在HTTP请求中包含 `Referer: URL’头
-s, –-save-headers 保存HTTP头到文件
-U, –-user-agent=AGENT 设定代理的名称为 AGENT而不是 Wget/VERSION
-–no-http-keep-alive 关闭 HTTP活动链接 (永远链接)
–-cookies=off 不使用 cookies
–-load-cookies=FILE 在开始会话前从文件 FILE中加载cookie
-–save-cookies=FILE 在会话结束后将 cookies保存到 FILE文件中

FTP 选项参数：

-nr, -–dont-remove-listing 不移走 `.listing’文件
-g, -–glob=on/off 打开或关闭文件名的 globbing机制
-–passive-ftp 使用被动传输模式 (缺省值).
-–active-ftp 使用主动传输模式
-–retr-symlinks 在递归的时候，将链接指向文件(而不是目录)

递归下载参数：

-r, -–recursive 递归下载－－慎用!
-l, -–level=NUMBER 最大递归深度 (inf 或 0 代表无穷)
–-delete-after 在现在完毕后局部删除文件
-k, –-convert-links 转换非相对链接为相对链接
-K, –-backup-converted 在转换文件X之前，将之备份为 X.orig
-m, –-mirror 等价于 -r -N -l inf -nr
-p, –-page-requisites 下载显示HTML文件的所有图片

递归下载中的包含和不包含(accept/reject)：

-A, –-accept=LIST 分号分隔的被接受扩展名的列表
-R, –-reject=LIST 分号分隔的不被接受的扩展名的列表
-D, –-domains=LIST 分号分隔的被接受域的列表
–-exclude-domains=LIST 分号分隔的不被接受的域的列表
–-follow-ftp 跟踪HTML文档中的FTP链接
–-follow-tags=LIST 分号分隔的被跟踪的HTML标签的列表
-G, –-ignore-tags=LIST 分号分隔的被忽略的HTML标签的列表
-H, –-span-hosts 当递归时转到外部主机
-L, –-relative 仅仅跟踪相对链接
-I, –-include-directories=LIST 允许目录的列表
-X, –-exclude-directories=LIST 不被包含目录的列表
-np, –-no-parent 不要追溯到父目录
wget -S –-spider url 不下载只显示过程


--limit-rate=300k    限制带宽为300k
```

### whereis

查找环境变量中的文件

- -l    列出whereis会去查询的几个目录
- -b    只找binary格式文件
- -m    只找在说明文件manual路径下文件
- -s    只找source来源文件
- -u    搜寻不在上述三个项目中的其他文件

### wireshark

图形接口封包的获取，与tcpdump的区别是tcpdump是文字接口封包获取

这玩意儿好像是一个软件

### xargs

> **xargs 命令** 是给其他命令传递参数的一个过滤器，也是组合多个命令的一个工具。它擅长将标准输入数据转换成命令行参数，xargs 能够处理管道或者 stdin 并将其转换成特定命令的命令参数。xargs 也可以将单行或多行文本输入转换为其他格式，例如多行变单行，单行变多行。xargs 的默认命令是 echo，空格是默认定界符。这意味着通过管道传递给 xargs 的输入将会包含换行和空白，不过通过 xargs 的处理，换行和空白将被空格取代。xargs 是构建单行命令的重要组件之一。

xargs（英文全拼： eXtended ARGuments）是给命令传递参数的一个过滤器，也是组合多个命令的一个工具。

xargs 可以将管道或标准输入（stdin）数据转换成命令行参数，也能够从文件的输出中读取数据。

xargs 也可以将单行或多行文本输入转换为其他格式，例如多行变单行，单行变多行。

xargs 默认的命令是 echo，这意味着通过管道传递给 xargs 的输入将会包含换行和空白，不过通过 xargs 的处理，换行和空白将被空格取代。

xargs 是一个强有力的命令，它能够捕获一个命令的输出，然后传递给另外一个命令。

之所以能用到这个命令，关键是由于很多命令不支持|管道来传递参数，而日常工作中有有这个必要，所以就有了 xargs 命令，例如：

```sh
find /sbin -perm +700 |ls -l       #这个命令是错误的
find /sbin -perm +700 |xargs ls -l   #这样才是正确的
```

- -n    num        指定每行num个输出，默认是无限制
- -d    xxx        以xxx为分隔符
- -a    file    从文件中读入作为stdin
- -e    flag    注意有的时候可能会是-E，flag必须是一个以空格分隔的标志，当xargs分析到含有flag这个标志的时候就停止。
- -p             当每次执行一个argument的时候询问一次用户。
- -t             表示先打印命令，然后再执行。
- -i 或者是-I，        这得看linux支持了，将xargs的每项名称，一般是一行一行赋值给 {}，可以用 {} 代替。
- -r no-run-if-empty     当xargs的输入为空的时候则停止xargs，不用再去执行了。
- -s num             命令行的最大字符数，指的是 xargs 后面那个命令的最大命令行字符数。
- -L num             从标准输入一次读取 num 行送给 command 命令。
- -l 同 -L。
- -x                 exit的意思，主要是配合-s使用。
- -P                 修改最大的进程数，默认是1，为0时候为as many as it can ，这个例子我没有想到，应该平时都用不到的吧

​        

xargs 结合 find 使用

用 rm 删除太多的文件时候，可能得到一个错误信息：**/bin/rm Argument list too long.** 用 xargs 去避免这个问题：

```
find . -type f -name "*.log" -print0 | xargs -0 rm -f
```

xargs -0 将 \0 作为定界符。

### yes

yes命令用于重复输出字符串（output a string repeatedly until killed）。这个命令可以帮你自动回答命令行提示，例如，进入一个含有多个文件的目录，执行 "yes | rm -i *"，所有的 rm: remove regular empty file `xxx'? 提示都会被自动回答 y。这在编写脚本程序的时候会很用处。yes命令还有另外一个用途，可以用来生成大的文本文件。（-i交互式）

参数

- i    会交互式询问

yes 后面直接跟单词或者字符表示一直输出这个



