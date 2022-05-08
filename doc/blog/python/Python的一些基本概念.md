## Python的一些基本概念





### 生成器

> A function which returns a generator iterator. It looks like a normal function except that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.

> Usually refers to a generator function, but may refer to a generator iterator in some contexts. In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.



定义：一边循坏一边计算的机制（generator）



1、它是一个**迭代器**；

2、它是一个含有特殊关键字 **yield** 的**迭代器**；

3、每次生成一个值，可通过 **next()** 方法获取。



创建一个生成器对象，

方法一：只需要将列表生成式的 [] 换成 () 即可

```python
g = (x * x for x in range(10))
```



方法二：函数使用 yield 关键字，那么这个函数将是一个 generator

```python
def g():
	a = {id:0 for id in range(10)}
	for k, v in a.items():
		yield k, v
```



原理：

（1）生成器(generator)能够迭代的关键是它有一个next()方法，

　　工作原理就是通过重复调用next()方法，直到捕获一个异常。

（2）带有 yield 的函数不再是一个普通函数，而是一个生成器generator。

　　可用next()调用生成器对象来取值。next 两种方式 t.__next__() | next(t)。

　　可用for 循环获取返回值（每执行一次，取生成器里面一个值）

　　（基本上不会用`next()`来获取下一个返回值，而是直接使用`for`循环来迭代）。

（3）yield相当于 return 返回一个值，并且记住这个返回的位置，下次迭代时，代码从yield的下一条语句开始执行。

（4）.send() 和next()一样，都能让生成器继续往下走一步（下次遇到yield停），但send()能传一个值，这个值作为yield表达式整体的结果

　　——换句话说，就是send可以强行修改上一个yield表达式值。比如函数中有一个yield赋值，a = yield 5，第一次迭代到这里会返回（5）a还没有赋值。第二次迭代时，使用.send(10)，那么，就是强行修改yield 5表达式的值为10，本来是5的，那么a=10







### 列表生成式

```python
a = [x * x for x in range(10)]
```





### 字典生成式

```python
a = {id:0 for id in range(10)}
```







### 可迭代对象（Iterable）

>iterable
An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any classes you define with an **iter**() method or with a **getitem**() method that implements Sequence semantics.

> Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …). When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself. The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. See also iterator, sequence, and generator.



1、它是能够一次返回一个成员的对象，也就是可以 for…in 遍历的；

2、所有的序列类型（也就是后面要说到的 Sequence），都是可迭代对象，如 list、str、tuple，还有映射类型 dict、文件对象等非序列类型也是可迭代对象；

3、自定义对象在实现了 **iter**() 方法或者实现了 **getitem**() 方法后，也可以成为可迭代对象；

4、**iter()**方法接受一个可迭代对象，该方法的返回值是一个迭代器（Iterator）



那么如何判断一个对象是可迭代对象呢？很容易想到的方法是 isinstance，这时候我们需要注意一点，文档介绍如下：

> class collections.abc.Iterable
> ABC for classes that provide the **iter**() method.

> Checking isinstance(obj, Iterable) detects classes that are registered as Iterable or that have an **iter**() method, but it does not detect classes that iterate with the **getitem**() method. The only reliable way to determine whether an object is iterable is to call iter(obj).

简单解释就是：通过 **isinstance(obj, Iterable)** 判断一个对象是否是可迭代对象时，只有当这个对象被注册为 Iterable 或者当它实现了 **iter() **方法的时候，才返回 True，而对于实现了 **getitem**() 方法的，返回的是 False。所以当判断是否是可迭代对象的方式是调用 **iter(obj)**，如果不报错，说明是可迭代对象，反之则不是。







### 序列（Sequence）

> An iterable which supports efficient element access using integer indices via the **getitem**() special method and defines a **len**() method that returns the length of the sequence. Some built-in sequence types are list, str, tuple, and bytes. Note that dict also supports **getitem**() and **len**(), but is considered a mapping rather than a sequence because the lookups use arbitrary immutable keys rather than integers.

> The collections.abc.Sequence abstract base class defines a much richer interface that goes beyond just **getitem**() and **len**(), adding count(), index(), **contains**(), and **reversed**(). Types that implement this expanded interface can be registered explicitly using register().



提练重点如下：

1、可迭代；

2、支持下标访问，即实现了 **getitem**() 方法，同时定义了 **len**() 方法，可通过 len() 方法获取长度；

3、内置的序列类型：list、str、tuple、bytes；

4、dict 同样支持 **getitem**() 和 **len**()，但它不归属于序列类型，它是映射类型，因为它不能根据下标查找，只能根据 key 来查找；

5、抽象类 collections.abc.Sequence 还提供了很多方法，比如 count()、index()、**contains**()、**reversed**()可用于扩展；

总结结论：**序列一定是一个可迭代对象，但可迭代对象不一定是序列**。







### 迭代器（Iterator）

> An object representing a stream of data. Repeated calls to the iterator’s **next**() method (or passing it to the built-in function next()) return successive items in the stream. When no more data are available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its **next**() method just raise StopIteration again. Iterators are required to have an **iter**() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.



1、一个表示**数据流**的对象，可通过重复调用 **next**（或使用内置函数**next()**）方法来获取元素。当没有元素存在时，抛出 StopIteration 异常；

2、**iter(obj)**接受一个迭代器作为参数时，返回的是它本身。在可迭代对象里我们说过，iter(obj)方法不报错，说明它一定是一个可迭代对象。因此迭代器一定是一个可迭代对象；

3、一个迭代器必须要实现 **iter**() 方法。但因为迭代器前提必须是一个可迭代对象，所以只实现 **iter**() 方法不一定是一个迭代器。



### 装饰器

作者：三眼鸭的编程教室
链接：https://www.zhihu.com/question/26930016/answer/1904166977



#### 函数装饰器

略



#### 带参数的装饰器

在装饰器外部再套一层带参装饰器



#### wraps装饰器

一个函数不止有他的执行语句，还有着 `__name__`（函数名），`__doc__` （说明文档）等属性，

```python3
def decorator(func):
    def wrapper(*args, **kwargs):
        """doc of wrapper"""
        print('123')
        return func(*args, **kwargs)

    return wrapper

@decorator
def say_hello():
    """doc of say hello"""
    print('同学你好')

print(say_hello.__name__)
print(say_hello.__doc__)
```



```text
wrapper
doc of wrapper
```



由于装饰器返回了 `wrapper` 函数替换掉了之前的 `say_hello` 函数，导致函数名，帮助文档变成了 `wrapper` 函数的了。

解决这一问题的办法是通过 `functools` 模块下的 `wraps` 装饰器。

```python3
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """doc of wrapper"""
        print('123')
        return func(*args, **kwargs)

    return wrapper

@decorator
def say_hello():
    """doc of say hello"""
    print('同学你好')

print(say_hello.__name__)
print(say_hello.__doc__)
```



```text
say_hello
doc of say hello
```





#### 内置装饰器

有三种我们经常会用到的装饰器， `property`、 `staticmethod`、 `classmethod`，他们有个共同点，都是作用于类方法之上。

##### property 装饰器

`property` 装饰器用于类中的函数，使得我们可以像访问属性一样来获取一个函数的返回值。

```python3
class XiaoMing:
    first_name = '明'
    last_name = '小'

    @property
    def full_name(self):
        return self.last_name + self.first_name

xiaoming = XiaoMing()
print(xiaoming.full_name)
```



```text
小明
```

例子中我们像获取属性一样获取 `full_name` 方法的返回值，这就是用 `property` 装饰器的意义，既能像属性一样获取值，又可以在获取值的时候做一些操作。

##### staticmethod 装饰器

`staticmethod` 装饰器同样是用于类中的方法，这表示这个方法将会是一个静态方法，意味着该方法可以直接被调用无需实例化，但同样意味着它没有 `self` 参数，也无法访问实例化后的对象。

```python3
class XiaoMing:
    @staticmethod
    def say_hello():
        print('同学你好')

XiaoMing.say_hello()

# 实例化调用也是同样的效果
# 有点多此一举
xiaoming = XiaoMing()
xiaoming.say_hello()
同学你好
同学你好
```

##### classmethod 装饰器

`classmethod` 依旧是用于类中的方法，这表示这个方法将会是一个类方法，意味着该方法可以直接被调用无需实例化，但同样意味着它没有 `self` 参数，也无法访问实例化后的对象。相对于 `staticmethod` 的区别在于它会接收一个指向类本身的 `cls` 参数。

```python3
class XiaoMing:
    name = '小明'

    @classmethod
    def say_hello(cls):
        print('同学你好， 我是' + cls.name)
        print(cls)

XiaoMing.say_hello()
```



```text
同学你好， 我是小明
<class '__main__.XiaoMing'>
```

#### 类装饰器

刚刚我们接触的装饰器是函数来完成，实际上由于 python 的灵活性， 我们用类也可以实现一个装饰器。

类能实现装饰器的功能， 是由于当我们调用一个对象时，实际上调用的是它的 `__call__` 方法。

```python3
class Demo:
    def __call__(self):
        print('我是 Demo')

demo = Demo()
demo()
```



```text
我是 Demo
```

通过这个特性，我们便可以用类的方式来完成装饰器，功能与刚开始用函数实现的一致。

```python3
class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('123')
        return self.func(*args, **kwargs)

@Decorator
def say_hello():
    print('同学你好')

say_hello()
```



```text
123
同学你好
```





### 总结

1、迭代的方式有两种，一种是通过下标，即实现 **getitem**，一种是直接获取值，即实现 **iter**，两种方式都可通过 ***\*for…in\**** 方式进行遍历。也都是可迭代对象；

2、isinstance 判断可迭代对象时，针对下标访问的判断有出入，需要特别注意；

3、可迭代对象基本要求是可遍历获取值；

4、序列一定是可迭代对象，它实现了 ***\*len()\**** 和 **getitem**，可获取长度，可通过下标访问；

5、迭代器一定是可迭代对象，它实现了 **next**()；

6、生成器是特殊的迭代器，它一定是迭代器，因此也一定是可迭代对象。


