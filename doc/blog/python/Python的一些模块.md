
## Python的模块







### re（正则）



通过正则表达式对字符串进⾏匹配

r：在带有 `'r'` 前缀的字符串字面值中，反斜杠不必做任何特殊处理。 因此 `r"\n"` 表示包含 `'\'` 和 `'n'` 两个字符的字符串，而 `"\n"` 则表示只包含一个换行符的字符串。

#### **re.match函数**

语法：re.match(pattern, string, flags=0)

| 参数    | 含义                                                         |
| ------- | ------------------------------------------------------------ |
| pattern | 匹配的正则表达式                                             |
| string  | 要匹配的字符串                                               |
| flags   | 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。<br/><br/>1、re.I 忽略大小写<br/>2、re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境<br/>3、re.M 多行模式<br/>4、re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）<br/>5、re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库<br/>6、re.X 为了增加可读性，忽略空格和 # 后面的注释<br/> |



匹配单个字符

| 字符 | 功能                             | 位置                  |
| ---- | -------------------------------- | --------------------- |
| .    | 匹配任意1个字符（除了\n）        |                       |
| [ ]  | 匹配[ ]中列举的字符              |                       |
| \d   | 匹配数字，即0-9                  | 可以写在字符集[...]中 |
| \D   | 匹配⾮数字，即不是数字           | 可以写在字符集[...]中 |
| \s   | 匹配空⽩，即空格，tab键          | 可以写在字符集[...]中 |
| \S   | 匹配⾮空⽩字符                   | 可以写在字符集[...]中 |
| \w   | 匹配单词字符，即a-z、A-Z、0-9、_ | 可以写在字符集[...]中 |
| \W   | 匹配⾮单词字符                   | 可以写在字符集[...]中 |





#### re.compile 函数

compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

```python
prog = re.compile(pattern)
result = prog.match(string)
```

等价于

```python
result = re.match(pattern, string)
```



举例

```python

>>>import re
>>> pattern = re.compile(r'\d+')   
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
>>> print m                                         # 返回一个 Match 对象
<_sre.SRE_Match object at 0x10a42aac0>
>>> m.group(0)   # 可省略 0
'12'
>>> m.start(0)   # 可省略 0
3
>>> m.end(0)     # 可省略 0
5
>>> m.span(0)    # 可省略 0
(3, 5)
```

在上面，当匹配成功时返回一个 Match 对象，其中：

- group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
- start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
- end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
- span([group]) 方法返回 (start(group), end(group))





#### re.search函数

re.search 扫描整个字符串并返回第一个成功的匹配，如果没有匹配，就返回一个 None。

re.match与re.search的区别：re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配

举例：

```python
import re
ret = re.search(r"\d+", "阅读次数为9999")
print(ret.group())
#结果：9999
```





#### re.findall函数

在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。注意： match 和 search 是匹配一次 findall 匹配所有。

举例：

```python
import re
ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)
#结果：['9999', '7890', '12345']
```

举例2：

```python
import re
alist = ['a','b','c']
if re.findall('.$','dfghc')[0] in alist:
    print 'yes1'
if re.findall('.$','dfgh')[0] in alist:
    print 'yes2'
print 'over'
#输出：
#yes1
#over

#re.findall('.$','dfghc')其实是返回一个列表
#但是匹配是找出结尾的字符所以只有一个，使用[0]获取
#然后判断是否存在于alist
```





#### re.finditer函数

和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

```python
import re
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())

#结果：
#12
#32
#43
#3
```





#### re.sub函数

sub是substitute的所写，表示替换，将匹配到的数据进⾏替换。

语法：re.sub(pattern, repl, string, count=0, flags=0)

| 参数    | 描述                                                         |
| ------- | ------------------------------------------------------------ |
| pattern | 必选，表示正则中的模式字符串                                 |
| repl    | 必选，就是replacement，要替换的字符串，也可为一个函数        |
| string  | 必选，被替换的那个string字符串                               |
| count   | 可选参数，*count* 是要替换的最大次数，必须是非负整数。如果省略这个参数或设为 0，所有的匹配都会被替换 |
| flag    | 可选参数，标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等 |



举例：将匹配到的阅读次数加1

方法一：

```python
import re
ret = re.sub(r"\d+", '998', "python = 997")
print(ret)
```

结果：python = 998



方法二：

```python
import re
def add(temp):
    #int（）参数必须是字符串，类似字节的对象或数字，而不是“re.Match”
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)
ret = re.sub(r"\d+", add, "python = 997")
print(ret)
ret = re.sub(r"\d+", add, "python = 99")
print(ret)

#这里不懂是怎么把后面的参数传递过去的，
#好像python就是这样传递参数的？但是有尝试将temp打印，出来是一个地址好像，并不是预期的字符串
#理解是正常情况下传递的应该是整个字符串，但是这里使用了正则表达式匹配数字，所以只传递了数字，然后使用group函数来获取
#根据这个思路尝试了一下
#将匹配规则更改为"r".+",输出temp.group的值正常，temp为地址，re会将参数传递更改为地址传递
```

结果;

python = 998
python = 100





#### re.subn函数

行为与sub()相同，但是返回一个元组 (字符串, 替换次数)。

re.subn(pattern, repl, string[, count])

返回：(sub(repl, string[, count]), 替换次数)

```python
import re
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(re.subn(pattern, r'\2 \1', s))
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print(re.subn(pattern, func, s))
### output ###
# ('say i, world hello!', 2)
# ('I Say, Hello World!', 2)
```





#### re.split函数

根据匹配进⾏切割字符串，并返回⼀个列表。

re.split(pattern, string, maxsplit=0, flags=0)

| 参数     | 描述                                                |
| -------- | --------------------------------------------------- |
| pattern  | 匹配的正则表达式                                    |
| string   | 要匹配的字符串                                      |
| maxsplit | 分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数 |

举例：

```python
import re
ret = re.split(r":| ","info:xiaoZhang 33 shandong")
print(ret)
```

结果：['info', 'xiaoZhang', '33', 'shandong']





#### python贪婪和⾮贪婪

Python⾥数量词默认是贪婪的（在少数语⾔⾥也可能是默认⾮贪婪），总是尝试匹配尽可能多的字符；⾮贪婪则相反，总是尝试匹配尽可能少的字符。

例如：正则表达式”ab*”如果用于查找”abbbc”，将找到”abbb”。而如果使用非贪婪的数量词”ab*?”，将找到”a”。

注：我们一般使用非贪婪模式来提取。

在"*","?","+","{m,n}"后⾯加上？，使贪婪变成⾮贪婪。

举例1：

```python
import re

s="This is a number 234-235-22-423"

#正则表达式模式中使⽤到通配字，那它在从左到右的顺序求值时，会尽量“抓取”满⾜匹配最⻓字符串，在我们上⾯的例⼦⾥⾯，“.+”会从字符串的启始处抓取满⾜模式的最⻓字符，其中包括我们想得到的第⼀个整型字段的中的⼤部分，“\d+”只需⼀位字符就可以匹配，所以它匹配了数字“4”，⽽“.+”则匹配了从字符串起始到这个第⼀位数字4之前的所有字符

r=re.match(".+(\d+-\d+-\d+-\d+)",s)
print(r.group(1))

#⾮贪婪操作符“？”，这个操作符可以⽤在"*","+","?"的后⾯，要求正则匹配的越少越好
r=re.match(".+?(\d+-\d+-\d+-\d+)",s)
print(r.group(1))
```

结果：

4-235-22-423
234-235-22-423



举例2：

```python
>>> re.match(r"aa(\d+)","aa2343ddd").group(1)
'2343'
>>> re.match(r"aa(\d+?)","aa2343ddd").group(1)
'2'
>>> re.match(r"aa(\d+)ddd","aa2343ddd").group(1)
'2343'
>>> re.match(r"aa(\d+?)ddd","aa2343ddd").group(1)
'2343'
```



举例3：提取图片地址

```python
import re
test_str="<img data-original=https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973.jpg>"
ret = re.search(r"https://.*?.jpg", test_str)
print(ret.group())
```





#### r的作⽤

与大多数编程语言相同，正则表达式里使用”\”作为转义字符，这就可能造成反斜杠困扰。假如你需要匹配文本中的字符”\”，那么使用编程语言表示的正则表达式里将需要4个反斜杠”\\\\”：前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。Python里的原生字符串很好地解决了这个问题，Python中字符串前⾯加上 r 表示原⽣字符串。

（前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。）

```python
import re
mm = "c:\\a\\b\\c"
print(mm)#c:\a\b\c
ret = re.match("c:\\\\",mm).group()
print(ret)#c:\
ret = re.match("c:\\\\a",mm).group()
print(ret)#c:\a
ret = re.match(r"c:\\a",mm).group()
print(ret)#c:\a
ret = re.match(r"c:\a",mm).group()
print(ret)#AttributeError: 'NoneType' object has no attribute 'group'
```







### os



#### os.popen

>os.popen() 方法用于从一个命令打开一个管道。
>在Unix，Windows中有效



popen()方法语法格式如下：

```python
os.popen(command[, mode[, bufsize]])
```



**参数**

- command – 使用的命令。
- mode – 模式权限可以是 ‘r’(默认) 或 ‘w’。
- bufsize – 指明了文件需要的缓冲大小：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲（大概值，以字节为单位）。负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。如果没有改参数，使用系统的默认值。



**返回值**

返回一个文件描述符号为fd的打开的文件对象







**python调用Shell脚本，有两种方法：os.system()和os.popen(),**
**前者返回值是脚本的退出状态码，后者的返回值是脚本执行过程中的输出内容**





##### os.system(command)

>该方法在调用完shell脚本后，返回一个16位的二进制数，低位为杀死所调用脚本的信号号码，高位为脚本的退出状态码，即脚本中“exit 1”的代码执行后，os.system函数返回值的高位数则是1，如果低位数是0的情况下，则函数的返回值是0x0100,换算为十进制得到256。



要获得os.system的正确返回值，可以使用位移运算（将返回值右移8位）还原返回值：

```sh
>>> import os
>>> os.system("./test.sh")
hello python!
hello world!
256
>>> n=os.system("./test.sh")
hello python!
hello world!
>>> n
256
>>> n>>8
1
>>> 
```



##### os.popen(command)

> 这种调用方式是通过管道的方式来实现，函数返回一个file对象，里面的内容是脚本输出的内容（可简单理解为echo输出的内容），使用os.popen调用test.sh的情况：

```sh
>> import os
>>> os.popen("./test.sh")
<open file './test.sh', mode 'r' at 0x7f6cbbbee4b0>
>>> f=os.popen("./test.sh")
>>> f
<open file './test.sh', mode 'r' at 0x7f6cbbbee540>
>>> f.readlines()
['hello python!\n', 'hello world!\n']
>>> 
```



像调用”ls”这样的shell命令，应该使用popen的方法来获得内容，对比如下：

```sh
>>> import os
>>> os.system("ls")   #直接看到运行结果
Desktop    Downloads     Music     Public     Templates  Videos
Documents  examples.desktop  Pictures  systemExit.py  test.sh
0    #返回值为0，表示命令执行成功
>>> n=os.system('ls')
Desktop    Downloads     Music     Public     Templates  Videos
Documents  examples.desktop  Pictures  systemExit.py  test.sh
>>> n
0
>>> n>>8   #将返回值右移8位，得到正确的返回值
0
>>> f=os.popen('ls') #返回一个file对象，可以对这个文件对象进行相关的操作
>>> f
<open file 'ls', mode 'r' at 0x7f5303d124b0>
>>> f.readlines()
['Desktop\n', 'Documents\n', 'Downloads\n', 'examples.desktop\n', 'Music\n', 'Pictures\n', 'Public\n', 'systemExit.py\n', 'Templates\n', 'test.sh\n', 'Videos\n']
>>> 
```



知识点梳理

1．  返回值是文件对象

注意：返回值是文件对象，既然是文件对象，使用完就应该关闭，对吧？！不信网上搜一下，一大把文章提到这个os.popen都是忘记关闭文件对象的。 所以，推荐的写法是：

```sh
with os.popen(command, "r") as p:
    r = p.read()
```

至于with的用法就不多讲了，使用它，不需要显式的写p.close()。



2．  非阻塞

通俗的讲，非阻塞就是os.popen不会等cmd命令执行完毕就继续下面的代码了，不信？！看下面代码实例：

![1.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly91cGxvYWQtaW1hZ2VzLmppYW5zaHUuaW8vdXBsb2FkX2ltYWdlcy8xMjUwNDUwOC1lOTA2ODQ1Nzk4MjMwYjJi)

从上面实例可知，os.popen执行打开Uedit32.exe这个工具，但从实际执行结果看，Uedit32.exe还没打开，就直接进入了下一条语句，打印了“hello 小蟒社区”。在某些应用场景，可能这并不是你期望的行为，那如何让命令执行完后，再执行下一句呢？

处理方法是使用read()或readlines()对命令的执行结果进行读操作。



3．  完全阻塞

上面写了该函数是非阻塞的，现在怎么又变成完全阻塞的呢？感觉一头雾水了吧。本质上os.popen是非阻塞的，为了实现阻塞的效果，我们使用read()或readlines()对命令结果进行读，由此产生了阻塞的效果。但是，如果你的命令执行无法退出或进入交互模式，这种“读”将形成完全阻塞的情况，表现的像程序卡住了。

看下面代码实例1：

![2.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly91cGxvYWQtaW1hZ2VzLmppYW5zaHUuaW8vdXBsb2FkX2ltYWdlcy8xMjUwNDUwOC0xMzI5MGFiNmQxMjc5MDIz)

os.popen执行了ping  127.0.0.1  -t 该命令会一直执行，除非CTRL+C强制退出，因而，执行readlines读取命令输出时会造成卡住。

代码实例2：

使用os.popen执行sqlplus命令对数据库进行操作的场景，如果sqlplus执行失败，会进入交互模式，如图所示，此时使用readlines()读取执行结果时也会卡死，效果如上图：

![3.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly91cGxvYWQtaW1hZ2VzLmppYW5zaHUuaW8vdXBsb2FkX2ltYWdlcy8xMjUwNDUwOC1lZjczNjQzMjIyYjhhN2M3)

总结

os.popen()在大多数场景都是挺好用方便的，但是也有坑！！ 具体应用中，需要注意下。

建议：
1. 在需要读取命令执行结果时，避免在命令无法退出或进入交互模式的场景应用os.popen;
2. 2.os.popen()无法满足需求时，可以考虑subprocess.Popen();



##### 

##### 进程间通信



###### 管道 

一般是半双工，只能一端读，一端写



###### 缓冲I/O

分为：无缓冲，行缓冲，全缓冲

通过 read 和 write 系统调用直接读写文件，就是无缓冲模式，性能也最差。 而通过标准 I/O 库读写文件，就是缓冲模式，标准 I/O 库提供缓冲的目的是尽可能减少 read 和 write 调用的次数，提高性能。



行缓冲模式，当在输入输出中遇到换行符时，才进行实际 I/O 操作。

 全缓冲模式，当填满缓冲区时，才进行实际 I/O 操作。

管道和普通文件默认是全缓冲的，标准输入和标准输出默认是行缓冲的，标准错误默认是无缓冲的。



参考：

[深入理解子进程：Python 相关源码解析](http://www.python88.com/topic/2893)

[文件描述符作用](https://blog.csdn.net/dianqicyuyan/article/details/106357863)











#### os.path.basename()

函数作用：返回path最后的文件名（\之后的）

示例：

```python
path='D:\file\cat\dog.jpg'

print(os.path.basename(path))
```

结果：
dog.jpg 





#### os.fork()

创建子进程，返回一个非0的子进程id，

接下来的代码，主进程与子进程都会执行



> 程序中通过引入 os 模块，并调用其提供的 fork() 函数，程序中会拥有 2 个进程，其中父进程负责执行整个程序代码，而通过 fork() 函数创建出的子进程，会从创建位置开始，执行后续所有的程序（包含创建子进程的代码）。



例子：

```python
import os
print('父进程 ID =', os.getpid())
# 创建一个子进程，下面代码会被两个进程执行
pid = os.fork()
print('当前进程 ID =',os.getpid()," pid=",pid)
#根据 pid 值，分别为子进程和父进程布置任务
if pid == 0:
    print('子进程, ID=',os.getpid()," 父进程 ID=",os.getppid())
else:
    print('父进程, ID=',os.getpid()," pid=",pid)
```



结果：

```
父进程 ID = 2884
当前进程 ID = 2884 pid= 2885
父进程, ID= 2884 pid= 2885
当前进程 ID = 2885 pid= 0
子进程, ID= 2885 父进程 ID= 2884
```



参考：

[Python os.fork()方法：创建新进程](http://c.biancheng.net/view/2631.html)





#### os.pipe()

创建一个管道，返回 r,w 文件描述符，用于进程间通信







### commands



commands，好像python3.x改了吧，在3.9里没有找到

> 模块内部使用os.popen()执行shell脚本
>
> 返回status，output



例子：（摘自源码）

```sh
#python3.x改了，移除了，在3.9里没有找到
#我就懒得敲了

#python commands模块在python3.x被subprocess取代，见下，见上
>>> subprocess.getstatusoutput('pwd')
(0, '/home/ronny')
>>> subprocess.getoutput('pwd')
'/home/ronny'
```







### subprocess



#### (1) call

执行命令，返回状态码(命令正常执行返回0，报错则返回1)

```sh
ret1=subprocess.call("ifconfig")
ret2=subprocess.call("ipconfig")　　　　#python3.5不是这样，依然会抛出异常导致无法对ret2赋值
print(ret1)     #0
print(ret2)     #1


ret = subprocess.call(["ls", "-l"], shell=False)    #shell为False的时候命令必须分开写
ret = subprocess.call("ls -l", shell=True)
```

#### (2) check_call

执行命令，如果执行成功则返回状态码0，否则抛异常

```sh
subprocess.check_call(["ls", "-l"])
subprocess.check_call("exit 1", shell=True)
```

#### (3) check_output

执行命令，如果执行成功则返回执行结果，否则抛异常

```sh
subprocess.check_output(["echo", "Hello World!"])
subprocess.check_output("exit 1", shell=True)
```

#### (4) subprocess.Popen(...)

用于执行复杂的系统命令

| 参数                  | 注释                                                         |
| --------------------- | ------------------------------------------------------------ |
| args                  | shell命令，可以是字符串或者序列类型（如：list，元组）        |
| bufsize               | 指定缓冲。0 无缓冲,1 行缓冲,其他 缓冲区大小,负值 系统缓冲    |
| stdin, stdout, stderr | 分别表示程序的标准输入、输出、错误句柄                       |
| preexec_fn            | 只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用 |
| close_sfs             | 在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。 |
| shell                 | 同上                                                         |
| cwd                   | 用于设置子进程的当前目录                                     |
| env                   | 用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。 |
| universal_newlines    | 不同系统的换行符不同，True -> 同意使用 \n                    |
| startupinfo           | 只在windows下有效，将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等 |
| createionflags        | 同上                                                         |

```sh
import subprocess
ret1 = subprocess.Popen(["mkdir","t1"])
ret2 = subprocess.Popen("mkdir t2", shell=True)
```

终端输入的命令分为两种：

1. 输入即可得到输出，如：ifconfig
2. 输入进行某环境，依赖再输入，如：python

```sh
import subprocess

obj = subprocess.Popen("mkdir t3", shell=True, cwd='/home/dev',)     #在cwd目录下执行命令
import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)")
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print(cmd_out)
print(cmd_error)
import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)")

out_error_list = obj.communicate()
print(out_error_list)
import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out_error_list = obj.communicate('print("hello")')
print(out_error_list)
```

 

 

### sys

##### sys.argv[]

> sys.argv[0]表示代码本身文件路径以及调用时的参数

​	sys.argv[]说白了就是一个从程序外部获取参数的桥梁，这个“外部”很关键，所以那些试图从代码来说明它作用的解释一直没看明白。因为我们从外部取得的参数可以是多个，所以获得的是一个列表（list)，也就是说sys.argv其实可以看作是一个列表，所以才能用[]提取其中的元素。其第一个元素是程序本身，随后才依次是外部给予的参数。

```python
sys.argv[num]		#调用时的第num个参数，0表示脚本本身
```







##### sys.modules

​	sys.modules是一个全局字典，该字典是python启动后就加载在内存中，每当导入新的模块，sys.modules都将记录这些模块。

​	字典sys.modules对于加载模块起到了缓冲的作用。当某个模块第一次导入，字典sys.modules将自动记录该模块。当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。





##### sys.getsizeof()

获取对象占用的内存大小







### timeit

看语句的执行时间

如：

```python
print(timeit.timeit('set([x for x in [1, 3, 5]])'))
print(timeit.timeit('set(x for x in [1, 3, 5])'))
```



源码，主要有两个方法

```python
def timeit(stmt="pass", setup="pass", timer=default_timer,
           number=default_number, globals=None):
    """Convenience function to create Timer object and call timeit method."""
    return Timer(stmt, setup, timer, globals).timeit(number)

def repeat(stmt="pass", setup="pass", timer=default_timer,
           repeat=default_repeat, number=default_number, globals=None):
    """Convenience function to create Timer object and call repeat method."""
    return Timer(stmt, setup, timer, globals).repeat(repeat, number)
```



参数解析：

- stmt	statement，需要计算的代码字符串。（本地测的时候，不支持外部的变量）
- setup	statement的前置执行，比如可以在这里import或者定义变量
- timer	默认是 default_timer = time.perf_counter ，使用的计时器
- number	指定执行的次数，默认是1000000（3.6的源码默认是100w）
- globals	执行的命名空间
- repeat	重复次数，3.6源码默认是3







### dis

看底层的调用，

官方释义为 字节码反汇编器



如：

```python
dis.dis('set([x for x in [1, 3, 5]])')
dis.dis('set(x for x in [1, 3, 5])')
```





### time



1. 在Python中，通常有这几种方式来表示时间：1）[时间戳](https://so.csdn.net/so/search?q=时间戳&spm=1001.2101.3001.7020) 2）格式化的时间字符串 3）元组（struct_time）共九个元素。由于Python的time模块实现主要调用C库，所以各个平台可能有所不同。
2. UTC（Coordinated Universal Time，世界协调时）亦即格林威治天文时间，世界标准时间。在中国为UTC+8。DST（Daylight Saving Time）即夏令时。
3. 时间戳（timestamp）的方式：通常来说，时间戳表示的是从**1970年1月1日00:00:00**开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。返回时间戳方式的函数主要有time()，clock()等。
4. 元组（struct_time）方式：struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()。下面列出这种方式元组中的几个元素：



| 索引（Index） | 属性（Attribute）         | 值（Values）       |
| :------------ | :------------------------ | :----------------- |
| 0             | tm_year（年）             | 比如2011           |
| 1             | tm_mon（月）              | 1 - 12             |
| 2             | tm_mday（日）             | 1 - 31             |
| 3             | tm_hour（时）             | 0 - 23             |
| 4             | tm_min（分）              | 0 - 59             |
| 5             | tm_sec（秒）              | 0 - 61             |
| 6             | tm_wday（weekday）        | 0 - 6（0表示周日） |
| 7             | tm_yday（一年中的第几天） | 1 - 366            |
| 8             | tm_isdst（是否是夏令时）  | 默认为-1           |





#### time.mktime()



将一个struct_time（元组形式的时间）转化为时间戳。

Python time mktime() 函数执行与gmtime(), localtime()相反的操作，它接收struct_time对象作为参数，返回用秒数来表示时间的浮点数。

如果输入的值不是一个合法的时间，将触发 OverflowError 或 ValueError。



mktime()方法语法：

```
time.mktime(t)
```



- t -- 结构化的时间或者完整的9位元组元素。



返回用秒数来表示时间的浮点数。



实例

```python
#!/usr/bin/python
import time

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime( t )
print "time.mktime(t) : %f" %  secs
print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))
```



结果

```python
time.mktime(t) : 1234915418.000000
asctime(localtime(secs)): Tue Feb 17 17:03:38 2009
```





#### time.time()

返回当前时间的时间戳（1970年开始的秒数）

时间戳（timestamp）的方式：通常来说，时间戳表示的是从**1970年1月1日00:00:00**开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。返回时间戳方式的函数主要有time()，clock()等。







#### time.localtime([secs])

将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。

```sh
>>> time.localtime()
time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=14, tm_min=14, tm_sec=50, tm_wday=3, tm_yday=125, tm_isdst=0)
>>> time.localtime(1304575584.1361799)
time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=14, tm_min=6, tm_sec=24, tm_wday=3, tm_yday=125, tm_isdst=0)
```



#### time.gmtime([secs])

和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。

```sh
>>>time.gmtime()
time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=6, tm_min=19, tm_sec=48, tm_wday=3, tm_yday=125, tm_isdst=0)
```





#### time.sleep(secs)

线程推迟指定的时间运行。单位为秒。



#### time.clock()

这个需要注意，在不同的系统上含义不同。

在UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间戳）。

而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。（实际上是以WIN32上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）



#### time.asctime([t])

把一个表示时间的元组或者struct_time表示为这种形式：**'Sun Jun 20 23:21:05 1993'**。如果没有参数，将会将time.localtime()作为参数传入。

```sh
>>> time.asctime()
'Thu May 5 14:55:43 2011'
```





#### time.ctime([secs])

把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。

如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。

```sh
>>> time.ctime()
'Thu May 5 14:58:09 2011'
>>> time.ctime(time.time())
'Thu May 5 14:58:39 2011'
>>> time.ctime(1304579615)
'Thu May 5 15:13:35 2011'
```





#### time.strftime(format[, t])

把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。

| 格式 | 含义                                                         | 备注 |
| :--- | :----------------------------------------------------------- | :--- |
| %a   | 本地（locale）简化星期名称                                   |      |
| %A   | 本地完整星期名称                                             |      |
| %b   | 本地简化月份名称                                             |      |
| %B   | 本地完整月份名称                                             |      |
| %c   | 本地相应的日期和时间表示                                     |      |
| %d   | 一个月中的第几天（01 - 31）                                  |      |
| %H   | 一天中的第几个小时（24小时制，00 - 23）                      |      |
| %I   | 第几个小时（12小时制，01 - 12）                              |      |
| %j   | 一年中的第几天（001 - 366）                                  |      |
| %m   | 月份（01 - 12）                                              |      |
| %M   | 分钟数（00 - 59）                                            |      |
| %p   | 本地am或者pm的相应符                                         | 一   |
| %S   | 秒（01 - 61）                                                | 二   |
| %U   | 一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。 | 三   |
| %w   | 一个星期中的第几天（0 - 6，0是星期天）                       | 三   |
| %W   | 和%U基本相同，不同的是%W以星期一为一个星期的开始。           |      |
| %x   | 本地相应日期                                                 |      |
| %X   | 本地相应时间                                                 |      |
| %y   | 去掉世纪的年份（00 - 99）                                    |      |
| %Y   | 完整的年份                                                   |      |
| %Z   | 时区的名字（如果不存在为空字符）                             |      |
| %%   | ‘%’字符                                                      |      |

**备注**：

1. “%p”只有与“%I”配合使用才有效果。
2. 文档中强调确实是0 - 61，而不是59，闰年秒占两秒（汗一个）。
3. 当使用strptime()函数时，只有当在这年中的周数和天数被确定的时候%U和%W才会被计算。

举个例子：

```sh
>>> time.strftime("%Y-%m-%d %X", time.localtime())
'2011-05-05 16:37:06'
```







#### time.strptime(string[, format])

把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。

```sh
>>> time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X')
time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6, tm_wday=3, tm_yday=125, tm_isdst=-1)
```

在这个函数中，format默认为：**"%a %b %d %H:%M:%S %Y"**。



总览

![image-20220124115250040](Python%E5%AD%A6%E4%B9%A0.assets/image-20220124115250040.png)





参考：

[python time模块](https://blog.csdn.net/you_are_my_dream/article/details/61616465)











### datetime

pass





### calender

pass







### fcntl

对文件操作控制



#### fcntl.fcntl(fd, cmd, arg)

fcntl()针对(文件)描述符提供控制.参数fd是被参数cmd操作(如下面的描述)的描述符.       

针对cmd的值,fcntl能够接受第三个参数（arg）



> fcntl函数有5种功能：
>
> 　1.复制一个现有的描述符（cmd=F_DUPFD）.
>
> 　2.获得／设置文件描述符标记(cmd=F_GETFD或F_SETFD).
>
> ​    3.获得／设置文件状态标记(cmd=F_GETFL或F_SETFL).
>
> ​    4.获得／设置异步I/O所有权(cmd=F_GETOWN或F_SETOWN).
>
> ​    5.获得／设置记录锁(cmd=F_GETLK,F_SETLK或F_SETLKW).



以下主要是linux的

cmd选项

> F_DUPFD   返回一个如下描述的(文件)描述符:               
>
> ​     　　  （1）最小的大于或等于arg的一个可用的描述符             
>
>   　　　 （2）与原始操作符一样的某对象的引用        
>
> ​      　　 （3）如果对象是文件(file)的话,返回一个新的描述符,这个描述符与arg共享相同的偏移量(offset)          
>
> 　　　　（4）相同的访问模式(读,写或读/写)             
>
> 　　　　（5）相同的文件状态标志(如:两个文件描述符共享相同的状态标志)               
>
> 　　　　（6）与新的文件描述符结合在一起的close-on-exec标志被设置成交叉式访问execve(2)的系统调用           
>
>  
>
> F_GETFD   取得与文件描述符fd联合close-on-exec标志,类似FD_CLOEXEC.如果返回值和FD_CLOEXEC进行与运算结果是0的话,文件保持交叉式访问exec(), 否则如果通过exec运行的话,文件将被关闭(arg被忽略)          
>
> 
>
> F_SETFD   设置close-on-exec旗标。该旗标以参数arg的FD_CLOEXEC位决定。           
>
> ​       
>
> F_GETFL   取得fd的文件状态标志,如同下面的描述一样(arg被忽略)            
>
> ​       
>
> F_SETFL   设置给arg描述符状态标志,可以更改的几个标志是：O_APPEND， O_NONBLOCK，O_SYNC和O_ASYNC。
>        
>
> F_GETOWN 取得当前正在接收SIGIO或者SIGURG信号的进程id或进程组id,进程组id返回成负值(arg被忽略)            
>
> ​       
>
> F_SETOWN 设置将接收SIGIO和SIGURG信号的进程id或进程组id,进程组id通过提供负值的arg来说明,否则,arg将被认为是进程id
>
> 
>
> 命令字(cmd)F_GETFL和F_SETFL的标志如下面的描述:      
>
> ​       O_NONBLOCK    非阻塞I/O;如果read(2)调用没有可读取的数据,或者如果write(2)操作将阻塞,read或write调用返回-1和EAGAIN错误
>
> ​	   O_APPEND       强制每次写(write)操作都添加在文件大的末尾,相当于open(2)的O_APPEND标志     
>
> ​       O_DIRECT       最小化或去掉reading和writing的缓存影响.系统将企图避免缓存你的读或写的数据.
>
> ​               					如果不能够避免缓存,那么它将最小化已经被缓存了的数 据造成的影响.如果这个标志用的不够好,将大大的降低性能           
>
> ​       O_ASYNC       当I/O可用的时候,允许SIGIO信号发送到进程组,例如:当有数据可以读的时候
>
>  注意：   在修改文件描述符标志或文件状态标志时必须谨慎，先要取得现在的标志值，然后按照希望修改它，最后设置新标志值。不能只是执行F_SETFD或F_SETFL命令，这样会关闭以前设置的标志位。





fcntl的返回值

> 与命令有关。如果出错，所有命令都返回－1，如果成功则返回某个其他值。
>
> 下列三个命令有特定返回值：
>
> F_DUPFD    返回新的文件描述符
>
> F_GETFD    返回相应标志
>
> F_GETFL或F_GETOWN    返回一个正的进程ID或负的进程组ID。





python的参数

fcntl模块：

```
flock() : flock(f, operation)
```

operation : 包括：
  	fcntl.LOCK_UN 解锁
 	 fcntl.LOCK_EX 排他锁
  	fcntl.LOCK_SH 共享锁
 	 fcntl.LOCK_NB 非阻塞锁

LOCK_SH 共享锁:所有进程没有写访问权限，即使是加锁进程也没有。所有进程有读访问权限。

LOCK_EX 排他锁:除加锁进程外其他进程没有对已加锁文件读写访问权限。

LOCK_NB 非阻塞锁:
如果指定此参数，函数不能获得文件锁就立即返回，否则，函数会等待获得文件锁。

LOCK_NB可以同LOCK_SH或LOCK_NB进行按位或（|）运算操作。 `fcnt.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)`







参考：

[Linux fcntl函数详解](https://www.cnblogs.com/xuyh/p/3273082.html)







### File



#### fileobject.fileno()

返回一个整型的文件描述符，用于底层操作系统的i/o操作





### subprocess模块



　通过调用：
$$
{\tt 
{subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec\_fn=None, close\_fds=False, shell=False, cwd=None, env=None, universal\_newlines=False, startupinfo=None, creationflags=0)}
}
$$

```python
subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
```

　　**创建并返回一个子进程**，并在这个进程中执行指定的程序。

　　实例化 Popen 可以通过许多参数详细定制子进程的环境，但是只有一个参数是必须的，即位置参数 *args* ，下面也会详细介绍剩余的具名参数。

**参数介绍：**

- ***args\***：要执行的命令或可执行文件的路径。一个由字符串组成的序列（通常是列表），列表的第一个元素是可执行程序的路径，剩下的是传给这个程序的参数，如果没有要传给这个程序的参数，args 参数可以仅仅是一个字符串。

- ***bufsize\***：控制 *stdin*, *stdout*, *stderr* 等参数指定的文件的缓冲，和打开文件的 open()函数中的参数 *bufsize* 含义相同。

  如果指定了bufsize参数作用就和内建函数open()一样：0表示不缓冲，1表示行缓冲，其他正数表示近似的缓冲区字节数，负数表示使用系统默认值。默认是0。

- ***executable\***：如果这个参数不是 None，将替代参数 args 作为可执行程序；

- ***stdin\***：指定子进程的标准输入；

- ***stdout\***：指定子进程的标准输出；

- ***stderr\***：指定子进程的标准错误输出；

　　对于 *stdin, stdout* 和 *stderr* 而言，如果他们是 None（默认情况），那么子进程使用和父进程相同的标准流文件。

　　父进程如果想要和子进程通过 communicate() 方法通信，对应的参数必须是 subprocess.PIPE（见下文例4）；

　　当然 *stdin, stdout* 和 *stderr* 也可以是已经打开的 file 对象，前提是以合理的方式打开，比如 *stdin* 对应的文件必须要可读等。　

- ***preexec_fn\***：默认是None，否则必须是一个函数或者可调用对象，在子进程中首先执行这个函数，然后再去执行为子进程指定的程序或Shell。
- ***close_fds\***：布尔型变量，为 True 时，在子进程执行前强制关闭所有除 stdin，stdout和stderr外的文件；
- ***shel\*l**：布尔型变量，明确要求使用shell运行程序，与参数 executable 一同指定子进程运行在什么 Shell 中——如果executable=None 而 shell=True，则使用 /bin/sh 来执行 args 指定的程序；也就是说，Python首先起一个shell，再用这个shell来解释指定运行的命令。
- ***cwd\***：代表路径的字符串，指定子进程运行的工作目录，要求这个目录必须存在；
- ***env\***：字典，键和值都是为子进程定义环境变量的字符串；
- ***universal_newline\***：布尔型变量，为 True 时，*stdout* 和 *stderr* 以通用换行（universal newline）模式打开，
- ***startupinfo\***：见下一个参数；
- ***creationfalgs\***：最后这两个参数是Windows中才有的参数，传递给Win32的CreateProcess API调用。



![image-20220215140104611](Python%E5%AD%A6%E4%B9%A0.assets/image-20220215140104611.png)

　　

同 Linux 中创建子进程类似，父进程创建完子进程后，并不会自动等待子进程执行，父进程在子进程之前推出将导致子进程成为孤儿进程，孤儿进程统一由 init 进程接管，负责其终止后的回收工作。

　　如果父进程在子进程之后终止，但子进程终止时父进程没有进行最后的回收工作，子进程残留的数据结构称为僵尸进程。大量僵尸进程将耗费系统资源，因此父进程及时等待和回收子进程是必要的，除非能够确认自己比子进程先终止，从而将回收工作过渡给 init 进程。

　　这个等待和回收子进程的操作就是wait()函数，下文中将会介绍。

例1：

　　创建一个子进程，然后执行一个简单的命令

```
>>> import subprocess
>>> p = subprocess.Popen('ls -l', shell=True)
>>> total 164
-rw-r--r--  1 root root   133 Jul  4 16:25 admin-openrc.sh
-rw-r--r--  1 root root   268 Jul 10 15:55 admin-openrc-v3.sh
...
>>> p.returncode
>>> p.wait()
0
>>> p.returncode
0
```

　　这里也可以使用 p = subprocess.Popen(['ls', '-cl']) 来创建子进程。

 

**Popen 对象的属性**



　　Popen创建的子进程有一些有用的属性，假设 p 是 Popen 创建的子进程，p 的属性包括：

1. 

```
p.pid
```

　　子进程的PID。

2. 

```
p.returncode
```

　　该属性表示子进程的返回状态，returncode可能有多重情况：

- None —— 子进程尚未结束；
- ==0 —— 子进程正常退出；
- \> 0—— 子进程异常退出，returncode对应于出错码；
- < 0—— 子进程被信号杀掉了。

3. 

```
p.stdin, p.stdout, p.stderr
```

　　子进程对应的一些初始文件，如果调用Popen()的时候对应的参数是subprocess.PIPE，则这里对应的属性是一个包裹了这个管道的 file 对象，

　　

**Popen 对象的方法**

1.

```
p.poll()
```

　　检查子进程  p 是否已经终止，返回 p.returncode 属性 (参考下文 Popen 对象的属性)；

2.

```
p.wait()
```

　　等待子进程 p 终止，返回 p.returncode 属性；

　　**注意：**

　　　　wait() 立即阻塞父进程，直到子进程结束！

3.

```
p.communicate(input=None)
```

　　和子进程 p 交流，将参数 *input* （字符串）中的数据发送到子进程的 stdin，同时从子进程的 stdout 和 stderr 读取数据，直到EOF。

　　**返回值：**

　　　　二元组 (stdoutdata, stderrdata) 分别表示从标准出和标准错误中读出的数据。

　　父进程调用 p.communicate() 和子进程通信有以下限制：

　　（1） 只能通过管道和子进程通信，也就是说，只有调用 Popen() 创建子进程的时候参数 stdin=subprocess.PIPE，才能通过 p.communicate(input) 向子进程的 stdin 发送数据；只有参数 stout 和 stderr 也都为 subprocess.PIPE ，才能通过p.communicate() 从子进程接收数据，否则接收到的二元组中，对应的位置是None。

　　（2）父进程从子进程读到的数据缓存在内存中，因此commucate()不适合与子进程交换过大的数据。

　　**注意：**

　　　　communicate() 立即阻塞父进程，直到子进程结束！

4.

```
p.send_signal(signal)
```

　　向子进程发送信号 *signal*；

5.

```
p.terminate()
```

　　终止子进程 p ，等于向子进程发送 SIGTERM 信号；

6.

```
p.kill()
```

　　杀死子进程 p ，等于向子进程发送 SIGKILL 信号；

 

**subprocess模块的其他方法**

1. 

```
subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
```

　　父进程直接创建子进程执行程序，然后等待子进程完成

　　**返回值：**

　　　　call() 返回子进程的 **退出状态** 即 child.returncode 属性；

2. 

```
subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
```

　　父进程直接创建子进程执行程序，然后等待子进程完成，具体可以使用的参数，参考上文 Popen 类的介绍。

　　**返回值：**

　　　　无论子进程是否成功，该函数都返回 0；但是　

　　如果子进程的退出状态不是0，check_call() 抛出异常 CalledProcessError，异常对象中包含了 child.returncode 对应的返回码。

例2：

　　check_call()正常与错误执行命令

```
>>> p ``=` `subprocess.check_call([``'ping'` `,``'-c'``, ``'2'``, ``'www.baidu.com'``])``PING www.a.shifen.com (``220.181``.``111.188``) ``56``(``84``) bytes of data.``64` `bytes ``from` `220.181``.``111.188``: icmp_seq``=``1` `ttl``=``42` `time``=``37.4` `ms``64` `bytes ``from` `220.181``.``111.188``: icmp_seq``=``2` `ttl``=``42` `time``=``37.3` `ms` `-``-``-` `www.a.shifen.com ping statistics ``-``-``-``2` `packets transmitted, ``2` `received, ``0``%` `packet loss, time ``1001ms``rtt ``min``/``avg``/``max``/``mdev ``=` `37.335``/``37.410``/``37.486``/``0.207` `ms``>>> ``print` `p``<strong>``0``<``/``strong>``>>> p ``=` `subprocess.check_call([``'ping'` `,``'-c'``, ``'4'``, ``'www.!@$#@!(*^.com'``])``ping: unknown host www.!@$``#@!(*^.com``Traceback (most recent call last):`` ``File` `"<stdin>"``, line ``1``, ``in` `<module>`` ``File` `"/usr/lib/python2.7/subprocess.py"``, line ``540``, ``in` `check_call``  ``raise` `CalledProcessError(retcode, cmd)``subprocess.<strong>CalledProcessError<``/``strong>: Command ``'['``ping``', '``-``c``', '``4``', '``www.!@$``#@!(*^.com']' returned non-zero exit status 2``>>> ``print` `p``<strong>``0``<``/``strong>
```

　　

3.

```
subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
```

　　父进程直接创建子进程执行程序，以**字符串**的形式返回子进程的输出。

　　**返回值：**

　　　　字符串形式的子进程的输出结果，但是，

　　如果子进程的 **退出状态** 不是0，那么抛出异常 CalledProcessError，异常对象中包含了 child.returncode 对应的返回码。

　　**注意：**

　　　　check_output() 的函数签名中没有参数 *stdout*，调用该方法时，子进程的输出默认就返回给父进程。

例3：

　　check_output() 调用的子进程正常与错误退出

```
>>> subprocess.check_output([``"echo"``, ``"Hello World!"``])``'Hello World!\n'` `>>> subprocess.check_output(``"exit 1"``, shell``=``True``)``Traceback (most recent call last):``  ``...``subprocess.CalledProcessError: Command ``'exit 1'` `returned non``-``zero exit status ``1
```

 

**注意：**

　　使用上面提到的三个方法：call()、check_call() 和 check_output() 时，尽量不要将参数 *stderr* 和 *stdout* 设置为 subprocess.PIPE，这几个函数默认都会等待子进程完成，子进程产生大量的输出数据如果造成管道堵塞，父进程再等待子进程完成可能造成死锁。

　　

**subprocess模块的其他属性**

```
subprocess.PIPE
```

　　调用本模块提供的若干函数时，作为 std* 参数的值，为标准流文件打开一个管道。

例4：

　　使用管道连接标准流文件

```
import` `subprocess``child1 ``=` `subprocess.Popen([``'ls'``, ``'-l'``], stdout``=``subprocess.PIPE)``child2 ``=` `subprocess.Popen([``'wc'``, ``'-l'``], stdin``=``child1.stdout, stdout``=``subprocess.PIPE)``out ``=` `child2.communicate()``child1.wait()``child2.wait()``print``(out)
```

　　这里将子进程 child1 的标准输出作为子进程 child2 的标准输入，父进程通过 communicate() 读取 child2 的标准输出后打印。

 

```python
subprocess.STDOUT
```

　　调用本模块提供的若干函数时，作为 stderr 参数的值，将子进程的标准错误输出打印到标准输出。

 

**subprocess模块定义的异常**

```python
exception subprocess.CalledProcessError
```

　　（1）什么时候可能抛出该异常：调用 check_call() 或 check_output() ，子进程的退出状态不为 0 时。

　　（2）该异常包含以下信息：

- returncode：子进程的退出状态；
- cmd：创建子进程时指定的命令；
- output：如果是调用 check_output() 时抛出的该异常，这里包含子进程的输出，否则该属性为None。

 

　　总结

　　本文介绍了Python subprocess的基本用法，使用 Popen 可以在Python进程中创建子进程，如果只对子进程的执行退出状态感兴趣，可以调用 subprocess.call() 函数，如果想通过异常处理机制解决子进程异常退出的情形，可以考虑使用 subprocess.check_call() 和 subprocess.check_output。如果希望获得子进程的输出，可以调用 subprocess.check_output()，但 Popen() 无疑是功能最强大的。

　　subprocess模块的缺陷在于默认提供的父子进程间通信手段有限，只有管道；同时创建的子进程专门用来执行外部的程序或命令。

　　Linux下进程间通信的手段很多，子进程也完全可能从创建之后继续调用



参考：

[python--subprocess.Popen()多进程](https://blog.csdn.net/liuyingying0418/article/details/100939697)





### mmap模块与mmap对象



mmap 模块提供“内存映射的文件对象”，mmap 对象可以用在使用 plain string 的地方，mmap 对象和 plain string 的区别是：

- mmap 对象不提供字符串对象的方法；
- mmap 对象是可变的，而 str 对象是不可变的
- mmap 对象同时对应于打开的文件，多态于一个Python file 对象

　　mmap 对象可以切片和索引，也可以为它的切片或索引赋值（因为 mmap 对象是可变的），为 mmap 对象的切片赋值时，赋值语句右值的长度必须和左值切片的长度相同。mmap 对象可以作为进程间通过文件进行 IPC 的一种替换手段。

 

**创建 mmap 对象**

```python
mmap(filedesc, length, tagname='') #windows
mmap(filedesc, length, flag=MAP_SHARED, prot=PROT_READ|PROT_WRITE) #Unix
```

　　创建并返回一个 mmap 对象，参数 filedesc 通常是由 f.fileno()获得的，这在Python文件系列中已经介绍过。

　　mmap 创建对象的含义是：将指定 fd 的前 *length* 字节映射到内存。

　　Windows中，可以通过参数tagname为一段内存映射指定名称，这样一个文件上面可以同时具有多个 mmap。windows中的内存映射都是可读可写的，同时在进程之间共享。

　　Unix平台上，参数 *flags* 的可选值包括：

　　　　mmap.MAP_PRIVATE：这段内存映射只有本进程可用；

　　　　mmap.MAP_SHARED：将内存映射和其他进程共享，所有映射了同一文件的进程，都能够看到其中一个所做的更改；

　　参数 prot 对应的取值包括：mmap.PROT_READ, mmap.PROT_WRITE 和 mmap.PROT_WRITE | mmap.PROT_READ。最后一者的含义是同时可读可写。

 

**mmap 对象的方法**

> m.close() 　关闭 m 对应的文件；
>
> m.find(str, start=0) 　从 start 下标开始，在 m 中从左往右寻找子串 str 最早出现的下标；
>
> m.flush([offset, n]) 　把 m 中从offset开始的n个字节刷到对应的文件中，参数 offset 要么同时指定，要么同时不指定；
>
> m.move(dstoff, srcoff, n) 　等于 m[dstoff:dstoff+n] = m[srcoff:srcoff+n]，把从 srcoff 开始的 n 个字节复制到从 dstoff 开始的n个字节，可能会覆盖重叠的部分。
>
> m.read(n) 　返回一个字符串，从 m 对应的文件中最多读取 n 个字节，将会把 m 对应文件的位置指针向后移动；
>
> m.read_byte() 　返回一个1字节长的字符串，从 m 对应的文件中读1个字节，要是已经到了EOF还调用 read_byte()，则抛出异常 ValueError；
>
> m.readline() 　返回一个字符串，从 m 对应文件的当前位置到下一个'\n'，当调用 readline() 时文件位于 EOF，则返回空字符串；
>
> m.resize(n) 　把 m 的长度改为 n，m 的长度和 m 对应文件的长度是独立的；
>
> m.seek(pos, how=0) 　同 file 对象的 seek 操作，改变 m 对应的文件的当前位置；
>
> m.size()　 返回 m 对应文件的长度（不是 m 对象的长度len(m)）；
>
> m.tell() 　返回 m 对应文件的当前位置；
>
> m.write(str) 　把 str 写到 m 对应文件的当前位置，如果从 m 对应文件的当前位置到 m 结尾剩余的空间不足len(str)，则抛出 *ValueError*；
>
> m.write_byte(byte) 　把1个字节（对应一个字符）写到 m 对应文件的当前位置，实际上 m.write_byte(ch) 等于 m.write(ch)。如果 m 对应文件的当前位置在 m 的结尾，也就是 m 对应文件的当前位置到 m 结尾剩余的空间不足1个字节，write() 抛出异常ValueError，而 write_byte() 什么都不做。
>
> ​	对于EOF的处理，write() 和 read_byte() 抛出异常 ValueError，而 write_byte() 和 read() 什么都不做。
>
> 例：
>
> ```python
> # process 1
> f = open('xxx', 'w')
> while True:
>  data = raw_input('Enter some text:')
>  f.seek(0)
>  f.write(data)
>  f.truncate()
>  f.flush()
> 
> # process 2
> import mmap, os, time
> m = mmap.mmap(os.open('xxx', os.O_RDWR), 1)
> last = None
> while True:
>  m.resize(m.size())
>  data = [:]
>  if data != last:
>      print data
>      last = data
>  time.sleep(5)
> ```
>
> ​	该例子中，process 1 等待用户输入新内容并将其写入到文件 xxx 中，process 2 直接将整个文件映射到内存对象 m，然后每隔5秒检查一下文件是否发生变化。


