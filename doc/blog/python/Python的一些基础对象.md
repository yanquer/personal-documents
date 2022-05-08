## Python的一些基础对象



### 字典（dict）

Python 字典(Dictionary) get() 函数返回指定键的值。

```python
dict.get(key, default=None)
```

- key -- 字典中要查找的键。
- default -- 如果指定键的值不存在时，返回该默认值。





### 列表

index()方法：

>检测**字符串**中是否包含子字符串 str，并返回索引值；
>从**列表**中找出某个值第一个匹配项的索引位置。

（时隔不久，我已经忘了这是啥了）



list 求交集并集差集

不建议的

```python
# 假设有两个集合 a,b
# 交集
[val for val in a if val in b]
# 并集
list(set(a+b))
# 差集
[val for val in b if val not in a]	# b中有而a中没有的
```



建议的高效的

```python
# 假设有两个集合 a,b
# 交集
list(set(a).intersection(set(b)))
# 并集
list(set(a).union(set(b)))
# 差集
list(set(b).difference(set(a)))	# b中有而a中没有的
```



set的运算

```python
s = set([3,5,9,10,20,40])      #创建一个数值集合 
t = set([3,5,9,1,7,29,81])      #创建一个数值集合 

a = t | s          # t 和 s的并集 ,等价于t.union(s)
b = t & s          # t 和 s的交集 ,等价于t.intersection(s) 
c = t - s          # 求差集（项在t中，但不在s中）  ,等价于t.difference(s) 
d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）,等价于t.symmetric_difference(s)
```


