### Json模块


#### 1、loads与load方法的异同

在Python中json是一个非常常用的模块，这个主要有4个方法：

```python
json.dumps
json.dump
json.loads
json.load
```



| 方法         | 作用                                         |
| ------------ | -------------------------------------------- |
| json.dumps() | 将python对象编码成Json字符串                 |
| json.loads() | 将Json字符串解码成python对象                 |
| json.dump()  | 将python中的对象转化成json储存到文件中       |
| json.load()  | 将文件中的json的格式转化成python对象提取出来 |



**dump()和dumps()之间的区别**

>json.dumps()是把python对象转换成json对象的一个过程，生成的是字符串。
>json.dump()是把python对象转换成json对象生成一个fp的文件流，和文件相关。

| **dump()**                                             | **dumps()**                                                  |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| 当必须将Python对象存储在文件中时，可以使用dump()方法。 | 当对象必须为字符串格式时，可以使用dumps()并将其用于解析，打印等。 |
| dump()需要json文件名，在其中必须将输出存储为参数。     | dumps()不需要传递任何此类文件名。                            |
| 该方法写入内存，然后单独执行写入磁盘的命令             | 该方法直接写入json文件                                       |
| 更快的方法                                             | 慢2倍                                                        |



#### dump()及其参数

```python
json.dump(data, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None)
```



| 参数                  | 含义                                                         |
| --------------------- | ------------------------------------------------------------ |
| **sort_keys =True**   | 是告诉编码器按照字典排序(a到z)输出。如果是字典类型的python对象，就把关键字按照字典排序。 |
| **indent**            | 参数根据数据格式缩进显示，读起来更加清晰。                   |
| **separators**        | 是分隔符的意思，参数意思分别为不同dict项之间的分隔符和dict项内key和value之间的分隔符 |
| **skipkeys**          | 默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key |
| **ensure_ascii=True** | 默认输出ASCLL码，如果把这个该成False,就可以输出中文          |
| **check_circular**    | 如果check_circular为false，则跳过对容器类型的循环引用检查，循环引用将导致溢出错误(或更糟的情况) |
| **allow_nan**         | 如果allow_nan为假，则ValueError将序列化超出范围的浮点值(nan、inf、-inf)，严格遵守JSON规范，而不是使用JavaScript等价值(nan、Infinity、-Infinity) |
| **default**           | default(obj)是一个函数，它应该返回一个可序列化的obj版本或引发类型错误。默认值只会引发类型错误 |



下面主要分析讲解一下json的loads和load方法。
这两个方法中都是把其他类型的对象转为Python对象，这里先说明一下Python对象，
Python对象包括：
所有Python基本数据类型，列表，元组，字典，自己定义的类，等等等等，当然不包括Python的字符串类型，把字符串或者文件鎏中的字符串转为字符串会报错的



##### 1.1、不相同点：

loads操作的是字符串
load操作的是文件流



##### 1.2、 相同点

除了第一个参数（要转换的对象）类型不同，其他所有的参数都相同
最终都是转换成Python对象



##### 1.3 、例子

先来一个例子，除了要转换的对象，其他什么参数都不传：

```python
s = '{"name": "wade", "age": 54, "gender": "man"}'
# json.loads读取字符串并转为Python对象
print("json.loads将字符串转为Python对象: type(json.loads(s)) 
      = {}".format(type(json.loads(s))))
print("json.loads将字符串转为Python对象: json.loads(s) 
      = {}".format(json.loads(s)))

# json.load读取文件并将文件内容转为Python对象
# 数据文件要s.json的内容 --> {"name": "wade", "age": 54, "gender": "man"}
with open('s.json', 'r') as f:
    s1 = json.load(f)
    print("json.load将文件内容转为Python对象: type(json.load(f)) = {}".format(type(s1)))
    print("json.load将文件内容转为Python对象: json.load(f) = {}".format(s1))

```



![img](https://img-blog.csdnimg.cn/20190907152436206.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RhZXJ6ZWk=,size_16,color_FFFFFF,t_70)





#### 2、转换成Python对象

由于loads和load两个方法只是处理的数据源不同，其他的参数都是相同的，返回的结果类型也相同，故这是loads和load方法两个只说一个，

日常工作中最常见的就是把字符串通过json.loads转为字典，其实json的loads方法不仅可以把字符串转为字典，还可以转为任何Python对象。
比如说，转成python基本数据类型：

```python
print('json.loads 将整数类型的字符串转为int类型: type(json.loads("123456"))) --> {}'.format(type(json.loads("123456"))))

print('json.loads 将浮点类型的字符串转为float类型: type(json.loads("123.456")) --> {}'.format(type(json.loads("123.456"))))

print('json.loads 将boolean类型的字符串转为bool类型: type(json.loads("true")) --> {}'.format((type(json.loads("true")))))

print('json.loads 将列表类型的字符串转为列表: type(json.loads(\'["a", "b", "c"]\')) --> {}'.format(type(json.loads('["a", "b", "c"]'))))

print('json.loads 将字典类型的字符串转为字典: type(json.loads(\'{"a": 1, "b": 1.2, "c": true, "d": "ddd"}\')) --> %s' % str(type(json.loads('{"a": 1, "b": 1.2, "c": true, "d": "ddd"}'))))
```



![Python中json模块的loads和load方法实战详解_02](https://img-blog.csdnimg.cn/20190907152524173.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RhZXJ6ZWk=,size_16,color_FFFFFF,t_70)



json模块会根据你的字符串自动转为最符合的数据类型，

但是需要注意的是不能把转为字符串，否则会报json.decoder.JSONDecodeError错误:

```python
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```





#### 3、json.load(s)的参数

我们先看下json.loads方法的签名：

```python
def loads(s, encoding=None, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    """Deserialize ``s`` (a ``str`` or ``unicode`` instance containing a JSON    # 把一个字符串反序列化为Python对象，这个字符串可以是str类型的，也可以是unicode类型的
    document) to a Python object.


    If ``s`` is a ``str`` instance and is encoded with an ASCII based encoding    # 如果参数s是以ASCII编码的字符串，那么需要手动通过参数encoding指定编码方式，
    other than utf-8 (e.g. latin-1) then an appropriate ``encoding`` name         # 不是以ASCII编码的字符串，是不被允许的，你必须把它转为unicode
    must be specified. Encodings that are not ASCII based (such as UCS-2)
    are not allowed and should be decoded to ``unicode`` first.


    ``object_hook`` is an optional function that will be called with the        # object_hook参数是可选的，它会将（loads的)返回结果字典替换为你所指定的类型
    result of any object literal decode (a ``dict``). The return value of        # 这个功能可以用来实现自定义解码器，如JSON-RPC
    ``object_hook`` will be used instead of the ``dict``. This feature
    can be used to implement custom decoders (e.g. JSON-RPC class hinting).


    ``object_pairs_hook`` is an optional function that will be called with the    # object_pairs_hook参数是可选的，它会将结果以key-value列表的形式返回
    result of any object literal decoded with an ordered list of pairs.  The      # 形式如：[(k1, v1), (k2, v2), (k3, v3)]
    return value of ``object_pairs_hook`` will be used instead of the ``dict``.   # 如果object_hook和object_pairs_hook同时指定的话优先返回object_pairs_hook
    This feature can be used to implement custom decoders that rely on the
    order that the key and value pairs are decoded (for example,
    collections.OrderedDict will remember the order of insertion). If
    ``object_hook`` is also defined, the ``object_pairs_hook`` takes priority.


    ``parse_float``, if specified, will be called with the string                 # parse_float参数是可选的，它如果被指定的话，在解码json字符串的时候，
    of every JSON float to be decoded. By default this is equivalent to           # 符合float类型的字符串将被转为你所指定的，比如说你可以指定为decimal.Decimal
    float(num_str). This can be used to use another datatype or parser
    for JSON floats (e.g. decimal.Decimal).


    ``parse_int``, if specified, will be called with the string                   # parse_int参数是可选的，它如果被指定的话，在解码json字符串的时候，
    of every JSON int to be decoded. By default this is equivalent to             # 符合int类型的字符串将被转为你所指定的，比如说你可以指定为float
    int(num_str). This can be used to use another datatype or parser
    for JSON integers (e.g. float).


    ``parse_constant``, if specified, will be called with one of the              # parse_constant参数是可选的，它如果被指定的话，在解码json字符串的时候，
    following strings: -Infinity, Infinity, NaN.                                  # 如果出现以以下字符串: -Infinity, Infinity, NaN 那么指定的parse_constant方法将会被调用到
    This can be used to raise an exception if invalid JSON numbers
    are encountered.


    To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``         # 你也可以用cls参数通过实现一个JSONDecoder的子类，来代替JSONDecoder,通过这个功能你可以自定义上面的那些parse_xxx参数,这里就不举例了
    kwarg; otherwise ``JSONDecoder`` is used.


    """
```

以下参数说明是根据官方文档翻译的

##### 3.1、s参数

把一个字符串反序列化为Python对象，这个字符串可以是str类型的，也可以是unicode类型的，如果参数s是以ASCII编码的字符串，那么需要手动通过参数encoding指定编码方式，不是以ASCII编码的字符串，是不被允许的，你必须把它转为unicode

对于loads方法来说，s是一个字符串，而对于load方法来说，是一个数据流文件

##### 3.2 、object_hook参数

object_hook参数是可选的，它会将（loads的)返回结果字典替换为你所指定的类型,这个功能可以用来实现自定义解码器，如JSON-RPC
这里先定义一个Person对象：

```python
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def toJSON(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }

    @staticmethod
    def parseJSON(dct):
        if isinstance(dct, dict):
            p = Person(dct["name"], int(dct['age']), dct['gender'])
            return p
        return dct
```

OK，试下object_hook参数吧：

```python
s = '{"name": "马云", "age": 54, "gender": "man"}'
# 测试json.loads方法的object_hook参数
p = json.loads(s, object_hook=Person.parseJSON)
print("json.loads 是否将字符串转为字典了: --> " + str(isinstance(p, dict)))
print("json.loads 是否将字符串转为Person对象了: --> " + str(isinstance(p, Person)))
```



![Python中json模块的loads和load方法实战详解_05](https://img-blog.csdnimg.cn/20190907160427855.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RhZXJ6ZWk=,size_16,color_FFFFFF,t_70)



##### 3.3 、object_pairs_hook参数

object_pairs_hook参数是可选的，它会将结果以key-value有序列表的形式返回,形式如：`[(k1, v1), (k2, v2), (k3, v3)]`,如果object_hook和object_pairs_hook同时指定的话优先返回object_pairs_hook

```python
s = '{"name": "马云", "age": 54, "gender": "man"}'
# 测试json.loads方法的object_pairs_hook参数
print("-" * 30 + "> test object_pairs_hook <" + "-" * 30)
p = json.loads(s, object_hook=Person.parseJSON, object_pairs_hook=collections.OrderedDict)
# p = json.loads(s, object_hook=Person.parseJSON, object_pairs_hook=Person.parseJSON)
print("json.loads 测试同时指定object_hook和object_pairs_hook,最终调用哪个参数: --> " + str(type(p)))
print("json.loads 指定object_pairs_hook结果将会返回一个有序列表 --> {}".format(p))
```



![Python中json模块的loads和load方法实战详解_06](https://img-blog.csdnimg.cn/20190907161313895.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RhZXJ6ZWk=,size_16,color_FFFFFF,t_70)



##### 3.4 、parse_float参数

parse_float参数是可选的，它如果被指定的话，在解码json字符串的时候，符合float类型的字符串将被转为你所指定的，比如说你可以指定为decimal.Decimal

```python
# 测试json.loads方法的parse_float参数
print("-" * 30 + "> test parse_float <" + "-" * 30)
p = json.loads("123.456", parse_float=decimal.Decimal)
print("json.loads 通过parse_float参数将原本应该转为float类型的字符串转为decimal类型: type(json.loads(\"123.456\", parse_float=decimal.Decimal)) --> " + str(type(p)))
print("")
```



![Python中json模块的loads和load方法实战详解_07](https://img-blog.csdnimg.cn/20190907161655372.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RhZXJ6ZWk=,size_16,color_FFFFFF,t_70)



##### 3.5 、parse_int参数

parse_int参数是可选的，它如果被指定的话，在解码json字符串的时候，符合int类型的字符串将被转为你所指定的，比如说你可以指定为float

```python
# 测试json.loads方法的parse_int参数
print("-" * 30 + "> test parse_int <" + "-" * 30)
p = json.loads("123", parse_int=float)
print("json.loads 通过parse_int参数将原本应该转为int类型的字符串转为float类型: type(json.loads(\"123\", parse_int=float)) --> " + str(type(p)))
```



![Python中json模块的loads和load方法实战详解_08](https://img-blog.csdnimg.cn/20190907161928429.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RhZXJ6ZWk=,size_16,color_FFFFFF,t_70)



##### 3.6 、parse_constant参数

parse_constant参数是可选的，它如果被指定的话，在解码json字符串的时候，如果出现以以下字符串:-Infinity，Infinity，NaN那么指定的parse_constant方法将会被调用到

```python
def transform(s):
    """
    此方法作为参数传给json.load(s)方法的parse_转译NAN, -Infinity,Infinity
    :param s:
    :return:
    """
    # NaN --> not a number
    if "NaN" == s:
        return "Not a Number"
    # 将负无穷大转为一个非常小的数
    elif "-Infinity" == s:
        return -999999
    # 将正无穷大转为一个非常大的数
    elif "Infinity" == s:
        return 999999
    else:
        return s

# 测试json.loads方法的parse_constant参数
print("-" * 30 + "> test parse_constant <" + "-" * 30)
print("json.loads Infinity: --> " + str(json.loads('Infinity')))
print("json.loads parse_constant convert Infinity: --> " + str(json.loads('Infinity', parse_constant=transform_constant)))

print("json.loads -Infinity: --> " + str(json.loads('-Infinity')))
print("json.loads parse_constant convert -Infinity: --> " + str(json.loads('-Infinity', parse_constant=transform_constant)))

print("json.loads NaN: --> " + str(json.loads('NaN')))
print("json.loads parse_constant convert NaN : --> " + str(json.loads('NaN', parse_constant=transform_constant)))
print("")
```



![Python中json模块的loads和load方法实战详解_09](https://img-blog.csdnimg.cn/20190907172608636.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RhZXJ6ZWk=,size_16,color_FFFFFF,t_70)



##### 3.7 、cls参数

通过官方文档的注释我们可以知道json.load(s)方法具体的实现是通过JSONCoder类实现的，而cls参数是用于自定义一个JSONCoder的子类，用于替换JSONCoder类，,通过这个功能你可以自定义上面的那些parse_xxx参数，这里就不举例了
原文链接：https://blog.csdn.net/daerzei/article/details/100598901

