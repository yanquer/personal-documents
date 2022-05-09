## 关于linux参数过长问题，

查看参数可以使用

```
xargs --show-limits
```

其中会有一个这个

```
Size of command buffer we are actually using: 131072
```

表示命令行单个参数长度不能超过 131072

实际测试 最大只能到 131071

```
/bin/echo `python -c "print '.'*131071"`
```

一些文章参考：

[python – 为什么subprocess.Popen参数长度限制...](http://www.cocoachina.com/articles/68156)

[Linux command line character limit](https://serverfault.com/questions/163371/linux-command-line-character-limit)

[【Linux】【编译相关】execvp: /bin/sh: Argument list too long问题处理小结](https://blog.csdn.net/qxhgd/article/details/115472297)

[What defines the maximum size for a command single argument?](https://unix.stackexchange.com/questions/120642/what-defines-the-maximum-size-for-a-command-single-argument)

[Unix / Linux: Maximum Character Length of Arguments In a Shell Command](https://www.cyberciti.biz/faq/linux-unix-arg_max-maximum-length-of-arguments/)

