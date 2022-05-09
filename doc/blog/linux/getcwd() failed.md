## 报错 getcwd() failed

```
sh: 0: getcwd() failed: No such file or directory
```

在一个不存在的目录上执行命令，会报上述错误， 这个目录是曾经存在，后来给删除了，但某些管理工具的命令还存在于这个目录下执行。会报上述错误

方法是 换目录