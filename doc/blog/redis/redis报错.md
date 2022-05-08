### redis

有遇到一个问题

```
connection 127.0.0.0:6379 refused
```

连接本地redis服务端失败

查到的主要就是服务端没有启动成功

可能是bind 还需要绑定本机ip：

```
bind    127.0.0.1,$ip
```

也可能是需要开始自动后台运行：daemonize（守护进程）

```
daemonize    yes
```

aof文件：记录redis数据的变动情况

如果是宕机，可能是aof（append only file）文件存在错误导致redis-server没有启动成功

需要执行

```
# 询问是否修复（交互命令）
redis-check-aof --fix aof文件名

# 报告aof文件错误
redis-check-aof aof文件名
```

