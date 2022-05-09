
## python的一些常识


### 1、python的单双引号

基本没有差别，混合使用可以减少转义

>```
>#包含单引号字符串
>my_str = 'I\'m a student'
>my_str = "I'm a student"
>
>#双引号
>my_str = "Jason said \"I like you\""
>my_str = 'Jason said "I like you"'
>```
>
>





### 2、文件读写模式

#### 读写模式

要了解文件读写模式，需要了解几种模式的区别，以及对应指针

r :  读取文件，若文件不存在则会报错

w:  写入文件，若文件不存在则会先创建再写入，会覆盖原文件

a :  写入文件，若文件不存在则会先创建再写入，但不会覆盖原文件，而是追加在文件末尾

rb,wb： 分别于r,w类似，但是用于读写二进制文件

r+ :  可读、可写，文件不存在也会报错，写操作时会覆盖

w+ :  可读，可写，文件不存在先创建，会覆盖

a+ : 可读、可写，文件不存在先创建，不会覆盖，追加在末尾





### 3、在linux使用py遇到的一些问题



#### pkg_resources.DistributionNotFound: pip==0.8.1

具体报错如下：

```
$ sudo pip install gevent-websocket

Traceback (most recent call last):  
File "/usr/local/bin/pip", line 5, in <module>
from pkg_resources import load_entry_point
File "/usr/lib/python2.7/dist-packages/pkg_resources.py", line 2675, in <module>
parse_requirements(__requires__), Environment()
File "/usr/lib/python2.7/dist-packages/pkg_resources.py", line 552, in resolve
raise DistributionNotFound(req)
pkg_resources.DistributionNotFound: pip==0.8.1
```

可以使用which pip查看一下命令的位置，然后vim查看一下，

会发现文件里是定死了版本号的，想办法改一下

可能是安装了多个pip版本或者pip管理包工具引起的

最终的解决方案：

```
which pip
# /usr/local/bin/pip
```

```
python -m pip install --upgrade --force pip==9		#这里我需要的是9版本的pip

cat /usr/local/bin/pip2.7 >/usr/local/bin/pip		#这里是which位置

which pip
# /usr/bin/local	这里因为我自己设置的原因有一个
ln -s /usr/local/bin/pip2.7 /usr/bin/local

##
#	源文件/usr/bin/local和/usr/local/bin/pip都限制死了pip版本，把正确的写进去
##
```





### 4、处理包依赖的问题

要知道package的依赖方案

可以直接看报错地方的源码的要求

也可以直接

```
apt-cache show $package
```



有些涉及到了系统的包没法操作的话

```
apt-get install aptitude
aptitude insatll $package		#这里会给出依赖方案，选一个可行的

apt-get insatll $package
```





### 5、关于python的字典

python3.6之前的dict都是无序的

当版本 >= 3.6 时，字典为有序的



py3.6 之前的无序字典

> 是以八行三列的数据结构存储
>
> 每一行有三列，每一列占用8byte的内存空间，所以每一行会占用24byte的内存空间
>
> 第一列：哈希值对8取余 hash(sKey)
>
> 第二列：sKey
>
> 第三列：sValue

​	当字典的键值对数量超过当前数组长度的2/3时，数组会进行扩容，8行变成16行，16行变成32行。长度变了以后，原来的余数位置也会发生变化，此时就需要移动原来位置的数据，导致插入效率变低。



py3.6之后

> 换成了两个一维列表组成

```
my_dict = {}

'''
此时的内存示意图 （indices 指数 entries 条目）
indices = [None, None, None, None, None, None, None, None]

entries = []
'''
```

这里先通过对 sKey 取余为 x ，然后 在 entries 插入一个列表 [ "hash值", sKey, sValue]

再在 indices 保存插入列表的下标，indices[x] = 下标



​	Python自带的这个`hash`函数，和我们传统上认为的Hash函数是不一样的。Python自带的这个`hash`函数计算出来的值，只能保证在每一个运行时的时候不变，但是当你关闭Python再重新打开，那么它的值就可能会改变，





### 6、关于负数取余

带余除法，

对于任意一个整数n ，都可以表示为 n=k*q + r ，其中 0 <= r < q

这里的 r 就是 n 除以 q 的余数，通常记做 n≡r(mod q)

例如-9=(-2)*5+1，则-9除以5的余数为1。



注：java 中 % 优先级高于 -





### 7、项目管理工具

才发现python居然没有项目管理工具比如maven

有时候摸索一下maven是怎么弄得







### 8、python的w跟w+



python 文件处理的打开方式有很多种，

os.mknod("test.txt") 创建空文件
fp = open("test.txt",w) 直接打开一个文件，如果文件不存在则创建文件

open 模式：

w 以写方式打开，
a 以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+ 以读写模式打开
w+ 以读写模式打开 (参见 w )
a+ 以读写模式打开 (参见 a )
rb 以二进制读模式打开
wb 以二进制写模式打开 (参见 w )
ab 以二进制追加模式打开 (参见 a )
rb+ 以二进制读写模式打开 (参见 r+ )
wb+ 以二进制读写模式打开 (参见 w+ )
ab+ 以二进制读写模式打开 (参见 a+ )

 

但r+和w+写的不清楚。

w+是打开后，清空原有内容，成为一个新的空文件，对这个空文件具有读写权限。

r+是打开后，可以读取文件内容吧，保存原有内容，追加写内容，写动作则是追加的新内容。其作用和a+基本相同。



原文链接：https://blog.csdn.net/longshenlmj/article/details/9921665





### 9、python3的`__str__`

当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据

比如：

```
class Cat:
    def __str__(self):
        return "猫"
    
t = Cat()
print(t)

# 猫
```





### 10、python的按位与、或

同为 2的n次方的数 

按位或的值等于各个数相加

并且用其中的一个值和最终的数与会得到他本身，反之为0 

```
if __name__ == '__main__':
    a, b, c = 2, 4, 8
    d = a | b | c
    
    print(d)
    print(a & d)
    print(d & c)
    print(32 & d)
    print(32 & c)

    # 14
    # 2
    # 8
    # 0
    # 0
```





### 11、一些斜杠转义

- **转义字符**：
  顾名思义，也就是在我们编码时会使用到的特殊字符。

| 转义字符          | 描述       |
| ----------------- | ---------- |
| \（处于行尾位置） | 续行符     |
| \\                | 反斜杠     |
| ’                 | 单引号     |
| \"                | 双引号     |
| \b                | 退格       |
| \n                | 换行       |
| \v                | 纵向制表符 |
| \t                | 横向制表符 |
| \r                | 回车       |
| \f                | 换页       |





### 12、python执行linux命令

```
import subprocess
import os


def subprocess_():
    """
    subprocess模块执行linux命令
    :return:
    """
    subprocess.call("ls") # 执行ls命令


def system_():
    """
    system模块执行linux命令
    :return:
    """
    # 使用system模块执行linux命令时，如果执行的命令没有返回值res的值是256
    # 如果执行的命令有返回值且成功执行，返回值是0
    res = os.system("ls")


def popen_():
    """
    popen模块执行linux命令。返回值是类文件对象，获取结果要采用read()或者readlines()
    :return:
    """
    val = os.popen('ls').read() # 执行结果包含在val中


def main():
    subprocess_() # 方法1
    system_() # 方法2
    popen_() # 方法3


if __name__ == '__main__':
    main()
```





### 13、赋值

```
a=b=c=[]
```

a b c 共享内存





### 14、设计模式

https://refactoringguru.cn/design-patterns/catalog







### 15、django

迪迦狗

https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/actions/





### 16、print与sys.stdout.write

- `sys.stdout.write()`只能输出一个字符串str，而`print()`可以输出多个值，数据类型多样。
- `print(obj)`实际上是调用`sys.stdout.write(obj+'\n')`，因此print在打印时会自动加个换行符。





### 17、关于多线程队列实现

- **threading**

  队列是基于双向队列 dedque 实现

  - **start()：**开启线程活动。它将使得run()方法在一个独立的控制线程中被调用，需要注意的是同一个线程对象的start()方法只能被调用一次，如果调用多次，则会报RuntimeError错误。

  - **run()：**此方法代表线程活动。

  - **join(timeout=None)：**让当前调用者线程（即开启线程的线程，一般就是主线程）等待，直到线程结束（无论它是什么原因结束的），timeout参数是以秒为单位的浮点数，用于设置操作超时的时间，返回值为None。如果想要判断线程是否超时，只能通过线程的is_alive方法来进行判断。join方法可以被调用多次。如果对当前线程使用join方法（即线程在内部调用自己的join方法），或者在线程没有开始前使用join方法，都会报RuntimeError错误。

  - **name：**线程的名称字符串，并没有什么实际含义，多个线程可以赋予相同的名称，初始值由初始化方法来设置。

  - **ident：**线程的标识符，如果线程还没有启动，则为None。ident是一个非零整数，参见threading.get_ident()函数。当线程结束后，它的ident可能被其他新创建的线程复用，当然就算该线程结束了，它的ident依旧是可用的。

  - **is_alive()：**线程是否存活，返回True或者False。在线程的run()运行之后直到run()结束，该方法返回True。

  - **daemon：**表示该线程是否是守护线程，True或者False。设置一个线程的daemon必须在线程的start()方法之前，否则会报RuntimeError错误。这个值默认继承自创建它的线程，主线程默认是非守护线程的，所以在主线程中创建的线程默认都是非守护线程的，即daemon=False。

    

  **threading.Condition(lock=None)：**一个条件变量对象允许一个或多个线程等待，直到被另一个线程通知。lock参数必须是一个Lock对象或者RLock对象，并且会作为底层锁使用，默认使用RLock。

  - **acquire(\*args)：**请求底层锁。此方法调用底层锁对应的方法和返回对应方法的返回值。
  - **release()：**释放底层锁。此方法调用底层所对应的方法，没有返回值。
  - **wait(timeout=None)：**释放锁，等待直到被通知（再获取锁）或者发生超时事件。如果线程在调用此方法时本身并没有锁（即线程首先得有锁），则会报RuntimeError错误。这个方法释放底层锁，然后阻塞线程，直到另一个线程中的同一个条件变量使用notify()或notify_all()唤醒，或者超时事件发生，一旦被唤醒或者超时，则会重新去获取锁并返回（成功返回True，否则返回False）。timeout参数为浮点类型的秒数。在RLock中使用一次release方法，可能并不能释放锁，因为锁可能被acquire()了多次，但是在条件变量对象中，它调用了RLock类的内部方法，可以一次就完全释放锁，重新获取锁时也会重置锁的递归等级。
  - **wait_for(predicate, timeout=None)：**与wait方法相似，等待，直到条件计算为True，返回最后一次的predicate的返回值。predicate参数为一个返回值为布尔值的可调用对象。调用此方法的时候会先调用predicate对象，如果返回的就是True，则不会释放锁，直接往后执行。另一个线程通知后，在它释放锁时，才会触发wait_for方法等待事件，这时如果predicate结果为True，则尝试获取锁，获取成功后则继续往后执行，如果为False，则会一直阻塞下去。此方法如果忽略timeout参数，就相当于：while not predicate(): condition_lock.wait()。
  - **notify(n=1)：**唤醒一个等待这个条件的线程，如果调用这个方法的线程在没有获得锁的情况下调用这个方法，会报RuntimeError错误。默认唤醒一个线程，可以通过参数n设置唤醒n个正在等待这个条件变量的线程，如果没有线程在等待，调用这个方法不会发生任何事。如果等待的线程中正好有n个线程，那么这个方法可以准确的唤醒这n个线程，但是等待的线程超过指定的n个，有时候可能会唤醒超过n个的线程，所以依赖参数n是不安全的行为。
  - **notify_all()：**唤醒所有等待这个条件的线程。这个方法与notify()不同之处在于它唤醒所有线程，而不是特定n个。

- **multiprocessing**

  队列是基于 管道 pipe 实现

  有最大限制，win10是1408，linux是6570





### 18、def main () -> None



照原样，它完全什么都不做。它是`main`函数的类型注释，只是声明该函数返回`None`。类型注释被引入`Python 3.5`并在 中指定[`PEP 484`](https://www.python.org/dev/peps/pep-0484/)。

函数返回值的注释使用`->`后跟类型的符号。它是完全可选的，如果你删除它，什么都不会改变。





### 19、关于可重入锁

为什么要有可重入锁？

当存在继承或者递归调用的时候，可能会出现重复加锁的情况，

如果不能重复加锁，就会自己把自己给锁死





### 20、时间格式

```
# django 数据库查询 2021-07-30T02:46:00.Z 格式日期转换

# 末日数据库格式查询结果
a = datetime.datetime('2021-07-30T02:46:00.Z')

TIME_ZONE = 'Asia/Shanghai'
TZ_SHANGHAI = pytz.timezone(TIME_ZONE)

# 转换
a.astimezone(TZ_SHANGHAI).strftime('%Y-%m-%d %H:%M:%S')
```





### 21、合并多个字典

```
dict(dict1, **dict2, **dict3)
```

这里要注意 **参数关键字必须是字符串





### 22、*args, **kwargs

```
单个 * 表示元组列表
** 表示转换为字典	这个时候首层的字典的键必须为字符串
```





### 23、编码解码

python3一个新特性就是对文本和二进制做了更清晰的划分，文本是str，二进制是byte(\x01\x06...)

编码 encode：str --> byte

解码 decode：byte --> str





### 24、字符串的拼接使用join

字符串的拼接有两种方式
- +			如果有n个字符串需要拼接，就会进行n-1次内存空间申请
- join		只会进行一次空间申请，申请时会统计所有字符串的个数，以及总的长度。再逐一进行字符串的拷贝



### 25、python三种基础序列类型

- list		可变序列，存放同类项目的集合
- tuple		不可变序列，存放固定长度的不同种类的对象集合
- range		不可变的数字序列，通常在for循环中循环指定的次数


### 26、一些优化建议

- 创建列表时，建议有初始值就写初始值，不要创建空列表再填充。因为创建空列表一定会扩容
- 列表的合并，使用 extend或者 += 较好与直接+



### 27、pyhton的选项

python -B

执行时不生成pyc文件





### 28、进制

八进制 0 开头

十六进制 0x 开头



转换

n进制转换为十进制，假设需要转换的位str的数字字符串

```
# str=001234; n=8
print int(str, n)
```


### 29. getsizeof()

sys.getsizeof()
获取程序中声明的一个整数，存储在变量中的大小

相似场景：文件复制案例中需要获取文件大小，尝试使用 sys.getsizeof()方法
确认：sys.getsizeof()方法用于获取变量中存储数据的大小



### 30. getsize()

os.path.getsize(path)
获取指定路径 path 下的文件的大小，以字节为单位
计算机中的单位换算：字节→1024-K→1024-M→1024-G→1024-T…





### 31. enmerate()

将列表转换为序号值得形式（类似于字典）





