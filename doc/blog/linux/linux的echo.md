### echo and /bin/echo

echo 是shell内置命令

/bin/echo 是可执行文件

通常来说，内建命令会比外部命令执行得更快，执行外部命令时不但会触发磁盘 I/O，还需要 fork 出一个单独的进程来执行，执行完成后再退出。而执行内建命令相当于调用当前 Shell 进程的一个函数。

目前来说遇到的一些区别

```
/bin/echo 参数触发 Argument list too long的临界点是 131072

echo 暂时没测试到有限制
```

参考：

[Shell内建命令（内置命令）](http://c.biancheng.net/view/1136.html)

[内置的 echo 命令和 /bin/echo 有什么区别？](https://qa.1r1g.cn/unix/ask/11322671/)

[为什么有/bin/echo，我为什么要使用它？](https://ubuntuqa.com/article/1658.html)

[为什么echo是内置命令的shell？](https://ubuntuqa.com/article/1658.html)

