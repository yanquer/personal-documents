
### 关于`__init__`

#### `__init__.py`

> 文件名
>
> 在Python工程里，当python检测到一个目录下存在`__init__.py`文件时，python就会把它当成一个模块(module)。Module跟C＋＋的命名空间和Java的Package的概念很像，都是为了科学地组织化工程，管理命名空间。
>
> `__init__.py`可以是一个空文件，也可以有非常丰富的内容。
>
> 
>
> `__init__.py`的原始使命是声明一个模块，所以它可以是一个空文件。在`__init__.py`中声明的所有类型和变量，就是其代表的模块的类型和变量
>
> 
>
> 我们在利用`__init__.py`时，应该遵循如下几个原则：
>
> A、不要污染现有的命名空间。模块一个目的，是为了避免命名冲突，如果你在种用`__init__.py`时违背这个原则，是反其道而为之，就没有必要使用模块了。
>
> B、利用`__init__.py`对外提供类型、变量和接口，对用户隐藏各个子模块的实现。一个模块的实现可能非常复杂，你需要用很多个文件，甚至很多子模块来实现，但用户可能只需要知道一个类型和接口。由于各个子模块的实现有可能非常复杂，而对外提供的类型和接口有可能非常的简单，我们就可以通过这个方式来对用户隐藏实现，同时提供非常方便的使用。
>
> C、只在`__init__.py`中导入有必要的内容，不要做没必要的运算。如果我们在`__init__.py`中做太多事情，每次import都会有额外的运算，会造成没有必要的开销。



`def __init__()`

> 用于类中，一般表示初始化类（构造函数）


### 关于`__init__.py`和`__main__.py`

当在文件夹下时

`__init__.py`表示是一个模块(把当前文件所在文件夹视为一个模块，相当于把此文件夹的上一层加入path)

`__main__.py`表示文件所在文件夹可以直接执行（把当前文件所在路径加入到sys.path）



举个例子：

我把他们都放到 test 文件夹下

- 执行 pyton test 只会执行 `__main__.py`
- 执行 python -m test 会先执行 `__init__.py` ， 再执行`__main__.py`



链接：https://www.jianshu.com/p/cb97d290c17f
