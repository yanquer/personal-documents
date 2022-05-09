
## auditd

### auditd

> The Linux Audit Subsystem is a system to Collect information regarding events occurring on the system(s) ,Kernel events (syscall events), User events (audit-enabled programs)
> syslog记录的信息有限，主要目的是软件调试，跟踪和打印软件的运行状态，而audit的目的则不同，它是linux安全体系的重要组成部分，是一种“被动”的防御体系。在内核里有内核审计模块，记录系统中的各种动作和事件，比如系统调用，文件修改，执行的程序，系统登入登出和记录所有系统中所有的事件，它的主要目的是方便管理员根据日记审计系统是否允许有异常，是否有入侵等等，说穿了就是把和系统安全有关的事件记录下来。

**audit可以用来干什么**

> Watching file access
> Monitoring system calls
> Recording commands run by a user
> Recording security events
> Monitoring network access

**怎么开启audit**

> 首先内核需要打开CONFIG_AUDIT的配置，在打开了配置重新编译内核后，audit功能默认是关闭的，有两种方法在使能audit：
> 1)cmdline中加入audit= 1参数，如果这个参数设置为1，而且auditd没有运行，则审计日志会被写到/var/log/messages中。
> 2)使用守护进程auditd

---详见assets下Linux audit详解_whuzm08的专栏-CSDN博客_audit.pdf---

---或者https://blog.csdn.net/whuzm08/article/details/87267956 ---

**auditd** 

> auditd是Linux审计系统的用户空间组件，它负责将审计记录写入磁盘。
> 
> 查看日志使用ausearch或aureport实用程序完成。
> 
> 使用auditctl实用程序配置审核系统或加载规则。
> 
> 在auditd启动期间，/etc/audit/audit.rules 中的审计规则由auditctl读取并加载到内核中。
> 
> 或者还有一个 augenrules程序，读取/etc/audit/rules.d/中的规则并将其编译成audit.rules 审计规则文件中。
> 
> 审计守护进程本身 有一些配置选项可以让管理员进行自定义配置

**auditd相关工具与配置文件** 

> auditctl : 即时控制审计守护进程的行为的工具，比如如添加规则等等
> 
> aureport : 查看和生成审计报告的工具
> 
> ausearch : 查找审计事件的工具
> 
> auditspd : 转发事件通知给其他应用程序，而不是写入到审计日志文件中
> 
> autrace : 一个用于跟踪进程的命令
> 
> /etc/audit/auditd.conf : auditd工具的配置文件
> 
> /etc/audit/rules.d/audit.rules：包含审核规则的文件
> 
> /etc/audit/audit.rules : 记录审计规则的文件

下面我们来分析每个字段的含义：

**type=SYSCALL**

> 　　每条记录都是以type=”keyword“开头，SYSCALL表示这条记录是向内核的系统调用触发产生的。更详细的type值和解释可以参考：https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-Audit_Record_Types

**msg=audit(1523501777.709:4172989316)**

> 　　在audit(time_stamp:ID)格式中，记录时间戳，从1970年1月1日00:00:00到现在的时间，ID为记录中唯一的ID标识，同一个事件产生的ID是相同的，如上访问audit_test目录会触发产生三条日志，但是事件ID是相同的。

**arch=c000003e**

> 　　表示系统的CPU架构，这个十六进制表示”x86_64“，使用命令**ausearch -i --arch c000003e**可以打印出有这部分内容的audit.log中日志的解释。需要注意的是，使用ausearch来查询时，需要保证audit log中有这样的日志记录。

**syscall=257**

> 　　向内核的系统调用的类型，类型值为257，在/usr/include/asm/unistd_64.h中有定义，这里257表示openat，可以使用命令ausyscall来查询不同的数字对应的系统调用名称。或者使用ausyscall --dump命令来显示所有的系统调用。

```
 # ausyscall 257
openat
 # ausyscall --dump
Using x86_64 syscall table:
0 read
1 write
2 open

……
```

**success=yes**

> 　　表示系统调用成功与否

**exit=3**

> 　　系统调用结束时的返回码，可以使用如下命令来查看返回值为3的日志解释，不同的系统调用，返回值不同。

```
#ausearch --interpret --exit 3
```

**a0=ffffffffffffff9c a1=21e0550 a2=90800 a3=0**

> 　　为系统调用时的前四个arguments，这些arguments依赖于使用的系统调用，可以使用ausearch来查看解释（部分参数可以打印出数值具体的解释）。

**items=1**

> 　　表示跟在系统调用后，补充记录的个数。

**ppid=2354**

> 　　父进程ID，如bash的ID。

**pid=30729**

> 　　进程Id，即为ls进程的ID。我们通过ps来查询，可以看到bash的进程与ppid是对应的

```
linux-xdYUnA:/home/audit_test # ps -aux | grep bash
lbh       2354  0.0  0.0 115376  2100 pts/1    S+   Apr11   0:00 bash
root     12478  0.0  0.0 115888  2608 pts/0    Ss   Apr11   0:00 -bash
root     13329  0.1  0.0 115888  2612 pts/2    Ss   11:15   0:00 -bash
root     15531  0.0  0.0 112652   972 pts/2    S+   11:15   0:00 grep --color=auto bash
root     30707  0.0  0.0 115888  2632 pts/1    Ss   Apr11   0:00 -bash
```

#### 关于/etc/audit/auditd.conf的配置

| option                                                                               | res                                                                                                                                                                                                                                                                                                                                                                                                           |
|:------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| log_file =/var/log/audit/audit.log                                                   | 审计日志文件的完整路径。<br/>如果您配置守护进程向除默认/var/log/audit/外的目录中写日志文件时，一定要修改它上面的文件权限，<br/>使得只有根用户有读、写和执行权限。<br/>所有其他用户都不能访问这个目录或这个目录中的日志文件。                                                                                                                                                                                                                                                                                 |
| log_format = RAW                                                                     | 写日志时要使用的格式。<br/>当设置为RAW时，数据会以从内核中检索到的格式写到日志文件中。<br/>当设置为NOLOG时，数据不会写到日志文件中，<br/>但是如果用dispatcher选项指定了一个，则数据仍然会发送到审计事件调度程序中                                                                                                                                                                                                                                                                                     |
| log_group = root                                                                     | 日志所属组                                                                                                                                                                                                                                                                                                                                                                                                         |
| priority_boost = 4                                                                   | 审计应采用多少优先级推进守护进程。必须是非负数。0表示没有变化                                                                                                                                                                                                                                                                                                                                                                               |
| flush = INCREMENTAL                                                                  | 多长时间向日志文件中写一次数据。值可以是NONE、INCREMENTAL、DATA和SYNC之一。<br/>如果设置为NONE，则不需要做特殊努力来将数据 刷新到日志文件中。<br/>如果设置为INCREMENTAL，则用freq选项的值确定多长时间发生一次向磁盘的刷新。<br/>如果设置为DATA，则审计数据和日志文件一直是同步的。<br/>如果设置为SYNC，则每次写到日志文件时，数据和元数据是同步的。                                                                                                                                                                                                 |
| freq = 20                                                                            | 如果flush设置为INCREMETNAL，审计守护进程在写到日志文件中前从内核中接收的记录数                                                                                                                                                                                                                                                                                                                                                               |
| num_logs = 5                                                                         | max_log_file_action设置为ROTATE时要保存的日志文件数目。必须是0~99之间的数。<br/>如果设置为小于2，则不会循环日志。<br/>如果递增了日志文件的数目，就可能有必要递增/etc/audit/audit.rules中的内核backlog设置值，<br/>以便留出日志循环的时间。<br/>如果没有设 置num_logs值，它就默认为0，意味着从来不循环日志文件。<br/>当达到指定文件容量后会循环日志文件，但是只会保存一定数目的老文件，这个数目由num_logs参数指定。<br/>老文件的文件名将为audit.log.N，其中 N是一个数字。这个数字越大，则文件越老。                                                                                                 |
| disp_qos = lossy                                                                     | 控制调度程序与审计守护进程之间的通信类型。有效值为lossy和lossless。<br/>如果设置为lossy，若审计守护进程与调度程序之间的缓冲区已满 (缓冲区为128千字节)，<br/>则发送给调度程序的引入事件会被丢弃。然而，只要log_format没有设置为nolog，事件就仍然会写到磁盘中。<br/>如果设 置为lossless，则在向调度程序发送事件之前和将日志写到磁盘之前，调度程序会等待缓冲区有足够的空间。                                                                                                                                                                                          |
| dispatcher = /sbin/audispd                                                           | 当启动这个守护进程时，由审计守护进程自动启动程序。所有守护进程都传递给这个程序。<br/>可以用它来进一步定制报表或者以与您的自定义分析程序兼容的不同格式 产生它们。<br/>自定义程序的示例代码可以在/usr/share/doc/audit- /skeleton.c中找到。<br/>由于调度程序用根用户特权运行，因此使用这个选项时要极其小心。这个选项不是必需的。                                                                                                                                                                                                                       |
| name_format = NONE<br/>##name = mydomain                                             | 此选项控制计算机节点名如何插入到审计事件流中。它有如下的选择：none,  hostname, fqd, numeric, and user<br/>None意味着没有计算机名被插入到审计事件中。<br/>hostname通过gethostname系统调用返回的名称。<br/>fqd意味着它=以主机名和解决它与DNS的完全合格的域名，<br/>numeric类似于fqd除解决本机的IP地址，<br/>为了使用这个选项，你可能想要测试’hostname -i’或 ’domainname-i’返回一个数字地址,<br/>另外，此选项不如果DHCP的使用是因为你可以有不同的地址，在同一台机器上的时间推荐。<br/>用户是从名称选项中定义的字符串。默认值是没有                                                                    |
| max_log_file = 6                                                                     | 以兆字节表示的最大日志文件容量。当达到这个容量时，会执行max_log_file _action指定的动作                                                                                                                                                                                                                                                                                                                                                         |
| max_log_file_action = ROTATE                                                         | 当达到max_log_file的日志文件大小时采取的动作。<br/>值必须是IGNORE、SYSLOG、SUSPEND、ROTATE和KEEP_LOGS之 一。<br/>如果设置为IGNORE，则在日志文件达到max_log_file后不采取动作。<br/>如果设置为SYSLOG，则当达到文件容量时会向系统日志/var /log/messages中写入一条警告。<br/>如果设置为SUSPEND，则当达到文件容量后不会向日志文件写入审计消息。<br/>如果设置为ROTATE，则当达 到指定文件容量后会循环日志文件，但是只会保存一定数目的老文件，<br/>这个数目由num_logs参数指定。老文件的文件名将为audit.log.N，其中 N是一个数字。这个数字越大，则文件越老。<br/>如果设置为KEEP_LOGS，则会循环日志文件，但是会忽略num_logs参数，因此不会删除日志文件 |
| space_left = 75                                                                      | 以兆字节表示的磁盘空间数量。<br/>当达到这个水平时，会采取space_left_action参数中的动作                                                                                                                                                                                                                                                                                                                                                        |
| space_left_action = SYSLOG                                                           | 当磁盘空间量达到space_left中的值时，采取这个动作。<br/>有效值为IGNORE、SYSLOG、EMAIL、SUSPEND、SINGLE和 HALT。<br/>如果设置为IGNORE，则不采取动作。<br/>如果设置为SYSLOG，则向系统日志/var/log/messages写一条警告消息。 <br/>如果设置为EMAIL，则从action_mail_acct向这个地址发送一封电子邮件，并向/var/log/messages中写一条警告消息。<br/>如果设置为 SUSPEND，则不再向审计日志文件中写警告消息。<br/>如果设置为SINGLE，则系统将在单用户模式下。<br/>如果设置为SALT，则系统会关闭                                                                                   |
| action_mail_acct = root                                                              | 负责维护审计守护进程和日志的管理员的电子邮件地址。如果地址没有主机名，则假定主机名为本地地址，比如root。<br/>必须安装sendmail并配置为向指定电子邮件地址发送电子邮件                                                                                                                                                                                                                                                                                                                    |
| admin_space_left = 50                                                                | 以兆字节表示的磁盘空间数量。<br/>用这个选项设置比space_left_action更多的主动性动作，<br/>以防万一space_left_action没有让管理员释放任何磁盘空间。<br/>这个值应小于space_left_action。如果达到这个水平，则会采取admin_space_left_ action所指定的动作                                                                                                                                                                                                                                        |
| admin_space_left_action = SUSPEND                                                    | 当自由磁盘空间量达到admin_space_left指定的值时，则采取动作。<br/>有效值为IGNORE、SYSLOG、EMAIL、SUSPEND、SINGLE和HALT。<br/>与这些值关联的动作与space_left_action中的相同。                                                                                                                                                                                                                                                                                  |
| disk_full_action = SUSPEND                                                           | 如果含有这个审计文件的分区已满，则采取这个动作。<br/>可能值为IGNORE、SYSLOG、SUSPEND、SINGLE和HALT。与这些值关联的动作<br/>与space_left_action中的相同。                                                                                                                                                                                                                                                                                                      |
| disk_error_action = SUSPEND                                                          | 如果在写审计日志或循环日志文件时检测到错误时采取的动作。<br/>值必须是IGNORE、SYSLOG、SUSPEND、SINGLE和HALT之一。<br/>与这些值关的动作与space_left_action中的相同                                                                                                                                                                                                                                                                                                  |
| ##tcp_listen_port =                                                                  | 这是在范围1、65535，一个数字值，如果指定，原因auditd听在从远程系统审计记录相应的TCP端口。<br/>审计程序可能与tcp_wrappers。<br/>你可能想控制在hosts.allow入口访问和否认文件。                                                                                                                                                                                                                                                                                                |
| tcp_listen_queue = 5                                                                 | 这是一个数字值，这表明有多少等待（要求但UNAC接受）的连接是允许的。<br/>默认值是5。设置过小的可能导致连接被拒绝，如果太多主机开始在完全相同的时间，如电源故障后。                                                                                                                                                                                                                                                                                                                         |
| tcp_max_per_addr = 1<br/>##tcp_client_ports = 1024-65535<br/>tcp_client_max_idle = 0 | 这是一个数字值，该值表示一个地址允许有多少个并发连接。默认为1，最大为1024。<br/>设置过大可能会允许拒绝服务攻击的日志服务器。<br/>还要注意的是，内核内部有一个最大的，最终将防止这种即使auditd允许它通过配置。<br/>在大多数情况下，默认应该是足够除非写一个自定义的恢复脚本运行提出未发送事件。<br/>在这种情况下，您将增加的数量只有足够大，让它在过。                                                                                                                                                                                                                    |
| enable_krb5 = no                                                                     | 如果设置为“yes”，Kerberos 5将用于认证和加密。默认是“no”。                                                                                                                                                                                                                                                                                                                                                                        |
| krb5_principal = auditd                                                              | 这是这个服务器的主要。<br/>默认是“auditd”。鉴于这种默认情况下，服务器会寻找一个名为`auditd/hostname@EXAMPLE.COM`存储在/etc/audit/audit.key<br/>认证本身其中主机是服务器的主机名称，如DNS查找其IP地址返回。                                                                                                                                                                                                                                                                     |
| ##krb5_key_file = /etc/audit/audit.key                                               | 这个客户的主要负责人的位置。请注意，密钥文件必须由根和模式0400所拥有。默认的是/etc/audit/audit.key                                                                                                                                                                                                                                                                                                                                                 |

注意：auditd当max_action设置为rotate时，日志分隔具有延时性，且后缀数字最大的是最旧的log文件

    研究audit日志规则，本文为进程配置。
    
    # 审计日志文件的完整路径。如果您配置守护进程向除默认/var/log/audit/外的目录中写日志文件时，
    # 一定要修改它上面的文件权限，使得只有根用户有读、写和执行权限。所有其他用户都不能访问这个
    # 目录或这个目录中的日志文件。
    log_file =/var/log/audit/audit.log
    
    # 写日志时要使用的格式。当设置为RAW时，数据会以从内核中检索到的格式写到日志文件中。当设置
    # 为NOLOG时，数据不会写到日志文件中，但是如果用dispatcher选项指定了一个，则数据仍然会发送
    # 到审计事件调度程序中
    log_format = RAW
    
    # 日志所属组
    log_group = root
    
    # 审计应采用多少优先级推进守护进程。必须是非负数。0表示没有变化。
    priority_boost = 4
    
    # 多长时间向日志文件中写一次数据。值可以是NONE、INCREMENTAL、DATA和SYNC之一。如果设置为
    # NONE，则不需要做特殊努力来将数据 刷新到日志文件中。如果设置为INCREMENTAL，则用freq选项
    # 的值确定多长时间发生一次向磁盘的刷新。如果设置为DATA，则审计数据和日志文件一直是同步的。
    # 如果设置为SYNC，则每次写到日志文件时，数据和元数据是同步的。
    flush = INCREMENTAL
    
    # 如果flush设置为INCREMETNAL，审计守护进程在写到日志文件中前从内核中接收的记录数
    freq = 20
    
    #max_log_file_action设置为ROTATE时要保存的日志文件数目。必须是0~99之间的数。如果设置为小于2，
    # 则不会循环日志。如果递 增了日志文件的数目，就可能有必要递增/etc/audit/audit.rules中的内核
    # backlog设置值，以便留出日志循环的时间。如果没有设 置num_logs值，它就默认为0，意味着从来不循环日志文件。
    num_logs = 5
    
    # 控制调度程序与审计守护进程之间的通信类型。有效值为lossy和lossless。如果设置为lossy，
    # 若审计守护进程与调度程序之间的缓冲区已满 (缓冲区为128千字节)，则发送给调度程序的引入
    # 事件会被丢弃。然而，只要log_format没有设置为nolog，事件就仍然会写到磁盘中。如果设 置为lossless，
    # 则在向调度程序发送事件之前和将日志写到磁盘之前，调度程序会等待缓冲区有足够的空间。
    disp_qos = lossy
    
    # 当启动这个守护进程时，由审计守护进程自动启动程序。所有守护进程都传递给这个程序。可以用
    # 它来进一步定制报表或者以与您的自定义分析程序兼容的不同格式 产生它们。自定义程序的示例
    # 代码可以在/usr/share/doc/audit- /skeleton.c中找到。由于调度程序用根用户特权运行，因此使用
    # 这个选项时要极其小心。这个选项不是必需的。
    dispatcher = /sbin/audispd
    
    # 此选项控制计算机节点名如何插入到审计事件流中。它有如下的选择：none,  hostname, fqd, numeric, and user
    # None意味着没有计算机名被插入到审计事件中。hostname通过gethostname系统调用返回的名称。fqd意味着它=以主机名
    # 和解决它与DNS的完全合格的域名，numeric类似于fqd除解决本机的IP地址，为了使用这个选项，你可能想要测试’hostname -i’
    # 或 ’domainname-i’返回一个数字地址,另外，此选项不如果DHCP的使用是因为你可以有不同的地址，在同一台机器上的时间推荐。
    # 用户是从名称选项中定义的字符串。默认值是没有
    name_format = NONE
    
    ##name = mydomain
    # 以兆字节表示的最大日志文件容量。当达到这个容量时，会执行max_log_file _action指定的动作
    max_log_file = 6 
    
    # 当达到max_log_file的日志文件大小时采取的动作。值必须是IGNORE、SYSLOG、SUSPEND、ROTATE和KEEP_LOGS之 一。
    # 如果设置为IGNORE，则在日志文件达到max_log_file后不采取动作。如果设置为SYSLOG，则当达到文件容量时会向
    # 系统日志/var /log/messages中写入一条警告。如果设置为SUSPEND，则当达到文件容量后不会向日志文件写入审计
    # 消息。如果设置为ROTATE，则当达 到指定文件容量后会循环日志文件，但是只会保存一定数目的老文件，这个数目
    # 由num_logs参数指定。老文件的文件名将为audit.log.N，其中 N是一个数字。这个数字越大，则文件越老。如果设
    # 置为KEEP_LOGS，则会循环日志文件，但是会忽略num_logs参数，因此不会删除日志文件
    max_log_file_action = ROTATE
    
    # 以兆字节表示的磁盘空间数量。当达到这个水平时，会采取space_left_action参数中的动作
    space_left = 75
    
    # 当磁盘空间量达到space_left中的值时，采取这个动作。有效值为IGNORE、SYSLOG、EMAIL、SUSPEND、SINGLE和 HALT。
    # 如果设置为IGNORE，则不采取动作。如果设置为SYSLOG，则向系统日志/var/log/messages写一条警告消息。如果设置为 
    # EMAIL，则从action_mail_acct向这个地址发送一封电子邮件，并向/var/log/messages中写一条警告消息。如果设置为 
    # SUSPEND，则不再向审计日志文件中写警告消息。如果设置为SINGLE，则系统将在单用户模式下。如果设置为SALT，则系统会关闭。
    space_left_action = SYSLOG
    
    # 负责维护审计守护进程和日志的管理员的电子邮件地址。如果地址没有主机名，则假定主机名为本地地址，比如root。
    # 必须安装sendmail并配置为向指定电子邮件地址发送电子邮件。
    action_mail_acct = root
    
    # 以兆字节表示的磁盘空间数量。用这个选项设置比space_left_action更多的主动性动作，以防万一space_left_action没有让
    # 管理员释放任何磁盘空间。这个值应小于space_left_action。如果达到这个水平，则会采取admin_space_left_ action所指定的动作。
    admin_space_left = 50
    
    # 当自由磁盘空间量达到admin_space_left指定的值时，则采取动作。有效值为IGNORE、SYSLOG、EMAIL、SUSPEND、SINGLE和HALT。
    # 与这些值关联的动作与space_left_action中的相同。
    admin_space_left_action = SUSPEND
    
    # 如果含有这个审计文件的分区已满，则采取这个动作。可能值为IGNORE、SYSLOG、SUSPEND、SINGLE和HALT。与这些值关联的动作
    # 与space_left_action中的相同。
    disk_full_action = SUSPEND
    
    # 如果在写审计日志或循环日志文件时检测到错误时采取的动作。值必须是IGNORE、SYSLOG、SUSPEND、SINGLE和HALT之一。
    # 与这些值关的动作与space_left_action中的相同
    disk_error_action = SUSPEND
    
    # 这是在范围1、65535，一个数字值，如果指定，原因auditd听在从远程系统审计记录相应的TCP端口。审计程序可能与tcp_wrappers。
    # 你可能想控制在hosts.allow入口访问和否认文件。
    tcp_listen_port = 
    
    # 这是一个数字值，这表明有多少等待（要求但UNAC接受）的连接是允许的。默认值是5。设置过小的可能导致连接被拒绝，
    # 如果太多主机开始在完全相同的时间，如电源故障后。
    tcp_listen_queue = 5
    
    # 这是一个数字值，该值表示一个地址允许有多少个并发连接。默认为1，最大为1024。设置过大可能会允许拒绝服务攻击的日志服务器。
    # 还要注意的是，内核内部有一个最大的，最终将防止这种即使auditd允许它通过配置。在大多数情况下，默认应该是足够除非写一个
    # 自定义的恢复脚本运行提出未发送事件。在这种情况下，您将增加的数量只有足够大，让它在过。
    tcp_max_per_addr = 1
    ##tcp_client_ports = 1024-65535
    tcp_client_max_idle = 0
    
    # 如果设置为“yes”，Kerberos 5将用于认证和加密。默认是“no”。
    enable_krb5 = no
    
    # 这是这个服务器的主要。默认是“auditd”。鉴于这种默认情况下，服务器会寻找一个名为auditd/hostname@EXAMPLE.COM存储在/etc/audit/audit.key
    # 认证本身其中主机是服务器的主机名称，如DNS查找其IP地址返回。
    krb5_principal = auditd
    
    # 这个客户的主要负责人的位置。请注意，密钥文件必须由根和模式0400所拥有。默认的是/etc/audit/audit.key
    krb5_key_file = /etc/audit/audit.key


#### auditd的使用

##### 1、安装auditd服务

CentOS7系统默认安装了audit服务

    rpm -aq | grep audit
    rpm -ql audit



##### 2、配置audit.rules规则

默认情况下审计规则是空的

```javascript
/*查看规则*/
auditctl -l

/*查看命令帮助*/
auditctl -h
```



例如添加一条规则


    auditctl -w /data -p rwxa
    /*监控/data目录
    -w path : 指定要监控的路径
    -p : 指定触发审计的文件/目录的访问权限
    rwxa ： 指定的触发条件，r 读取权限，w 写入权限，x 执行权限，a 属性（attr）*/




##### 3、永久保存审计规则

    vi /etc/audit/rules.d/audit.rules
    例如将-w /data/ -p rwxa加入到最后一行
    service auditd restart
    auditctl -l



##### 4、审计效果

在/data/目录下生成一个文件或者修改文件，查看审计日志

    tail -f /var/log/audit/audit.log



##### 5、实现将audit日志通过rsyslog转发给日志服务器

###### 1）audit有rsyslog插件能实现转发到本地的rsyslog服务


    cd /etc/audisp/plugins.d/
    vi syslog.conf
    修改如下两项
    active = yes
    args = LOG_LOCAL0
    然后重启audit服务
    service auditd restart


###### 2)audit审计日志还会输出到/var/log/message文件中

如果需要禁止输出到/var/log/messages文件，可以修改rsyslog.conf配置项并重启rsyslog服务 

在如下位置加入local0.none来实现不输出到/var/log/messages中


    vi /etc/rsyslog.conf
    *.info;mail.none;authpriv.none;cron.none;local0.none    /var/log/messages
    最后一行添加日志服务器
    *.* @192.168.31.51
    保存退出
    service rsyslog restart



###### 3)效果验证 如下图所示，审计日志只输出到日志服务器，未打印到/var/log/messages中



### 系统日志

> 以下介绍的是20个位于/var/log/ 目录之下的日志文件。其中一些只有特定版本采用，如dpkg.log只能在基于Debian的系统中看到。
> 
> 1. **/var/log/messages** — 包括整体系统信息，其中也包含系统启动期间的日志。此外，mail，cron，daemon，kern和auth等内容也记录在var/log/messages日志中。
> 2. /**var/log/dmesg** — 包含内核缓冲信息（kernel ring buffer）。在系统启动时，会在屏幕上显示许多与硬件有关的信息。可以用dmesg查看它们。
> 3. **/var/log/auth.log** — 包含系统授权信息，包括用户登录和使用的权限机制等。
> 4. **/var/log/boot.log** — 包含系统启动时的日志。
> 5. **/var/log/daemon.log** — 包含各种系统后台守护进程日志信息。
> 6. **/var/log/dpkg.log** – 包括安装或dpkg命令清除软件包的日志。
> 7. **/var/log/kern.log** – 包含内核产生的日志，有助于在定制内核时解决问题。
> 8. **/var/log/lastlog** — 记录所有用户的最近信息。这不是一个ASCII文件，因此需要用lastlog命令查看内容。
> 9. **/var/log/maillog /var/log/mail.log** — 包含来着系统运行电子邮件服务器的日志信息。例如，sendmail日志信息就全部送到这个文件中。
> 10. **/var/log/user.log** — 记录所有等级用户信息的日志。
> 11. **/var/log/Xorg.x.log** — 来自X的日志信息。
> 12. **/var/log/alternatives.log** – 更新替代信息都记录在这个文件中。
> 13. **/var/log/btmp** – 记录所有失败登录信息。使用last命令可以查看btmp文件。例如，”last -f /var/log/btmp | more“。
> 14. **/var/log/cups** — 涉及所有打印信息的日志。
> 15. **/var/log/anaconda.log** — 在安装Linux时，所有安装信息都储存在这个文件中。
> 16. **/var/log/yum.log** — 包含使用yum安装的软件包信息。
> 17. **/var/log/cron** — 每当cron进程开始一个工作时，就会将相关信息记录在这个文件中。
> 18. **/var/log/secure** — 包含验证和授权方面信息。例如，sshd会将所有信息记录（其中包括失败登录）在这里。
> 19. **/var/log/wtmp或/var/log/utmp** — 包含登录信息。使用wtmp可以找出谁正在登陆进入系统，谁使用命令显示这个文件或信息等。
> 20. **/var/log/faillog** – 包含用户登录失败信息。此外，错误登录命令也会记录在本文件中。
> 
> 除了上述Log文件以外， /var/log还基于系统的具体应用包含以下一些子目录：
> 
> - /var/log/httpd/或/var/log/apache2 — 包含服务器access_log和error_log信息。
> - /var/log/lighttpd/ — 包含light HTTPD的access_log和error_log。
> - /var/log/mail/ – 这个子目录包含邮件服务器的额外日志。
> - /var/log/prelink/ — 包含.so文件被prelink修改的信息。
> - /var/log/audit/ — 包含被 Linux audit daemon储存的信息。
> - /var/log/samba/ – 包含由samba存储的信息。
> - /var/log/sa/ — 包含每日由sysstat软件包收集的sar文件。
> - /var/log/sssd/ – 用于守护进程安全服务。
> 
> 除了手动存档和清除这些日志文件以外，还可以使用logrotate在文件达到一定大小后自动删除。可以尝试用vi，tail，grep和less等命令查看这些日志文件。
