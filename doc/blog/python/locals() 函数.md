### locals() 函数

**locals()** 函数会以字典类型返回当前位置的全部局部变量。

对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。

```sh
>>>def runoob(arg):    # 两个局部变量：arg、z
...     z = 1
...     print (locals())
... 
>>> runoob(4)
{'z': 1, 'arg': 4}      # 返回一个名字/值对的字典
>>>
```

