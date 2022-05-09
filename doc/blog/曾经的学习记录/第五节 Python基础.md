## 第五节 Python基础



**关于字典：**

```
#当字典的元素个数少于1000时，应使用dData.keys(),dData.items(),dDate.values()
#当字典的元素个数超过1000时，为了提高效率，可以使用dData.iterkeys(),dData.iteritems,dData.itervalues()
#当没有把握时，采用第一种keys的方案

#keys，items，values会创建新的副本参与元素遍历，安全性更高，而iter是迭代器的概念，直接用元素的内存地址指针参与每个元素的遍历
```



**多个变量的赋值：**

```
a = b = c = 1
#创建一个整型对象，值为1，三个变量被分配到相同的内存空间上
a, b, c = 1, 2, "john"
#a,b,c分别被赋值为1,2，"john"
```



**Python 五个标准的数据类型**

```
Numbers				#数字
String				#字符串
List				#列表
Tuple				#元组
Dictionary			#字典
```



**Python支持四种不同的数字类型**

```
int					#有符号整型
long				#长整型，也可以代表八进制或者十六进制
float				#浮点型
complex				#复数
```

python2.2之后int溢出后会自动自动转换为long，3中long被移除

在python中类型属于对象，变量是没有类型的  



**argparse的使用**

```
#例子
import argparse

def main():
    parser = argparse.ArgumentParser(description="Demo of argparse")
    parser.add_argument('-n','--name', default=' Li ')
    parser.add_argument('-y','--year', default='20')
    args = parser.parse_args()
    print(args)
    name = args.name
    year = args.year
    print('Hello {}  {}'.format(name,year))

if __name__ == '__main__':
    main()
```







基本使用模板

```
#导入argparse
import argparse

parser = argparse.ArgumentParser(description="Demo of argparse")	#生成argparse对象
parser.add_argument('-n','--name', default=' Li ')					#增加参数
args = parser.parse_args()											#获取


#add_argument参数列表
default				#add_argument
required			#这个参数是否一定需要设置
type				#参数类型
choices				#参数值只能从几个选项里面选择
help				#指定参数的说明信息
dest				#设置参数在代码中的变量名
nargs				#设置参数在使用可以提供的个数
        #值  含义
        N   #参数的绝对个数（例如：3）
        '?'   #0或1个参数
        '*'   #0或所有参数
        '+'   #所有，并且至少一个参数
        
parser.add_argument('-n', defalut=1, required=True, type=int, choices=[1,2,3], help='is number', dest=iNum, nargs='?')

```





**time模块函数**

```
strptime
#p表示parse，表示分析的意思，所以strptime是给定一个时间字符串和分析模式，返回一个时间对象。

strftime
#f表示format，表示格式化，和strptime正好相反，要求给一个时间对象和输出格式，返回一个时间字符串


#获取当前时间戳
timestamp = int(time.time())
#格式化时间戳为本地的时间元组
timeArray = time.localtime(timestamp)
#格式化时间为目标格式字符串
timeStr = time.strftime('%Y-%m-%d %H:%N:%S', timeArray)
#根据指定的格式把一个时间字符串解析为时间元组
timeArray2 = time.strptime(timeStr, '%Y-%m-%d %H:%N:%S')
#转换为时间戳
timestamp2 = int(time.mktime(timeArray2))
```





**字符串的操作**

```
#截取字符串
str = 'hello'
print str[1:4]				#ell
#str[start:end],从下标start开始，end结束，不包括end

#将字符串转换为数组
str = 'hi yo'
print str.split()			#['hi', 'yo']
#split，以指定字符串分隔, 不带参默认是空格
```

