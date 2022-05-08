### 使用



```sh
bt			#打印当前的堆栈信息 backtrace
```

常用模板

```
gdb exefile corefile -x script
gdb --core corefile exefile -x script
gbd -c corefile exefile -x script
gdb exefile corefile < script
```

前三者基本等价，最后一个不确定



常用选项

```
-nx / -n：不执行任何初始化文件里的命令。通常在处理所有的命令此选项和参数之后，GDB 会执行这些文件里的命令。
-quite / -silent / -q：“安静模式”，不打印介绍和版权信息。在批处理模式下也不打印。
-batch：以批处理模式运行。处理完所有命令文件后以 0 状态推出。批处理模式将在 GDB 作为过滤器运的时候很有用，例如下载和运行一个远程计算机上的程序。
-symbols <file> / -s <file>：从指定的文件中读取符号表。
-se <file>：从指定文件中读取符号表信息，并把它用在可执行文件中。
-core <file> / -c <file>：调试 core dump 的 core 文件， core dump 叫做核心转储，它是进程运行时在突然崩溃的那一刻的一个内存快照，操作系统在程序发生异
常而异常在进程内部又没有被捕获的情况下，会把进程此刻内存、寄存器状态、运行堆栈等信息转储保存在一个文件里。
-directory <directory> / -d <directory>：加入一个源文件的搜索路径。默认搜索路径是环境变量中的 PATH 所定义的路径。
-tty device / -t device：将设备作为程序的标准输入输出。
-tui：在启动时激活文本用户接口。文本用户接口在终端上管理多种文本窗口，用来显示代码，汇编，寄存器和 GDB 命令的输出。
-write：以可读可写的方式打开可执行程序和 core 文件，和 set write on 命令相同。
-statistics：在每次完成命令和回收到提示符的时候，此选项可让 GDB 打印时间和内存使用统计信息。
-version：此选项可让 GDB 打印版本号和非保障性的声明然后退出
```



常用的command

```sh
run						#运行
info xxx				#显示xxx信息
bt						#显示堆栈
continue				#中断后继续运行到下一个断点
step					#单步执行，进入函数
next					#单步执行
return					#函数未执行完，忽略未执行的语句，返回。
finish					#函数执行完毕返回。
call					#调用某一个函数 fun("1234")
(backtrace)bt			#显示栈桢
bt N					#显示开头N个栈桢
bt -N					#显示最后N个栈桢
(frame)f N				#显示第N层栈桢
list					#显示源码
set directory			#设置gdb的工作目录
pwd						#当前的工作目录
```









### 关于gdb的core文件



- **Core Dump**：Core的意思是内存，Dump的意思是扔出来，堆出来。开发和使用Unix程序时，有时程序莫名其妙的down了，却没有任何的提示(有时候会提示core dumped)，这时候可以查看一下有没有形如core.进程号的文件生成，这个文件便是操作系统把程序down掉时的内存内容扔出来生成的, 它可以做为调试程序的参考
- **生成Core文件**

```
一般默认情况下，core file的大小被设置为了0，这样系统就不dump出core file了。修改后才能生成core文件。
#设置core大小为无限
ulimit -c unlimited
#设置文件大小为无限
ulimit unlimited

这些需要有root权限, 在ubuntu下每次重新打开中断都需要重新输入上面的第一条命令, 来设置core大小为无限

core文件生成路径:输入可执行文件运行命令的同一路径下。若系统生成的core文件不带其他任何扩展名称，则全部命名为core。新的core文件生成将覆盖原来的core文件。

1）/proc/sys/kernel/core_uses_pid可以控制core文件的文件名中是否添加pid作为扩展。文件内容为1，表示添加pid作为扩展名，生成的core文件格式为core.xxxx；为0则表示生成的core文件同一命名为core。
可通过以下命令修改此文件：
echo "1" > /proc/sys/kernel/core_uses_pid

2）proc/sys/kernel/core_pattern可以控制core文件保存位置和文件名格式。
可通过以下命令修改此文件：
echo "/corefile/core-%e-%p-%t" > core_pattern，可以将core文件统一生成到/corefile目录下，产生的文件名为core-命令名-pid-时间戳
以下是参数列表:
    %p - insert pid into filename 添加pid
    %u - insert current uid into filename 添加当前uid
    %g - insert current gid into filename 添加当前gid
    %s - insert signal that caused the coredump into the filename 添加导致产生core的信号
    %t - insert UNIX time that the coredump occurred into filename 添加core文件生成时的unix时间
    %h - insert hostname where the coredump happened into filename 添加主机名
    %e - insert coredumping executable name into filename 添加命令名
```

- **用gdb查看core文件**

```
发生core dump之后, 用gdb进行查看core文件的内容, 以定位文件中引发core dump的行.
gdb [exec file] [core file]
如:
gdb ./test core

或gdb ./a.out
 core-file core.xxxx
gdb后, 用bt命令backtrace或where查看程序运行到哪里, 来定位core dump的文件->行.

待调试的可执行文件，在编译的时候需要加-g，core文件才能正常显示出错信息

1）gdb -core=core.xxxx
file ./a.out
bt
2）gdb -c core.xxxx
file ./a.out
bt
```

- **用gdb实时观察某进程crash信息**

```
启动进程
gdb -p PID
c
运行进程至crash
gdb会显示crash信息
bt
```



总结为两种情况

​	1、进程意外死亡或者崩溃，在对 core 的限制不为0的情况下可发生 core dump 生成 core 文件

​		如需对当时的情况进行排查，则需执行：

```
gdb execfile corefile
```



​	2、跟踪已经存在的一个pid进行调试直至该pid崩溃

```
gdb -p pid
```









### Python使用gdb调试

启动有两种方式

1、交互式

```
$ gdb python
...
(gdb) run <programname>.py <arguments>
```

2、自动

```
$ gdb -ex r --args python <programname>.py <arguments>
```



调试

```sh
bt				#查看c调用堆栈
py-by			#查看python调用栈
info threads	#相关线程信息
py-list			#查看python代码运行到哪里
thread apply all py-list
				#查看所有进程的pyhton代码位置
```



python gdb extension在gdb的环境下提供了如下几个py-*命令

```
py-list        查看当前python应用程序上下文
py-bt          查看当前python应用程序调用堆栈
py-bt-full   查看当前python应用程序调用堆栈，并且显示每个frame的详细情况
py-print     查看python变量
py-locals   查看当前的scope的变量
py-up         查看上一个frame
py-down    查看下一个frame
```


