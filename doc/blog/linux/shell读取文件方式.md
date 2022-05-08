### while read line的使用

1。重定向
```sh
while read line

do

    …

done < file
```

read通过输入重定向，把file的第一行所有的内容赋值给变量line，循环体内的命令一般包含对变量line的处理；然后循环处理file的第二行、第三行。。。一直到file的最后一行。还记得while根据其后的命令退出状态来判断是否执行循环体吗？是的，read命令也有退出状态，当它从文件file中读到内容时，退出状态为0，循环继续进行；当read从文件中读完最后一行后，下次便没有内容可读了，此时read的退出状态为非0，所以循环才会退出。

2.使用管道：

```sh
command | while read line

do

  …

done
```

