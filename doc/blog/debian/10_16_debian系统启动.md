## debian启动

UEFI ==》 加载引导程序 （一般情况）



#### 内核消息

在控制台上显示的内核错误信息，能够通过设置他们的阈值水平来配置。

```
dmesg -n3


错误级别值	错误级别名称		说明
0			KERN_EMERG		系统不可用
1			KERN_ALERT		行为必须被立即采取
2			KERN_CRIT		危险条件
3			KERN_ERR		错误条件
4			KERN_WARNING	警告条件
5			KERN_NOTICE		普通但重要的条件
6			KERN_INFO		信息提示
7			KERN_DEBUG		debug 级别的信息
```





#### 系统消息

在 `systemd` 下, 内核和系统的信息都通过日志服务 `systemd-journald.service` (又名 `journald`)来记录，放在"`/var/log/journal`"下的不变的二进制数据，或放在"`/run/log/journal/`"下的变化的二进制数据.这些二进制日志数据，可以通过 `journalctl`(1) 命令来访问。例如，你可以显示从最后一次启动以来的日志，按如下所示：

```
journalctl -b

操作										命令片段
查看从最后一次启动开始的系统服务和内核日志	"journalctl -b --system"
查看从最后一次启动开始的当前用户的服务日志	"journalctl -b --user"
查看从最后一次启动开始的 "$unit" 工作日志	"journalctl -b -u $unit"
查看从最后一次启动开始的 "$unit"的工作日志 ("tail -f" 式样)												"journalctl -b -u $unit -f"
```





`modinfo`(8) 程序显示 Linux 内核模块信息。

`lsmod`(8) 程序以好看的格式展示"`/proc/modules`"的内容,显示当前内核加载了哪些模块。