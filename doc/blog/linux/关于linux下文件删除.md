## 关于linux下文件的删除



文件被打开后会在当前文件下申请一个存放存在文件信息内容的交换空间，

而linux下进程存在的方式是：





没空写了，我先放在这里，明天我再来写





而linux下进程是以文件的形式存在的，所以如果你在某个会话打开了一个文件，那么在当前目录下`ls -al`可以看到存在一个以.swap结尾且前面以点加文件名的文件，这个就是打开之后存在于缓冲区



这时如果将原文件删除，这个交换区还是存在，

因为Linux的删除只是删除指向索引的文件，但是文件本身还是在那，并不会立刻删除，但是除非还有其他的硬链接，否则也是找不到的