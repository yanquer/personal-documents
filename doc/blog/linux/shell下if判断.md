## if[]判断

```
str1 = str2　　　　　　当两个串有相同内容、长度时为真 
str1 != str2　　　　　 当串str1和str2不等时为真 
-n str1　　　　　　　 当串的长度大于0时为真(串非空) 
-z str1　　　　　　　 当串的长度为0时为真(空串) 
str1　　　　　　　　   当串str1为非空时为真
int1 -eq int2　　　　两数相等为真 
int1 -ne int2　　　　两数不等为真 
int1 -gt int2　　　　int1大于int2为真 
int1 -ge int2　　　　int1大于等于int2为真 
int1 -lt int2　　　　int1小于int2为真 
int1 -le int2　　　　int1小于等于int2为真

-r file　　　　　用户可读为真 
-w file　　　　　用户可写为真 
-x file　　　　　用户可执行为真 
-f file　　　　　文件为正规文件为真 
-d file　　　　　文件为目录为真 
-c file　　　　　文件为字符特殊文件为真 
-b file　　　　　文件为块特殊文件为真 
-s file　　　　　文件大小非0时为真   
-t file　　　　　当文件描述符(默认为1)指定的设备为终端时为真
-L file               文件存在符号链接为真
-e file            文件是否存在

-S file            存在 Socket 文件
-p file            存在且为 FIFO（pipe）文件

-a 　 　　　　　 与 
-o　　　　　　　 或 
!　　　　　　　　非
```

比较两个字符串是否相等的办法是

```
 if [ "$test"x = "test"x ]; then

  这里的关键有几点：

    1 使用单个等号

    2 注意到等号两边各有一个空格：这是unix shell的要求

    3 注意到"$test"x最后的x，这是特意安排的，因为当$test为空的时候，上面的表达式就变成了x = testx，显然是不相等的。而如果没有这个x，表达式就会报错：[: =: unary operator expected
```


