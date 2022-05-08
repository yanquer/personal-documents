### Linux的一些内核参数

问题背景
execvp: /bin/sh: Argument list too long问题出现的两种情况：

1、make的时候，如编译Linux内核、驱动、Android版本等较长-I、-D选项的情况；
2、shell操作，涉及较多文件的情况，如删除大量文件时，直接用rm；

问题原因
1、错误来源于sysdeps/gnu/errlist.c文件中：

```
[ERR_REMAP (E2BIG)] = N_("Argument list too long"),  
```

可据此找到对应Linux内核中exec.c中返回E2BIG的地方，实际和ARG_MAX有很大关系。
2、参考APUE，ARG_MAX的值在运行时间不变的值，但值可能不确定。
ARG_MAX的值实际上和下面参数有关系：

```
 - MAX_ARG_STRLEN #单个字符串的最大大小
 - MAX_ARG_STRINGS #参数个数的限制
 - MAX_ARG_PAGES #分配给参数的最大页数
 - stack size #堆栈空间
 - ARG_MAX in limits.h #参数的最大长度
```

实际上，不同内核的版本也有区别。

几个命令执行情况的例子：

```
[qxhgd@localhost]getconf ARG_MAX
2897152
[qxhgd@localhost]ulimit -s
8192
[qxhgd@localhost]xargs --show-limits 
Your environment variables take up 4222 bytes
POSIX upper limit on argument length (this system): 2090882
POSIX smallest allowable upper limit on argument length (all systems): 4096
Maximum length of command we could actually use: 2086660
Size of command buffer we are actually using: 131072
```


原文链接：https://blog.csdn.net/qxhgd/article/details/115472297

