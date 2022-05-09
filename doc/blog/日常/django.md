## Django

进度：
https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/
下的字段选项

[执行查询 | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/3.2/topics/db/queries/)

下面的filter链的例子


参考：

[使用Django](https://docs.djangoproject.com/zh-hans/3.2/topics/)

[编写你的第一个 Django 应用，第 3 部分](https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial03/)



### 创建项目



```
django-admin startproject $项目名
```





### 模型模块module



总览

- module.objects.all() 获取该实例的所有信息
- module.objects.add() 添加
- module.objects.create() 创建
- module.objects.get() 
- module.objects.filter(**kargs) 过滤器 返回包含指定参数的QuerySet
- module.objects.exclude(**kargs) 返回不包含指定参数的QuerySet
- module.objects.annotate()
- module.objects.order_by() 排序
- module.objects.annotate()
- module.objects.alias()





filter/other

过滤后的QuerySet都是唯一的

前缀为变量或者说字段名

后缀如下：

- `__gt` : 大于
- `__gte` : 大于等于
- `__lt` : 小于
- `__lte` : 小于等于
- `__in` : 其中之一
- `__range` : 范围
- `__year` : 日期-年

- `__exact`：“精确”匹配（区分大小写）

- `__iexact`：是不区分大小写的匹配项

- `__contains`：区分大小写的模糊查询

- `__icontains`：不区分大小写的模糊查询，与`contains`相对应。
- `__startswith`：以什么开头的模糊查询（**区分大小写**）
- `__istartswith`：以什么开头的模糊查询（**不区分大小写**）
- `__endswith`：以什么结尾的模糊查询（**区分大小写**）
- `__iendswith`：以什么结尾的模糊查询（**不区分大小写**）
- `__isnull` : 是空的
- `__regex` : 区分大小写的正则匹配
- `__iregex` : 不区分大小写的正则匹配



#### 模型类



##### 1、模型定义

每个模型都是python的一个类，且需继承 django.db.models.Model

类下每个属性都相当于一个数据库字段



每当新建一个模型的时候，都需要在 setting.py下的  INSTALL_APPS 配置，如



新建 app

```
python manage.py start myapp
```



配置app

```
INSTALL_APPS = [
	'myapp'
]
```



将变更好的内容写入数据库

```
# 查找所有可用的模型 为任意一个在数据库中不存在对应数据表的模型创建迁移脚本文件
python manage.py makemigrations

# 将变更写入数据库
python manage.py migrate
```



##### 2、模型中的字段类型

待看
https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#model-field-types



###### AutoField

一个 IntegerField，根据可用的 ID 自动递增。你通常不需要直接使用它；如果你没有指定，主键字段会自动添加到你的模型中。


###### BigAutoField

一个 64 位整数，与 AutoField 很相似，但保证适合 1 到 9223372036854775807 的数字。


###### BigIntegerField

一个 64 位的整数，和 IntegerField 很像，只是它保证适合从 -9223372036854775808 到 9223372036854775807 的数字。该字段的默认表单部件是一个 NumberInput。


###### BinaryField

一个用于存储原始二进制数据的字段。可以指定为 bytes、bytearray 或 memoryview。

默认情况下，BinaryField 将 ediditable` 设置为 False，在这种情况下，它不能被包含在 ModelForm 中。

BinaryField 有一个额外的可选参数：

	BinaryField.max_length
	The maximum length (in bytes) of the field. The maximum length is enforced in Django's validation using MaxLengthValidator.

滥用 BinaryField

虽然你可能会想到在数据库中存储文件，但考虑到这在99%的情况下是糟糕的设计。这个字段 不能 代替正确的 静态文件 处理。


###### BooleanField

一个 true／false 字段。

该字段的默认表单部件是 CheckboxInput，或者如果 null=True 则是 NullBooleanSelect。

当 Field.default 没有定义时，BooleanField 的默认值是 None。


###### CharField

一个字符串字段，适用于小到大的字符串。

对于大量的文本，使用 TextField。

该字段的默认表单部件是一个 TextInput。

CharField 有两个额外的参数：

	CharField.max_length
	必须的。该字段的最大长度（以字符为单位）。max_length 在数据库层面强制执行，在 Django 的验证中使用 MaxLengthValidator。



###### DateField

一个日期，在 Python 中用一个 datetime.date 实例表示。有一些额外的、可选的参数。

DateField.auto_now
每次保存对象时，自动将该字段设置为现在。对于“最后修改”的时间戳很有用。请注意，当前日期 总是 被使用，而不仅仅是一个你可以覆盖的默认值。

只有在调用 Model.save() 时，该字段才会自动更新。当以其他方式对其他字段进行更新时，如 QuerySet.update()，该字段不会被更新，尽管你可以在这样的更新中为该字段指定一个自定义值。

DateField.auto_now_add
当第一次创建对象时，自动将该字段设置为现在。对创建时间戳很有用。请注意，当前日期是 始终 使用的；它不是一个你可以覆盖的默认值。因此，即使你在创建对象时为该字段设置了一个值，它也会被忽略。如果你想修改这个字段，可以设置以下内容来代替 auto_now_add=True ：

对于 DateField: default=date.today ——来自 datetime.date.today()
对于 DateTimeField: default=timezone.now ——来自 django.utils.timezone.now()
该字段的默认表单部件是一个 DateInput。管理中增加了一个 JavaScript 日历，以及“今天”的快捷方式。包含一个额外的 invalid_date 错误信息键。

auto_now_add、auto_now 和 default 选项是相互排斥的。这些选项的任何组合都会导致错误。

注解

目前，将 auto_now 或 auto_now_add 设置为 True，将导致该字段设置为 editable=False 和 blank=True。

注解

auto_now 和 auto_now_add 选项将始终使用创建或更新时 默认时区 的日期。如果你需要一些不同的东西，你可能需要考虑使用你自己的可调用的默认值，或者覆盖 save() 而不是使用 auto_now 或 auto_now_add ；或者使用 DateTimeField 而不是 DateField，并决定如何在显示时间处理从日期时间到日期的转换。


###### DateTimeField

class DateTimeField(auto_now=False, auto_now_add=False, \*\*options)
一个日期和时间，在 Python 中用一个 datetime.datetime 实例表示。与 DateField 一样，使用相同的额外参数。

该字段的默认表单部件是一个单独的 DateTimeInput。管理中使用两个单独的 TextInput 部件，并使用 JavaScript 快捷方式。

###### DecimalField

class DecimalField(max_digits=None, decimal_places=None, \*\*options)
一个固定精度的十进制数，在 Python 中用一个 Decimal 实例来表示。它使用 DecimalValidator 验证输入。

有两个 必要的 参数：

DecimalField.max_digits
数字中允许的最大位数。请注意，这个数字必须大于或等于 decimal_places。

DecimalField.decimal_places
与数字一起存储的小数位数。

例如，如果要存储精度为小数点后两位的 999 的数字，你可以使用：

models.DecimalField(..., max_digits=5, decimal_places=2)
并以 10 位小数的精度来存储最多约 10 亿的数字：

models.DecimalField(..., max_digits=19, decimal_places=10)
当 localize 为 False 时是 NumberInput 否则，该字段的默认表单部件是 TextInput。

注解

关于 FloatField 和 DecimalField 类之间差异的更多信息，请参见 FloatField vs. DecimalField。你还应该注意小数字段的 SQLite 限制。


###### DurationField
class DurationField(\*\*options)
一个用于存储时间段的字段——在 Python 中用 timedelta 建模。当在 PostgreSQL 上使用时，使用的数据类型是 interval，在 Oracle 上使用的数据类型是 INTERVAL DAY(9) TO SECOND(6)。否则使用微秒的 bigint。

注解

DurationField 的算术在大多数情况下是可行的。但在 PostgreSQL 以外的所有数据库中，将 DurationField 的值与 DateTimeField 实例上的算术进行比较，将无法达到预期的效果。

###### EmailField

class EmailField(max_length=254, \*\*options)
一个 CharField，使用 EmailValidator 来检查该值是否为有效的电子邮件地址。

###### FileField

class FileField(upload_to=None, max_length=100, \*\*options)
一个文件上传字段

注解

primary_key 参数不支持，如果使用，会引起错误。

有两个可选参数：

FileField.upload_to
这个属性提供了一种设置上传目录和文件名的方式，可以有两种设置方式。在这两种情况下，值都会传递给 Storage.save() 方法。

如果你指定一个字符串值或一个 Path，它可能包含 strftime() 格式，它将被文件上传的日期／时间所代替（这样上传的文件就不会填满指定的目录）。例如：

class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
如果你使用的是默认的 FileSystemStorage，这个字符串的值将被附加到你的 MEDIA_ROOT 路径后面，形成本地文件系统中上传文件的存储位置。如果你使用的是不同的存储系统，请检查该存储系统的文档，看看它是如何处理 upload_to 的。

upload_to 也可以是一个可调用对象，如函数。这个函数将被调用以获得上传路径，包括文件名。这个可调用对象必须接受两个参数，并返回一个 Unix 风格的路径（带斜线），以便传给存储系统。这两个参数是：

参数	描述
instance	
定义 FileField 的模型实例。更具体地说，这是附加当前文件的特定实例。

在大多数情况下，这个对象还没有被保存到数据库，所以如果它使用默认的 AutoField，它的主键字段可能还没有一个值。

filename	最初给文件的文件名。在确定最终目标路径时，可能会考虑到，也可能不会考虑到。
例子：

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
FileField.storage¶
一个存储对象，或是一个返回存储对象的可调用对象。它处理你的文件的存储和检索。参见 管理文件，了解如何提供这个对象。

Changed in Django 3.1:
增加了提供可调用对象的能力。

该字段的默认表单部件是一个 ClearableFileInput。

在模型中使用 FileField 或 ImageField （见下文）需要几个步骤：

在你的配置文件中，你需要定义 MEDIA_ROOT 作为你希望 Django 存储上传文件的目录的完整路径。（为了保证性能，这些文件不存储在数据库中。）定义 MEDIA_URL 作为该目录的基本公共 URL。确保这个目录是 Web 服务器的用户账号可以写的。
将 FileField 或 ImageField 添加到你的模型中，定义 upload_to 选项，指定 MEDIA_ROOT 的子目录，用于上传文件。
所有这些将被存储在你的数据库中的是一个文件的路径（相对于 MEDIA_ROOT ）。你很可能要使用 Django 提供的方便的 url 属性。例如，如果你的 ImageField 叫做 mug_shot，你可以在模板中使用 {{ object.mug_shot.url }} 获取图片的绝对路径。
例如，你的 MEDIA_ROOT 设置为 '/home/media'， upload_to 设置为 'photos/%Y/%m/%d'。upload_to 中的 '%Y/%m/%d' 部分是 strftime() 格式化，'%Y' 是四位数的年，'%m' 是两位数的月，'%d' 是两位数的日。如果你在 2007 年 1 月 15 日上传了一个文件，它将被保存在 /home/media/photos/2007/01/15 目录下。

如果你想检索上传文件的盘上文件名，或者文件的大小，可以分别使用 name 和 size 属性；关于可用属性和方法的更多信息，请参见 File 类参考和 管理文件 主题指南。

注解

文件在数据库中作为保存模型的一部分，因此在模型被保存之前，不能依赖磁盘上使用的实际文件名。

上传的文件的相对 URL 可以通过 url 属性获得。内部调用底层 Storage 类的 store() 方法。

需要注意的是，无论何时处理上传的文件，你都应该密切关注你上传的文件在哪里，是什么类型的文件，以避免安全漏洞。对所有上传的文件进行验证，这样你才能确定文件是你认为的那样。例如，如果你盲目地让别人上传文件，不经过验证，就上传文件到你的 Web 服务器的文档根目录下，那么有人就可以上传一个 CGI 或 PHP 脚本，并通过访问它的 URL 在你的网站上执行该脚本。不要允许这种情况发生。

另外要注意的是，即使是上传的 HTML 文件，由于可以被浏览器执行（虽然不能被服务器执行），也会造成相当于 XSS 或 CSRF 攻击的安全威胁。

FileField 实例在数据库中被创建为 varchar 列，默认最大长度为 100 个字符。与其他字段一样，你可以使用 max_length 参数改变最大长度。

###### FileField 和 FieldFile

class FieldFile
当你访问一个模型上的 FileField 时，你会得到一个 FieldFile 的实例作为访问底层文件的代理。

FieldFile 的 API 与 File 的 API 相同，但有一个关键的区别。该类所封装的对象不一定是 Python 内置文件对象的封装 相反，它是 Storage.open() 方法结果的封装，该方法可能是 File 对象，也可能是自定义存储对 File API 的实现。

除了从 File 继承的 API，如 read() 和 write() 之外，FieldFile 还包括一些可以用来与底层文件交互的方法：

警告

该类的两个方法 save() 和 delete()，默认为将与相关 FieldFile 的模型对象保存在数据库中。

FieldFile.name
文件名，包括从关联的 Storage 的根部开始的相对路径 FileField。

FieldFile.path
一个只读属性，通过调用底层的 path() 方法，访问文件的本地文件系统路径。

FieldFile.size
底层 Storage.size() 方法的结果。

FieldFile.url
一个只读属性，通过调用底层 Storage 类的 Storage() 方法来访问文件的相对 URL。

FieldFile.open(mode='rb')
以指定的 mode 打开或重新打开与该实例相关的文件。与标准的 Python open() 方法不同，它不返回一个文件描述符。

因为在访问底层文件时，底层文件是隐式打开的，所以除了重置底层文件的指针或改变 mode 之外，可能没有必要调用这个方法。

FieldFile.close()
类似于标准的 Python file.close() 方法，关闭与该实例相关的文件。

FieldFile.save(name, content, save=True)
这个方法接收一个文件名和文件内容，并将它们传递给字段的存储类，然后将存储的文件与模型字段关联。如果你想手动将文件数据与模型上的 FileField 实例关联起来，那么 save() 方法用来持久化该文件数据。

取两个必要的参数。name 是文件的名称，content 是包含文件内容的对象。 可选的 save 参数控制在与该字段相关联的文件被更改后是否保存模型实例。默认为 True。

注意 content 参数应该是 django.core.files.File 的实例，而不是 Python 内置的文件对象。你可以从现有的 Python 文件对象构造一个 File，像这样：

from django.core.files import File

Open an existing file using Python's built-in open()
f = open('/path/to/hello.world')
myfile = File(f)
或者你可以从 Python 字符串中构建一个像这样的字符串：

from django.core.files.base import ContentFile
myfile = ContentFile("hello world")
更多信息，请参见 管理文件。

FieldFile.delete(save=True)
删除与此实例相关的文件，并清除字段的所有属性。注意：如果在调用 delete() 时，文件恰好被打开，本方法将关闭该文件。

可选的 save 参数控制在删除与该字段相关的文件后是否保存模型实例。默认值为 True。

请注意，当一个模型被删除时，相关文件不会被删除。如果你需要清理遗留文件，你需要自己处理（例如，使用自定义管理命令，可以手动运行或通过例如 cron 定期运行）。

###### FilePathField

class FilePathField(path='', match=None, recursive=False, allow_files=True, allow_folders=False, max_length=100,\ *\*options)
一个 CharField，其选择仅限于文件系统中某个目录下的文件名。有一些特殊的参数，其中第一个参数是 必须的。

FilePathField.path
必须的。一个目录的绝对文件系统路径，这个 FilePathField 应从该目录中获取其选择。例如："/home/images"。

path 也可以是一个可调用对象，可以是在运行时动态设置路径的函数。例如：

import os
from django.conf import settings
from django.db import models

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class MyModel(models.Model):
    file = models.FilePathField(path=images_path)
FilePathField.matc
可选。一个正则表达式，作为一个字符串， FilePathField 将用于过滤文件名。请注意，正则表达式将被应用于基本文件名，而不是完整的路径。例如："foo.*.txt$"，它将匹配名为 foo23.txt 的文件，但不匹配 bar.txt 或 foo23.png。

FilePathField.recursive
可选。True 或 False。默认为 False。指定是否包含 path 的所有子目录。

FilePathField.allow_files
可选。 True 或 False。 默认值是 True。 指定是否应该包含指定位置的文件。 这个或 allow_folders 必须是 True。

FilePathField.allow_folders
可选。 True 或 False。 默认为 False。 指定是否应该包含指定位置的文件夹。 这个或 allow_files 必须是 True。

一个潜在的问题是 match 适用于基本文件名，而不是完整的路径。所以，这个例子：

FilePathField(path="/home/images", match="foo.*", recursive=True)
...将匹配 /home/images/foo.png，但不匹配 /home/images/foo/bar.png，因为 match 适用于基本文件名（ foo.png 和 bar.png ）。

FilePathField 实例在数据库中作为 varchar 列创建，默认最大长度为 100 个字符。与其他字段一样，你可以使用 max_length 参数改变最大长度。

###### FloatField

class FloatField(\*\*options)
在 Python 中用一个 float 实例表示的浮点数。

当 localize 为 False 时是 NumberInput 否则，该字段的默认表单部件是 TextInput。

FloatField vs. DecimalField

FloatField 类有时会与 DecimalField 类混淆。虽然它们都表示实数，但它们表示的方式不同。FloatField 内部使用 Python 的 float 类型，而 DecimalField 则使用 Python 的 Decimal 类型。关于两者之间的区别，请参见 Python 的 decimal 模块的文档。

###### ImageField

class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, \*\*options)
继承 FileField 的所有属性和方法，但也验证上传的对象是有效的图像。

除了 FileField 的特殊属性外， ImageField 也有 height 和 width 属性。

为了方便查询这些属性，ImageField 有两个额外的可选参数。

ImageField.height_field
模型字段的名称，每次保存模型实例时将自动填充图像的高度。

ImageField.width_field
模型字段的名称，每次保存模型实例时将自动填充图像的宽度。

需要 Pillow 库。

ImageField 实例在数据库中创建为 varchar 列，默认最大长度为 100 个字符。与其他字段一样，你可以使用 max_length 参数改变最大长度。

该字段的默认表单部件是一个 ClearableFileInput。

###### IntegerField

class IntegerField(\*\*options)
一个整数。从 -2147483648 到 2147483647 的值在 Django 支持的所有数据库中都是安全的。

它使用 MinValueValidator 和 MaxValueValidator 根据默认数据库支持的值来验证输入。

当 localize 为 False 时是 NumberInput 否则，该字段的默认表单部件是 TextInput。

###### GenericIPAddressField

class GenericIPAddressField(protocol='both', unpack_ipv4=False, **options)¶
IPv4 或 IPv6 地址，字符串格式（如 192.0.2.30 或 2a02:42fe::4 ）。该字段的默认表单部件是一个 TextInput。

IPv6 地址规范化遵循 RFC 4291#section-2.2 第 2.2 节，包括使用该节第 3 段建议的 IPv4 格式，如 ::fffff:192.0.2.0。例如，2001:0::0:01 将被标准化为 2001::1，::fffff:0a0a:0a0a 将被标准化为 ::fffff:10.10.10.10。所有字符都转换为小写。

GenericIPAddressField.protocol¶
将有效输入限制为指定协议。接受的值是 'both' （默认）、'IPv4' 或 'IPv6'。匹配是不分大小写的。

GenericIPAddressField.unpack_ipv4¶
解压 IPv4 映射地址，如 ::fffff:192.0.2.1。如果启用该选项，该地址将被解压为 192.0.2.1。默认为禁用。只有当 protocol 设置为 'both' 时才会启用。

如果允许空值，就必须允许 null 值，因为空值会被存储为 null。

###### JSONField

class JSONField(encoder=None, decoder=None, **options)¶
New in Django 3.1.
一个用于存储 JSON 编码数据的字段。在 Python 中，数据以其 Python 本地格式表示：字典、列表、字符串、数字、布尔值和 None。

JSONField 在 MariaDB 10.2.7+、MySQL 5.7.8+、Oracle、PostgreSQL 和 SQLite（在 JSON1 扩展被启用的情况下）都支持。

JSONField.encoder¶
一个可选的 json.JSONEncoder 子类，用于序列化标准 JSON 序列化器不支持的数据类型（例如 datetime.datetime 或 UUID ）。例如，你可以使用 DjangoJSONEncoder 类。

默认为 json.JSONEncoder。

JSONField.decoder¶
一个可选的 json.JSONDecoder 子类，用于反序列化从数据库中获取的值。该值将采用自定义编码器选择的格式（通常是字符串）。你的反序列化可能需要考虑到你无法确定输入类型的事实。例如，你有可能返回一个 datetime，实际上是一个字符串，而这个字符串恰好与 datetime 选择的格式相同。

默认为 json.JSONDecoder。

如果你给字段一个 default，确保它是一个不可变的对象，比如 str，或者是一个每次返回一个新的可变对象的可调用对象，比如 dict 或一个函数。提供一个像 default={} 或 default=[] 这样的可改变的默认对象，在所有模型实例之间共享一个对象。

要在数据库中查询 JSONField，请看 查询 JSONField。

索引

Index 和 Field.db_index 都创建了一个 B 树索引，在查询 JSONField 的时候并不是特别有用。仅在 PostgreSQL 上，可以使用 GinIndex 比较适合。

PostgreSQL 用户

PostgreSQL 有两种基于 JSON 的原生数据类型： json 和 jsonb。json 和 jsonb。它们之间的主要区别在于它们的存储方式和查询方式。PostgreSQL 的 json 字段是作为 JSON 的原始字符串表示来存储的，当根据键来查询时，必须同时进行解码。jsonb 字段是基于 JSON 的实际结构存储的，它允许索引。这样做的代价是在写入 jsonb 字段时增加了一点成本。JSONField 使用 jsonb。

Oracle 用户

Oracle 数据库不支持存储 JSON 标量值。只支持 JSON 对象和数组（在 Python 中使用 dict 和 list 表示)。

###### NullBooleanField

class NullBooleanField(**options)¶
就像 BooleanField 的 null=True。

3.1 版后已移除:
NullBooleanField 已被废弃，改为 BooleanField(null=True)。

###### PositiveBigIntegerField¶
class PositiveBigIntegerField(**options)¶
New in Django 3.1.
就像一个 PositiveIntegerField，但只允许在某一特定点下的值（依赖于数据库）。0 到 9223372036854775807 的值在 Django 支持的所有数据库中都是安全的。

###### PositiveIntegerField¶
class PositiveIntegerField(**options)¶
就像 IntegerField 一样，但必须是正值或零（ 0 ）。从 0 到 2147483647 的值在 Django 支持的所有数据库中都是安全的。出于向后兼容的原因，接受 0 的值。

###### PositiveSmallIntegerField¶
class PositiveSmallIntegerField(**options)¶
就像一个 PositiveIntegerField，但只允许在某一特定（数据库依赖的）点下取值。0 到 32767 的值在 Django 支持的所有数据库中都是安全的。

###### SlugField¶
class SlugField(max_length=50, **options)¶
Slug 是一个报纸术语。slug 是一个简短的标签，只包含字母、数字、下划线或连字符。它们一般用于 URL 中。

像 CharField 一样，你可以指定 max_length （也请阅读那一节中关于数据库可移植性和 max_length 的说明）。如果没有指定 max_length，Django 将使用默认长度 50。

意味着将 Field.db_index 设置为 True。

基于其他值的值自动预填充一个 SlugField 通常是很有用的。 你可以在管理中使用 prepopulated_fields 来自动完成。

它使用 validate_slug 或 validate_unicode_slug 进行验证。

SlugField.allow_unicode¶
如果是 True，该字段除了接受 ASCII 字母外，还接受 Unicode 字母。默认值为 False。

###### SmallAutoField¶
class SmallAutoField(**options)¶
就像一个 AutoField，但只允许值在一定（依赖于数据库）的限制下。1 到 32767 的值在 Django 支持的所有数据库中都是安全的。

###### SmallIntegerField¶
class SmallIntegerField(**options)¶
就像一个 IntegerField，但只允许在某一特定（依赖于数据库的）点下取值。从 -32768 到 32767 的值在 Django 支持的所有数据库中都是安全的。

###### TextField¶
class TextField(**options)¶
一个大的文本字段。该字段的默认表单部件是一个 Textarea。

如果你指定了 max_length 属性，它将反映在自动生成的表单字段的 Textarea 部件中。但是，它并没有在模型或数据库层面被强制执行。使用一个 CharField 来实现。

TextField.db_collation¶
New in Django 3.2.
该字段的数据库字符序名称。

注解

字符序名称是不标准化的。因此，这将无法在多个数据库后端之间进行移植。

Oracle

Oracle 不支持 TextField 的字符序。

###### TimeField¶
class TimeField(auto_now=False, auto_now_add=False, **options)¶
一个时间，在 Python 中用 datetime.time 实例表示。接受与 DateField 相同的自动填充选项。

该字段默认的表单部件t是一个 TimeInput。管理中添加了一些 JavaScript 快捷方式。

###### URLField¶
class URLField(max_length=200, **options)¶
URL 的 CharField，由 URLValidator 验证。

该字段的默认表单部件是一个 URLInput。

像所有的 CharField 子类一样， URLField 接受可选的 max_length 参数。如果你没有指定 max_length 参数，则使用默认的 200。

###### UUIDField¶
class UUIDField(**options)¶
一个用于存储通用唯一标识符的字段。使用 Python 的 UUID 类。当在 PostgreSQL 上使用时，它存储在一个 uuid 的数据类型中，否则存储在一个 char(32) 中。

通用唯一标识符是 primary_key 的 AutoField 的一个很好的替代方案。数据库不会为你生成 UUID，所以建议使用 default ：

import uuid
from django.db import models

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # other fields
请注意，一个可调用对象（省略括号）被传递给 default，而不是 UUID 的实例。

在 PostgreSQL 上查找

在 PostgreSQL 上使用 iexact、contains、icontains、startswith、istartswith、endswith 或 iendswith 在 PostgreSQL 上查找没有连字符的值是行不通的，因为 PostgreSQL 将它们存储在一个连字符的 uuid 数据类型中。

















下面这个好像不属于这里



###### Model.save()

[Model.save(force_insert=False, force_update=False, using=DEFAULT_DB_ALIAS, update_fields=None)](https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#django.db.models.Model.save)

For details on using the `force_insert` and `force_update` arguments, see [强制执行 INSERT 或 UPDATE](https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#ref-models-force-insert). Details about the `update_fields` argument can be found in the [指定要保存的字段](https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#ref-models-update-fields) section.

如果你想自定义保存行为，你可以覆盖这个 `save()` 方法。更多细节请参见 [重写之前定义的模型方法](https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/#overriding-model-methods)。








##### 3、模型中的字段选项



关于类中的字段

每个字段都应该是 Field 类的实例



有一些选项


- max_length	指定该字段长度
- db_index	True表示将为此字段建索引
- default	该字段的默认值 。可以是可调用对象，但是默认不可变
- primary_key	为True时，表示将该字段设置为主键。同时表示 null=False 和 unique=True 如果该模型中一个主键都没有设置，那么将会自动添加一个字段来设置主键。主键字段是只读的。如果改变了现有对象的主键值，然后将其保存，则会在旧对象旁边创建一个新对象。
- verbose_name	该字段的含义

- unique	设置为True，表示字段必须在整个表中保持值唯一。属于数据库级别和模型验证中强制执行。

- unique_for_date	将其设置为 DateField 或 DateTimeField 的名称，要求该字段的日期字段值是唯一的。
- unique_for_month	与上一个一致，区别为要求月份唯一
- unique_for_year	要求年份唯一
- null	如果设置为True，表示当该字段为空时，Django会将数据库中该字段设置为NULL。默认False
- blank	默认False。True表示该字段允许为空。
	与null的区别是，null仅表示数据库层面的空，而 blank涉及表单验证，为Flase表示表单该字段必填	

- db_column	字段使用的数据库列名，未指定时使用数据库名
- db_tablespace	如果这个字段有索引，那么要为这个字段的索引使用的 数据库表空间 的名称。默认是项目的 DEFAULT_INDEX_TABLESPACE （如果有设置）,或者是模型的 db_tablespace （如果有）。如果后端不支持索引的表空间，则忽略此选项。
	这里其实没搞懂为啥索引也有表空间，搜了一下暂时没得到答案。[mysql的表空间使用](https://blog.csdn.net/finalkof1983/article/details/83829341)
	
- editable	默认为True。 False表示该字段不会在管理或者任何其他地方中显示
- error_messages	覆盖该字段引发的默认消息。传入一个与你想覆盖的错误信息相匹配的键值的字典。
	这里也没懂啥意思 -_- ，可参考[error_messages](https://docs.djangoproject.com/zh-hans/3.2/topics/forms/modelforms/#considerations-regarding-model-errormessages)
	
- help_text	额外的帮助文档，随表单控件一起显示。即便字段未用与表单，对于生成文档也可用。
	这个也没懂 ^_^
	
- validators	要为该字段运行的验证器列表。更多信息请参见 [验证器文档](https://docs.djangoproject.com/zh-hans/3.2/ref/validators/) 
	这个有点深，表示自定义验证机制



参考
[Django模型字段](https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#model-field-types)



###### 字段选项，部分解释



####### 1、null

默认 Flase，当设置 null=True ，当该字段为空时，将数据库中对应的字段设置为空



####### 2、blank

默认 Flase，当设置 blank=True，该字段允许为空

与null不同的是，null只是数据库层面的设置，blank是表单验证时候是否允许为空



####### 3、choices

一系列二元数组，在表单上表示为选择框

如，一个选项列表

```
from django.db import models

class Person(models.Model):
    # 一个选项列表
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```



注意，当choices的顺序变动时，将创建新的迁移



当代码包含此字段时，可以使用 get\_定义值\_dispaly 来获取响应的结果，如

```
>>> p = Person(name="Fred Flintstone", shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'
```





####### 4、default

该字段的默认值





####### 5、help-text

表单使用的额外帮助文档





####### 6、primary_key

设置为Ture，表示为此模型的主键

整个模型未显式设置，将会自动添加一个 IntegerFiled的字段并设置为主键



注意，主键字段只读，当修改时，会创建一个新的值（原来的值保留）





####### 7、unique

设置为True表示，此字段的值在表中是保持唯一





####### 8、verbose_name

字段备注名

（相当于给他一个注释）





####### 9、through

仅用于多对多字段中

指定使用哪个模型





##### 4、模型中的一些函数/方法



`__str__()`

返回值表示这个对象



`get_absolute_url()`

计算一个对象的url

任何需要一个唯一url的都需要定义此方法





##### 5、自定义sql



`Manager.raw(raw_query,params=(),translations=None)`

如：

```
>>> Person.objects.raw('''SELECT first AS first_name,
...                              last AS last_name,
...                              bd AS birth_date,
...                              pk AS id,
...                       FROM some_other_table''')
```



带参

```
>>> lname = 'Doe'
>>> Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
```



参考

[执行原生 SQL 查询 | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/3.2/topics/db/sql/)





##### 6、抽象基类

抽象基类在你要将公共信息放入很多模型时会很有用。编写你的基类，并在 [Meta](https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/#meta-options) 类中填入 `abstract=True`。该模型将不会创建任何数据表。当其用作其它模型类的基类时，它的字段会自动添加至子类。

如：

```
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```

`Student` 模型拥有3个字段： `name`， `age` 和 `home_group`。 `CommonInfo` 模型不能用作普通的 Django 模型，因为它是一个抽象基类。它不会生成数据表，也没有管理器，也不能被实例化和保存。

从抽象基类继承来的字段可被其它字段或值重写，或用 `None` 删除。

对很多用户来说，这种继承可能就是你想要的。它提供了一种在 Python 级抽出公共信息的方法，但仍会在子类模型中创建数据表。



#### 模型类内部类Meta



##### 可用的选项



####### abstract

abstract = True，表示这是一个抽象基类



####### app_label



如果在 INSTALLED_APPS 中定义了一个应用程序之外的模型，它必须声明它属于哪个应用程序：


```
app_label = 'myapp'
```

如果你想用 app_label.object_name 或 app_label.model_name 来表示一个模型，你可以分别使用 model.\_meta.label 或 model.\_meta.label_lower。




####### db_table

用于模型的数据库表的名称



####### base_manager_name

管理器的属性名

管理器的属性名，例如，'objects'，用于模型的 _base_manager。

说实话 没懂




####### db_tablespace

数据库表空间名称

[表空间（Tablespaces） | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/3.2/topics/db/tablespaces/)




####### default_manager_name

模型的管理器名称

模型的 [\_default_manager](https://docs.djangoproject.com/zh-hans/3.2/topics/db/managers/#django.db.models.Model._default_manager) 管理器名称。




####### default_related_name

从相关对象到这个对象的关系默认使用的名称。默认为 `_set`。

这个选项还可以设置 [related_query_name](https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#django.db.models.ForeignKey.related_query_name)。

由于字段的反向名称应该是唯一的，所以如果你打算对你的模型进行子类化，就要小心了。为了避免名称冲突，名称的一部分应该包含 `'%(app_label)s'` 和 `'%(model_name)s'`，它们分别被模型所在的应用程序的名称和模型的名称所取代，都是小写的。见 [抽象模型的相关名称](https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/#abstract-related-name) 段落。




####### get_latest_by

模型中的字段名或字段名列表

我的理解是 以这个字段集进行排序




####### managed

默认为True，表示Django 管理 数据库表的生命周期。

如果 False，将不对该模型进行数据库表的创建、修改或删除操作。如果该模型代表一个现有的表或一个通过其他方式创建的数据库视图，这一点很有用。这是在 managed=False 时 唯一 的区别。模型处理的所有其他方面都与正常情况完全相同。




####### order_with_respect_to

使该对象可以根据给定字段（通常是 ForeignKey ）进行排序。




####### ordering

对象的默认排序




####### permissions

表的额外权限

创建此对象时要输入权限表的额外权限。为每个模型自动创建添加、更改、删除和查看权限。这个例子指定了一个额外的权限，can_deliver_pizzas ：
```
permissions = [('can_deliver_pizzas', 'Can deliver pizzas')]
```
这是一个由二元元组组成的列表或元组，格式为 (permission_code, human_readable_permission_name)。





####### default_permissions

默认值为 ('add', 'change', 'delete', 'view') 。
你可以自定义这个列表，例如，如果你的应用不需要任何默认的权限，可以将其设置为空列表。它必须在模型创建之前通过 migrate 在模型上指定，以防止任何遗漏的权限被创建。





####### proxy

如果 `proxy = True`，作为另一个模型子类的模型将被视为 [代理模型](https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/#proxy-models)。





####### required_db_features

当前连接应具备的数据库特征列表，以便在迁移阶段考虑模型。例如，如果你将此列表设置为 ['gis_enabled']，则模型将只在支持 GIS 的数据库上同步。在使用多个数据库后端进行测试时，跳过一些模型也很有用。避免模型之间的关系，这些模型可能会被创建，也可能不会被创建，因为 ORM 不会处理这个问题。




####### required_db_vendor

本模型所特有的支持的数据库厂商名称。目前的内置厂商名称是： `sqlite`，`postgresql`，`mysql` 和 `oracle`。如果该属性不为空，且当前连接厂商与之不匹配，则该模型将不会同步。





####### select_on_save

确定 Django 是否会使用 1.6 之前的 [django.db.models.Model.save()](https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#django.db.models.Model.save) 算法。旧的算法使用 `SELECT` 来确定是否有一条现有的记录需要更新。新算法直接尝试 `UPDATE`。在一些罕见的情况下，Django 看不到现有行的 `UPDATE`。例如 PostgreSQL 的 `ON UPDATE` 触发器会返回 `NULL`。在这种情况下，即使数据库中存在一条记录，新算法最终也会进行 `INSERT`。

通常不需要设置这个属性。默认值是 `False`。

关于新旧保存算法，请参见 [django.db.models.Model.save()](https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#django.db.models.Model.save)。





####### indexes

定义索引列表

如

```
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]
```





####### unique_together

一组字段名，组合起来必须是唯一的





####### index_together

可以理解为联合索引





####### constraints

表约束




####### verbose_name

对象的注释 单数




####### verbose_name_plural

对象的复数，默认是上一个加s




####### label

对象的表示，返回 app_label.object_name，例如 'polls.Question'。





####### label_lower

模型的表示，返回 app_label.model_name，例如 'polls.question'。











### 后台管理模块admin







这里其实对应的就是 应用中的 admin.py



###### 1、常用字段



例子：

```
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
```



可以自行设置自定义的后台表单

如例所示，自定义的类需要 register 在基类之后

类中字段定义方法：



####### 1、fields

```
fields = ['pub_date', 'question_text']
```

表示前台直接展示的字段以及顺序

主要用于新增



####### 2、fieldsets

```
fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
```

表示将这些字段分成几个字段集

其中每个元组中第一个元素表示这个集的标题

主要用于新增



####### 3、list_display

```
list_display = ('question_text', 'pub_date')
```

表示在前台展示一个可视化的字段列表

主要用于表格化的展示



####### 4、list_filter

```
list_filter = ['pub_date']
```

表示允许在前端使用此字段的过滤选项（在侧边栏显示过滤选项）



####### 5、search_fields

```
search_fields = ['question_text']
```

表示前端新增此字段的搜索框（后端将使用like查询）







###### 2、自定义后台界面风格

通过 Django 的模板系统来修改。

Django 的后台由自己驱动，且它的交互接口采用 Django 自己的模板系统。



在包含 manage.py 的工程目录内创建一个 templates 目录，放模板资源吧



在 settings.py 配置 DIRS选项

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



TEMPLATES 作用：

包含所有 Django 模板引擎的配置的列表。列表中的每一项都是一个字典，包含了各个引擎的选项。



[DIRS](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-TEMPLATES-DIRS) 是一个包含多个系统目录的文件列表，用于在载入 Django 模板时使用，是一个待搜索路径。







参考

[自定义后台表单](https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial07/)









[执行原生 SQL 查询 | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/3.2/topics/db/sql/))









### settings常用字段



  

###### 1、TEMPLATES

默认： `[]` （空列表）

一个包含所有 Django 模板引擎的配置的列表。列表中的每一项都是一个字典，包含了各个引擎的选项。

下面是一个配置，告诉 Django 模板引擎从每个安装好的应用程序中的 `templates` 子目录中加载模板：

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]
```

以下选项适用于所有后端。



####### 1、BACKEND

默认：未定义

要使用的模板后端。内置的模板后端有：

- `'django.template.backends.django.DjangoTemplates'`
- `'django.template.backends.jinja2.Jinja2'`

你可以通过将 `BACKEND` 设置为一个完全限定的路径（例如 `'mypackage.whatever.Backend'`）来使用一个不在 Django 中的模板后端。



####### 2、NAME

默认：见下方

这个特定模板引擎的别称。它是一个标识符，允许选择一个引擎进行渲染。所有配置的模板引擎的别名必须是唯一的。

它默认为定义引擎类的模块名称，即 [`BACKEND` 的下一个到最后一个，如果没有提供的话。例如，如果后端是 `'mypackage.whatever.Backend'`，那么它的默认名称是 `'whatever'`。



####### 3、DIRS

默认： `[]` （空列表）

按照搜索顺序，引擎应该查找模板源文件的目录。



####### 4、APP_DIRS

默认：`False`

引擎是否应该在已安装的应用程序中查找模板源文件。

注解

默认的 `settings.py` 文件由 `django-admin startproject` 创建，设置 `'APP_DIRS': True`。



####### 5、OPTIONS

默认值： `{}` （空字典）

要传递给模板后台的额外参数。根据模板后端的不同，可用的参数也不同。参见 [DjangoTemplates](https://docs.djangoproject.com/zh-hans/3.2/topics/templates/#django.template.backends.django.DjangoTemplates) 和 [Jinja2](https://docs.djangoproject.com/zh-hans/3.2/topics/templates/#django.template.backends.jinja2.Jinja2) 了解内置后端的选项。





参考

[setting配置](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-TEMPLATES)







### 应用打包





使用 setuptools 打包



1、建立一个文件夹放模块

2、将模块目录移入这个新建的目录

3、在新建目录下创建一个 README.rst 文件，包含以下内容

```rst
=====
Polls
=====

Polls is a Django app to conduct Web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
```



4、在同一目录下创建 LICENSE 文件。选择一个授权协议（这里暂时不知道怎么搞）



5、创建 setup.cfg 和 setup.py 说明构建与安装的细节。可参考  [setuptools docs](https://setuptools.readthedocs.io/en/latest/) 。

大致包含以下内容

setup.cfg

```cfg
[metadata]
name = django-polls
version = 0.1
description = A Django app to conduct Web-based polls.
long_description = file: README.rst
url = https://www.example.com/
author = Your Name
author_email = yourname@example.com
license = BSD-3-Clause  # Example license
classifiers =
    Environment :: Web Environment
    Framework :: Django
    Framework :: Django :: X.Y  # Replace "X.Y" as appropriate
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Operating System :: OS Independent
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Topic :: Internet :: WWW/HTTP
    Topic :: Internet :: WWW/HTTP :: Dynamic Content

[options]
include_package_data = true
packages = find:
python_requires = >=3.6
install_requires =
    Django >= X.Y  # Replace "X.Y" as appropriate
```



setup.py

```
from setuptools import setup

setup()
```



6、默认情况，包中仅包含 Python 模块和包。要包含其他文件，我们需要创建一个`MANIFEST.in` 文件。 上一步中提到的 setuptools 文档更详细地讨论了这个文件。 要包含模板、`README.rst` 和我们的 `LICENSE` 文件，创建一个文件 `MANIFEST.in` ，其内容如下：


    include LICENSE
    include README.rst
    recursive-include polls/static *
    recursive-include polls/templates *



7、在应用中包含详细文档是可选的，但我们推荐你这样做。新建目录下创建一个空目录 `docs` 用于未来编写文档。额外添加一行至 `MANIFEST.in`

```
recursive-include docs *
```

注意，现在 `docs` 目录不会被加入你的应用包，除非你往这个目录加几个文件。许多 Django 应用也提供他们的在线文档通过类似 [readthedocs.org](https://readthedocs.org/) 这样的网站。



8、试着构建你自己的应用包通过 ptyhon setup.py sdist（在  django-polls 目录内）。这将创建一个名为 `dist` 的目录并构建你自己的应用包， `django-polls-0.1.tar.gz`。

更多关于打包的信息，见 Python 的 [关于打包和发布项目的教程](https://packaging.python.org/tutorials/packaging-projects/)。







### 其他



##### 缓存模块的问题

使用的 LocMemCache 是不能作同步缓存的

注意每个进程都有自己的私有缓存实例，这意味着不可能有跨进程缓存

所以说，**LocMemCache是不能用来做同步缓存的! 请使用别的任意Cache!**





可以参考以下链接使用其他的缓存





参考：

[震惊！Django缓存中的数据频频丢失，究竟谁是幕后黑手](https://cloud.tencent.com/developer/article/1005556)

[使用其他的缓存](https://segmentfault.com/a/1190000016095832)

[Django项目如何配置Memcached和Redis缓存?哪个更好?](https://blog.csdn.net/weixin_42134789/article/details/115474919)

[Redis和Memcache的区别分析](https://www.1024sou.com/article/35125.html)







##### 测试

一份好的业务代码，是需要经过实际测试的。

一方面是自己确认代码运行正常，另一方面是对外提供测试信息。



###### 编写方法

一般来说，Django的测试用例应该定义在应用的 tests.py 文件里。

系统会自动在以 tests 开头的文件里寻找并执行测试代码。



比如有一个 polls 的django应用，将以下代码写入 tests.py

```
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```



解读：

创建一个 django.test.TestCase 的子类，并添加一个方法，此方法创建一个 pub_date 时未来某天的 `Question` 实例。然后检查它的 `was_published_recently()` 方法的返回值——它 *应该* 是 False。



###### 运行测试

在终端中，我们通过输入以下代码运行测试:

```
$ python manage.py test polls
```

你将会看到运行结果:

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/path/to/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```



以下是自动化测试的运行过程：

- `python manage.py test polls` 将会寻找 `polls` 应用里的测试代码
- 它找到了 [`django.test.TestCase`](https://docs.djangoproject.com/zh-hans/3.2/topics/testing/tools/#django.test.TestCase) 的一个子类
- 它创建一个特殊的数据库供测试使用
- 它在类中寻找测试方法——以 `test` 开头的方法。
- 在 `test_was_published_recently_with_future_question` 方法中，它创建了一个 `pub_date` 值为 30 天后的 `Question` 实例。
- 接着使用 `assertls()` 方法，发现 `was_published_recently()` 返回了 `True`，而我们期望它返回 `False`。

测试系统通知我们哪些测试样例失败了，和造成测试失败的代码所在的行号。







参考

[自动化测试简介](https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial05/)







### 附1：常用指令

```
# 查看django位置
python -c "import django; print(django.__path__)"

# 打开django自带的命令行工具
python manage.py shell

# 启动 polls应用的自动化测试
python manage.py test polls
```



```
# 创建 django 项目
$ django-admin startproject $pro

# 安装模块app
$ python manage.py startapp $app

# 启动服务
$ python manage.py runserver 0:8000

# 查找所有可用的模型 为任意一个在数据库中不存在对应数据表的模型创建迁移脚本文件
$ python manage.py makemigrations

# 运行这些迁移来自动创建数据库表
#  migrate 命令只会为在 INSTALLED_APPS 里声明了的应用进行数据库迁移。
$ python manage.py migrate

# 创建某个app的表结构
$ python manage.py makemigrations $app
$ python manage.py migrate

# 含 django 的环境变量shell
$ python manage.py shell
```



url path 四个参数

```
# view 可以是 使用 include() 使用其他的app下的url
# name 别名
path('route', view.fun, name='')
```



创建管理员用户

```
$ python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
```



数据库的设置 setting.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```



默认的，Django 会在外键字段名后追加字符串 `"_id"` 。（同样，这也可以自定义。）







### 附2：QuerySet Api



包含两个公开属性：

- ordered：查询时候是否有序（True/False）
- db：查询时使用的数据库





#### 模型.objects的一些方法



每次执行都是返回一个新的QuerySet()



总览

- module.objects.all() 获取该实例的所有信息
- module.objects.add() 添加
- module.objects.create() 创建
- module.objects.get() 
- module.objects.filter(*kargs)	过滤器 返回包含指定参数的QuerySet，底层通过AND连接多个参数
- module.objects.exclude(*kargs)	返回不包含指定参数的QuerySet，底层是用NOT()包裹的AND
- module.objects.annotate()	聚合查询，对QuerySet的每个对象进行注解
- module.objects.order_by() 排序
- module.objects.annotate()
- module.objects.alias()	对QuerySet的每个字段设置别名，相当于as（没搞懂）
- module.objects.select_related()	会获取外键对应的对象，在需要的时候就不用重新查询数据库了（主要用于一对多字段的查询）
- module.objects.prefetch_related()	多对多字段的查询（通过外键所对应实体找外键所在实体），底层使用的in 
- module.objects.reverse()	反向查询
- module.objects.distinct( \*fields )	反向查询
- module.objects.values()	返查询字典而不是实例
- module.objects.defer()	单次加载时，指定不加载指定的字段，后续是需要时再加载
- module.objects.only()	单次加载时，指定加载指定的字段，未指定的需要再加载
- module.objects.extra()
- 





[所有查询操作参考](https://www.liujiangblog.com/course/django/129)



####### 1、module.objects.all() 

获取该实例的所有信息



注意：

```
Entry.objects.filter(pub_date__year=2006)
```

等价于

```
Entry.objects.all().filter(pub_date__year=2006)
```



####### 2、module.objects.add() 

添加



####### 3、module.objects.create() 

创建



####### 4、module.objects.get() 



####### 5、module.objects.filter(*kargs)	

过滤器 返回包含指定参数的QuerySet，底层通过AND连接多个参数

如果是多个filter，那么这些filter的链之间是或的关系（or）



####### 6、module.objects.exclude(*kargs)	

返回不包含指定参数的QuerySet，底层是用NOT()包裹的AND



####### 7、module.objects.annotate()	

聚合查询，对QuerySet的每个对象进行注解



####### 8、module.objects.order_by() 

排序



####### 9、module.objects.annotate()



####### 10、module.objects.alias()	

对QuerySet的每个字段设置别名

好像相当于as（没搞懂）



####### 11、module.objects.select_related()	

会获取外键对应的对象，

在需要的时候就不用重新查询数据库了（主要用于一对多字段的查询）



####### 12、module.objects.prefetch_related()	

多对多字段的查询

（通过外键所对应实体找外键所在实体），底层使用的in 



####### 13、module.objects.reverse()	

反向查询



####### 14、module.objects.distinct( *fields )	

反向查询



####### 15、module.objects.values()	

返查询字典而不是实例

注意values与distinct使用会影响排序结果



####### 16、module.objects.defer()	

返回对象实例，指定不加载字段

单次加载时，指定不加载指定的字段，后续是需要时再加载



####### 17、module.objects.only()	

返回对象实例，指定加载字段

单次加载时，指定加载指定的字段，未指定的需要再加载

多个链式的only，只会以最后一个为准



> 比如:ret=Book.object.all().only('name')
>         id始终会查,结果是queryset对象,套book对象(里面只有id与name字段)
>         问:如果取price,发生了什么?
>         它会再次查询数据库,对数据库造成压力



####### 18、extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)

有时候，Django 查询语法本身并不能很容易地表达一个复杂的 WHERE 子句。对于这些边缘情况，Django 提供了 extra() QuerySet 修饰符——用于将特定的子句注入到由 QuerySet 生成的 SQL 中。

如果在 extra() 调用之后使用 values() 子句，则 extra() 中的 select 参数所定义的任何字段必须明确地包含在 values() 调用中。任何在 values() 调用之后进行的 extra() 调用将忽略其额外选择的字段。

官网文档说计划 extra将在未来废弃










##### filter/other

过滤后的QuerySet都是唯一的

前缀为变量或者说字段名

后缀如下：

- `__gt` : 大于
- `__gte` : 大于等于
- `__lt` : 小于
- `__lte` : 小于等于
- `__in` : 其中之一
- `__range` : 范围
- `__year` : 日期-年

- `__exact`：“精确”匹配（区分大小写）

- `__iexact`：是不区分大小写的匹配项

- `__contains`：区分大小写的模糊查询

- `__icontains`：不区分大小写的模糊查询，与`contains`相对应。
- `__startswith`：以什么开头的模糊查询（**区分大小写**）
- `__istartswith`：以什么开头的模糊查询（**不区分大小写**）
- `__endswith`：以什么结尾的模糊查询（**区分大小写**）
- `__iendswith`：以什么结尾的模糊查询（**不区分大小写**）
- `__isnull` : 是空的
- `__regex` : 区分大小写的正则匹配
- `__iregex` : 不区分大小写的正则匹配





### 附3：创建虚拟环境



用于创建和管理虚拟环境的模块称为[venv](https://docs.python.org/3/library/venv.html#module-venv)。[ venv](https://docs.python.org/3/library/venv.html#module-venv)通常会安装您可用的最新版本的Python。如果您的系统上有多个版本的Python，则可以通过运行或所需的任何版本来选择特定的Python版本。`python3`

要创建虚拟环境，请确定要放置它的目录，然后将[venv](https://docs.python.org/3/library/venv.html#module-venv)模块作为脚本运行

```
# 创建环境位置 常用 .开始，以区分环境变量
python3 -m venv $mydir
```



启动

```
# 如果是windows
$mydir/scripts/activate.bat

# 如果是 linux
source $mydr/bin/activate
```







[使用虚拟工具安装包创建隔离的python环境](https://docs.python.org/3/tutorial/venv.html)





### 附4：F Q

#### F

##### 1、F支持表内部字段的比较	单下划线

例如，为了查找comments数目多于pingbacks数目的Entry，可以构造一个F()对象来引用pingback数目，并在查询中使用该F()对象：

Entry有两个字段 number_of_comments，number_of_pingbacks

> from django.db.models import F
> Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))
> 

ps： 也支持加减乘除
如：查询rating比pingback和comment数目总和要小的Entry，可以这么写：

> Entry.objects.filter(rating__lt=F('number_of_comments') + F('number_of_pingbacks'))

##### 2、F支持跨表查询	双下划线

在F()中使用双下划线来进行跨表查询。例如，查询author的名字与blog名字相同的Entry：

> Entry.objects.filter(authors__name=F('blog__name'))




```
F，更新时用于获取原来的值
from django.db.models import F,Q
models.UserInfo.objects.all().update(age=F("age")+1)

 Q，用于构造复杂查询条件
# 应用一：
models.UserInfo.objects.filter(Q(id__gt=1))
models.UserInfo.objects.filter(Q(id=8) | Q(id=2))
models.UserInfo.objects.filter(Q(id=8) & Q(id=2))
# 应用二：
q1 = Q()
q1.connector = 'OR'
q1.children.append(('id__gt', 1))
q1.children.append(('id', 10))
q1.children.append(('id', 9))


q2 = Q()
q2.connector = 'OR'
q2.children.append(('c1', 1))
q2.children.append(('c1', 10))
q2.children.append(('c1', 9))

q3 = Q()
q3.connector = 'AND'
q3.children.append(('id', 1))
q3.children.append(('id', 2))
q2.add(q3,'OR')

con = Q()
con.add(q1, 'AND')
con.add(q2, 'AND')

models.UserInfo.objects.filter(con)
```







### 附5：web的瓶颈

1、单个请求里太多sql串行查询导致耗时长
2、单个sql太过复杂导致耗时长



### 附6：外键

pk就是primary key的缩写。通常情况下，一个模型的主键为“id”，所以下面三个语句的效果一样：

> Blog.objects.get(id__exact=14) # Explicit form
> Blog.objects.get(id=14) # __exact is implied
> Blog.objects.get(pk=14) # pk implies id__exact


[查询操作](https://www.liujiangblog.com/course/django/129)