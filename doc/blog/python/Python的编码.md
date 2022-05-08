## 关于Python的编码



### 1、字符编码

​	1）.为了处理英文字符，产生了ASCII码。

​	2）.为了处理中文字符，产生了GB2312。

​	3）.为了处理各国字符，产生了Unicode。

​	4）.为了提高Unicode存储和传输性能，产生了UTF-8，它是Unicode的一种实现形式。



>**encode和decode**
>
>讲解编码和解码之前，先来讲讲Unicode和utf-8的关系，推荐[这篇博客](http://flyer103.diandian.com/post/2014-03-09/40061199665)给大家。
>
>可以这样来理解：字符串是由字符构成，字符在计算机硬件中通过二进制形式存储，这种二进制形式就是编码。如果直接使用 “字符串↔️字符↔️二进制表示（编码）” ，会增加不同类型编码之间转换的复杂性。所以引入了一个抽象层，“字符串↔️字符↔️与存储无关的表示↔️二进制表示（编码）” ，这样，可以用一种与存储无关的形式表示字符，不同的编码之间转换时可以先转换到这个抽象层，然后再转换为其他编码形式。在这里，unicode 就是 “与存储无关的表示”，utf—8 就是 “二进制表示”。
>
>python2中字符串有两种表示形式，str和unicode。str可以理解为上面这段话中的二进制编码格式，unicode可以理解为抽象层。encode是编码，即从unicode格式到二进制的编码格式如utf-8、gb2312等。decode是解码，即从二进制编码格式到unicode编码格式。
>
>原文：https://www.cnblogs.com/jinhaolin/p/5128973.html





### 2、Python的字符编码

​	1）.Python2中默认的字符编码是ASCII码。

​	2）.Python2中字符串有str和unicode两种类型。str有各种编码的区别，unicode是没有编码的标准形式。

​	3）.Python2中可以直接查看到unicode的字节串。

​	4）.python3默认使用unicode编码，unicode字节串将被直接处理为中文显示出来。



### 3、decode()与encode()方法

​	decode()方法将其他编码字符转化为Unicode编码字符。
​	encode()方法将Unicode编码字符转化为其他编码字符。



python3一个新特性就是对文本和二进制做了更清晰的划分，文本是str，二进制是byte(\x01\x06...)

编码 encode：str --> byte

解码 decode：byte --> str







### 4、实际遇到的问题

​	win10下python2.7读取一个txt文本出现了乱码

​	最终解决方案有两个：

​	1.使用decode方法

```python
#text.txt是读取的文件内容，编码ANSI，实际应该是gb2312吧
with open("text.txt","r") as f:
    lines = f.readlines()			#将内容转换为数组
    for line in lines:
        print line.decode('gb2312')	#直接print line会报错，参数为原本的编码
```

​	decode函数的参数是本身的编码，表示以此编码解析为unicode



​	2.导入codecs模块

```python
#text.txt是读取的文件内容，编码ANSI，实际应该是gb2312吧
#codesc.open的encoding参数可以指定原文件的编码，读取写入就会自动转换
with codecs.open("text.txt","r",encoding="gb2312") as f:
    lines = f.readlines()			#将内容转换为数组
    for line in lines:
        print line
```



### 5、其他：

> 读文件时候asacll一直无法转换成功，使用json.dumps解决
>
> ```python
> >>> a='\xe6\x81\xb6\xe6\x84\x8f\xe8\xbd\xaf\xe4\xbb\xb6'
> >>> bb=json.dumps(a, encoding="UTF-8", ensure_ascii=False)
> >>> print(bb)
> ```
>



python字符串前面加u,r,b的含义：

u/U:表示unicode字符串
不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行unicode编码。
一般英文字符在使用各种编码下, 基本都可以正常解析, 所以一般不带u；但是中文, 必须表明所需编码, 否则一旦编码转换就会出现乱码。
建议所有编码方式采用utf8

r/R:非转义的原始字符串
与普通字符相比，其他相对特殊的字符，其中可能包含转义字符，即那些，反斜杠加上对应字母，表示对应的特殊含义的，比如最常见的”\n”表示换行，”\t”表示Tab等。而如果是以r开头，那么说明后面的字符，都是普通的字符了，即如果是“\n”那么表示一个反斜杠字符，一个字母n，而不是表示换行了。
以r开头的字符，常用于正则表达式，对应着re模块。

b:bytes
python3.x里默认的str是(py2.x里的)unicode, bytes是(py2.x)的str, b”“前缀代表的就是bytes
python2.x里, b前缀没什么具体意义， 只是为了兼容python3.x的这种写法


