## Mysql





### 常用函数/关键字



#### 函数



###### 数值计算

- format

  格式化为string，format($num, $n)， 四舍五入保留小数点后 n 位，并格式化用逗号隔开（每三位一个逗号）

  ```
  select format(1000.1254);
  # 1,000.13
  ```

- round

  直接四舍五入，round($num, $n)，四舍五入保留 n 位小数

- truncate

  截取数字的小数点后几位 truncate($num, $n)，不四舍五入

  ```
  select truncate(100.1234, 2) as '1';
  # 1
  # 100.12
  # 截取小数点后两位
  ```

- convert

  转型，会四舍五入

  ```
  select convert(1478568.2457, DECIMAL(10,2));
  # 1478568.25
  ```

- ceiling

  取整，个位加一

  ```
  select CEILING(1478568.2457);   直接取整，个位+1
  # 1478569
  ```

- floor

  直接取整

  ```
  select FLOOR(1478568.2457);
  # 1478568
  ```






###### 字符串拼接

- cancat

  cancat(a, b, c) 将abc拼起来







#### 关键字

##### truncate

###### 1.truncate使用语法

truncate的作用是清空表或者说是截断表，只能作用于表。truncate的语法很简单，后面直接跟表名即可，例如： truncate table tbl_name 或者 truncate tbl_name 。

执行truncate语句需要拥有表的drop权限，从逻辑上讲，truncate table类似于delete删除所有行的语句或drop table然后再create table语句的组合。为了实现高性能，它绕过了删除数据的DML方法，因此，它不能回滚。尽管truncate table与delete相似，但它被分类为DDL语句而不是DML语句。

###### 2.truncate与drop,delete的对比

上面说过truncate与delete，drop很相似，其实这三者还是与很大的不同的，下面简单对比下三者的异同。

- truncate与drop是DDL语句，执行后无法回滚；delete是DML语句，可回滚。
- truncate只能作用于表；delete，drop可作用于表、视图等。
- truncate会清空表中的所有行，但表结构及其约束、索引等保持不变；drop会删除表的结构及其所依赖的约束、索引等。
- truncate会重置表的自增值；delete不会。
- truncate不会激活与表有关的删除触发器；delete可以。
- truncate后会使表和索引所占用的空间会恢复到初始大小；delete操作不会减少表或索引所占用的空间，drop语句将表所占用的空间全释放掉。

###### 3.truncate使用场景及注意事项

通过前面介绍，我们很容易得出truncate语句的使用场景，即该表数据完全不需要时可以用truncate。如果想删除部分数据用delete，注意带上where子句；如果想删除表，当然用drop；如果想保留表而将所有数据删除且和事务无关，用truncate即可；如果和事务有关，或者想触发trigger，还是用delete；如果是整理表内部的碎片，可以用truncate然后再重新插入数据。

无论怎样，truncate表都是高危操作，特别是在生产环境要更加小心，下面列出几点注意事项，希望大家使用时可以做下参考。

- truncate无法通过binlog回滚。
- truncate会清空所有数据且执行速度很快。
- truncate不能对有外键约束引用的表使用。
- 执行truncate需要drop权限，不建议给账号drop权限。
- 执行truncate前一定要再三检查确认，最好提前备份下表数据。
  







### 类型



###### 1、固定长度 & 可变长度

- varchar

  ​	VARCHAR类型用于存储`可变长度`字符串，是最常见的字符串数据类型。它比固定长度类型更节省空间，因为它仅使用必要的空间(根据实际字符串的长度改变存储空间)。
   有一种情况例外，如果MySQL表使用ROW_FORMAT=FIXED创建的话，每一行都会使用定长存储。

- char

  ​	CHAR类型用于存储固定长度字符串：MySQL总是根据定义的字符串长度分配足够的空间。当存储CHAR值时，MySQL会删除字符串中的末尾空格(在MySQL 4.1和更老版本中VARCHAR 也是这样实现的——也就是说这些版本中CHAR和VARCHAR在逻辑上是一样的，区别只是在存储格式上)。
   同时，CHAR值会根据需要采用空格进行剩余空间填充，以方便比较和检索。但正因为其长度固定，所以会占据多余的空间，也是一种空间换时间的策略；

###### 2、存储方式

- VARCHAR
    VARCHAR需要使用1或2个额外字节记录字符串的长度：如果列的最大长度小于或等于255字节，则只使用1个字节表示，否则使用2个字节。假设采用latinl字符集，一个VARCHAR(10)的列需要11个字节的存储空间。VARCHAR(1000)的列则需要1002 个字节，因为需要2个字节存储长度信息。

  VARCHAR节省了存储空间，所以对性能也有帮助。但是，由于行是变长的，在UPDATE时可能使行变得比原来更长，这就导致需要做额外的工作。如果一个行占用的空间增长，并且在页内没有更多的空间可以存储，在这种情况下，不同的存储引擎的处理方式是不一样的。例如，MylSAM会将行拆成不同的片段存储，InnoDB则需要分裂页来使行可以放进页内。

- CHAR
    CHAR适合存储很短或长度近似的字符串。例如，CHAR非常适合存储密码的MD5值，因为这是一个定长的值。对于经常变更的数据，CHAR也比VARCHAR更好，因为定长的CHAR类型不容易产生碎片。对于非常短的列，CHAR比VARCHAR在存储空间上也更有效率。例如用CHAR(1)来存储只有Y和N的值，如果采用单字节字符集只需要一个字节，但是VARCHAR(1)却需要两个字节，因为还有一个记录长度的额外字节。

###### 3、存储容量

- CHAR
    对于char类型来说，最多只能存放的字符个数为255，和编码无关，任何编码最大容量都是255。

- VARCHAR
    MySQL行默认最大65535字节，是所有列共享（相加）的，所以VARCHAR的最大值受此限制。

  表中只有单列字段情况下，varchar一般最多能存放(65535 - 3)个字节，varchar的最大有效长度通过最大行数据长度和使用的字符集来确定，通常的最大长度是65532个字符（当字符串中的字符都只占1个字节时，能达到65532个字符）；

为什么是65532个字符？算法如下（有余数时向下取整）：

> 最大长度(字符数) = （行存储最大字节数 - NULL标识列占用字节数 - 长度标识字节数） / 字符集单字符最大字节数

- NULL标识列占用字节数：允许NULL时，占一字节
- 长度标识字节数：记录长度的标识，长度小于等于255（28）时，占1字节；小于65535时（216）,占2字节
  VARCHAR类型在4.1和5.0版本发生了很大的变化，使得情况更加复杂。从MySQL 4.1开始，每个字符串列可以定义自己的字符集和排序规则。这些东西会很大程度上影响性能。

- 4.0版本及以下，MySQL中varchar长度是按字节展示，如varchar(20)，指的是20字节；

- 5.0版本及以上，MySQL中varchar长度是按字符展示。如varchar(20)，指的是20字符。

  

当然，行总长度还是65535字节，而字符和字节的换算，则与编码方式有关，不同的字符所占的字节是不同的。编码划分如下：

> GBK编码：
> 一个英文字符占一个字节，中文2字节，单字符最大可占用2个字节。

> UTF-8编码：
> 一个英文字符占一个字节，中文3字节，单字符最大可占用3个字节。

> utf8mb4编码：
> 一个英文字符占一个字节，中文3字节，单字符最大占4个字节（如emoji表情4字节）。

假设当前还有6字节可以存放字符，按单字符占用最大字节数来算，可以存放3个GBK、或2个utf8、或1个utf8mb4。



###### 思考：既然VARCHAR长度可变，那我要不要定到最大?

  没错，相信你已经有答案了，别这么干！

  就像使用VARCHAR(5)和VARCHAR(200)存储 '陈哈哈’的磁盘空间开销是一样的。那么使用更短的列有什么优势呢？

  事实证明有很大的优势。更长的列会消耗更多的内存，因为MySQL通常会分配固定大小的内存块来保存内部值。

  当然，在没拿到存储引擎存储的数据之前，并不会知道我这一行拿出来的数据到底有多长，可能长度只有1，可能长度是500，那怎么办呢？那就只能先把最大空间分配好了，避免放不下的问题发生，这样实际上对于真实数据较短的varchar确实会造成空间的浪费。
  举例：我向数据类型为：varchar（1000）的列插入了1024行数据，但是每个只存一个字符，那么这1024行真实数据量其实只有1K，但是我却需要约1M的内存去适应他。所以最好的策略是只分配真正需要的空间。



###### 类似

 与CHAR和VARCHAR类似的类型还有BINARY和VARBINARY,它们存储的是二进制字符串。二进制字符串跟常规字符串非常相似，但是二进制字符串存储的是字节码而不是字符。 填充也不一样：MySQL填充BINARY采用的是\0 (零字节)而不是空格，在检索时也不会去掉填充值。

  当需要存储二进制数据，并且希望MySQL使用字节码而不是字符进行比较时，这些类型是非常有用的。二进制比较的优势并不仅仅体现在大小写敏感上。MySQL比较BINARY字符串时，每次按一个字节，并且根据该字节的数值进行比较。因此，二进制比 较比字符比较简单很多，所以也就更快。











### binlog



binlog是Mysql sever层维护的一种二进制日志，与innodb引擎中的redo/undo log是完全不同的日志；其主要是用来记录对mysql数据更新或潜在发生更新的SQL语句，并以"事务"的形式保存在磁盘中；

作用主要有：

- 复制：MySQL Replication在Master端开启binlog，Master把它的二进制日志传递给slaves并回放来达到master-slave数据一致的目的
- 数据恢复：通过mysqlbinlog工具恢复数据
- 增量备份

Binlog 包括两类文件：

- 二进制日志索引文件(.index)：记录所有的二进制文件。
- 二进制日志文件(.00000*)：记录所有 DDL 和 DML 语句事件。



**redo log** 保证一致性（将修改后的数据记录，当前语句）

**undo log** 保证原子性（将修改前的数据记录，与当前语句相反的语句）





#### 关于binlog的清除/不记录



##### 不记录 

在 配置文件的 mysqld 下写入 skip-log-bin  



##### 清除

- **手动清理**

  查看主从库使用的是哪个binlog文件

  ```
  show master status;
  show slave status;
  ```

  删除之前可以先做个备份

  清除指定日期的备份

  ```
  purge master logs before '2016-09-01 17:20:00'; //删除指定日期以前的日志索引中binlog日志文件
  ```

  或者

  ```
  purge master logs to'mysql-bin.000022'; //删除指定日志文件的日志索引中binlog日志文件
  ```

  注意：使用该语法，会将对应的文件和mysql-bin.index中对应路径删除

  时间和文件名一定不可以写错，尤其是时间中的年和文件名中的序号，以防不下心将正在使用的binlog删除！！！切勿删除正在使用的binlog

  - reset master:将删除日志索引文件中记录的所有binlog文件，创建一个新的日志文件，起始值从000001开始。不要轻易使用该命令，这个命令通常仅仅用于第一次用于搭建主从关系的时的主库。
  - reset slave:清除master.info文件、relay-log.info文件，以及所有的relay log文件,并重新启用一个新的relaylog文件

- **自动清理**

  设置binlog过期时间，使系统自动删除binlog文件

  **在mysql中修改**

  查看binlog过期时间，这个值默认是0天，也就是说不自动清理，可以根据生产情况修改，本例修改为7天

  ```
  mysql> show variables like 'expire_logs_days'; 
  
  +------------------------+-------+ 
  
  | Variable_name  | Value | 
  
  +------------------------+-------+ 
  
  | expire_logs_days |   0  | 
  
  +------------------------+-------+ 
  
  mysql> set global expire_logs_days = 7;    #设置binlog多少天过期
  
  ```

  设置之后不会立即清除，触发条件是以下之一：

  1.binlog大小超过max_binlog_size，max_binlog_size默认为1G

  2.手动执行flush logs

   

  如果binlog非常多，不要轻易设置该参数，有可能导致IO争用，这个时候可以使用purge命令予以清除：

  将bin.000055之前的binlog清掉:

  ```
  mysql>purge binary logs to 'bin.000055';
  ```

  将指定时间之前的binlog清掉:

  ```
  mysql>purge binary logs before '2017-05-01 13:09:51';
  ```

- **配置文件中修改**

  mysqld在每个二进制日志名后面添加一个数字扩展名。每次你启动服务器或刷新日志时该数字则增加。如果当前日志大小达到max_binlog_size,还会自动创建新的二进制日志。如果你正则使用大的事务，二进制日志还会超过max_binlog_size:事务全写入一个二进制日志中，绝对不要写入不同的二进制日志中。

   

  expire_logs_days :定义了mysql清除过期日志的时间。默认值为0,表示“没有自动删除”。

  max_binlog_size：二进制日志最大大小，如果二进制日志写入的内容超出给定值，日志就会发生滚动。你不能将该变量设置为大于1GB或小于4096字节。 默认值是1GB。

   

  在my.cnf中添加配置,设置过期时间为30天

  ```
  expire_logs_days = 30
  ```

  max_binlog_size使用默认值即可

   

  注意：

  过期时间设置的要适当，对于主从复制，要看从库的延迟决定过期时间，避免主库binlog还未传到从库便因过期而删除，导致主从不一致！！！







### DDL与DML

DML(Data Manipulation Language)数据操纵语言：

适用范围：对数据库中的数据进行一些简单操作，如insert,delete,update,select等.

 

DDL(Data Definition Language)数据定义语言：

适用范围：对数据库中的某些对象(例如，database,table)进行管理，如Create,Alter和Drop.


一、DDL(数据定义语言,Data Definition Language)

建库、建表、设置约束等：create\drop\alter
1、创建数据库:
create database IF NOT EXISTS hncu CHARACTER SET utf8;

2、创建表格:
use hncu;
create table IF NOT EXISTS stud(
id int,
name varchar(30),
age int
);

3、更改表结构(设置约束)
desc stud; //查看表结构
alter table stud drop column age;
alter table stud add column age int;

4、删除表、删除数据库
drop table stud;
drop database hncu;


二、DML (数据操纵语言，Data Manipulation Language )
主要指数据的增删查改: Select\delete\update\insert\call

select * from stud;
select name,age from stud; //查询指定的列
select name as 姓名, age as 年龄 from stud;





### MyDumper

​	相对于 [MySQL](https://cloud.tencent.com/product/cdb?from=10680) 官方提供的逻辑备份工具 mysqldump，mydumper 最突出的特性就是可采用多线程并行备份，极大提高了数据导出的速度。



使用

```
mydumper -h $host -u $user -p $password --database $db --tables-lists $tables --compress --threads 4 --outputdir $path

# 少一个  --tables-lists $tables 就是全库备份
mydumper -h $host --database $db --compress --threads 4 --outputdir $path --defaults-file=$passfile 
```



- -c --compress		压缩输出文件
- -m --no-schemas	不导出表结构
- -t --threads		使用的线程数量
- -F --chunk-filesize	将表数据分割成这个输出大小的块，单位默认是MB





### mysql索引



#### 基本





- **单列索引**：一个索引只包含单个列

- **组合索引**：组合索引指在表的多个字段组合上创建的索引，只有在查询条件中使用了这些字段的左边字段时，索引才会被使用。使用组合索引时**遵循最左前缀集合**

- **Primary Key（聚集索引）**：InnoDB存储引擎的表会存在主键（唯一非null），如果建表的时候没有指定主键，则会使用第一非空的唯一索引作为聚集索引，否则InnoDB会自动帮你创建一个不可见的、长度为6字节的row_id用来作为聚集索引。

- **Unique（唯一索引）**：索引列的值必须唯一，但允许有空值。若是组合索引，则列值的组合必须唯一。主键索引是一种特殊的唯一索引，不允许有空值

- **Key（普通索引）**：是MySQL中的基本索引类型，允许在定义索引的列中插入重复值和空值

- **FULLTEXT（全文索引）**：全文索引类型为FULLTEXT，在定义索引的列上支持值的全文查找，允许在这些索引列中插入重复值和空值。全文索引可以在CHAR、VARCHAR或者TEXT类型的列上创建

  注意搜索长度有默认值，参考：https://blog.csdn.net/mrzhouxiaofei/article/details/79940958

- **SPATIAL（空间索引）**：空间索引是对空间数据类型的字段建立的索引，MySQL中的空间数据类型有4种，分别是GEOMETRY、POINT、LINESTRING和POLYGON。MySQL使用SPATIAL关键字进行扩展，使得能够用于创建正规索引类似的语法创建空间索引。创建空间索引的列必须声明为NOT NULL



这里在说一下组合索引的遵循最左前缀原则：

```
order by使用索引最左前缀
- order by a
- order by a,b
- order by a,b,c
- order by a desc, b desc, c desc 

如果where使用索引的最左前缀定义为常量，则order by能使用索引
- where a=const order by b,c
- where a=const and b=const order by c
- where a=const and b > const order by b,c

不能使用索引进行排序
- order by a , b desc ,c desc  --排序不一致
- where d=const order by b,c   --a丢失
- where a=const order by c     --b丢失
- where a=const order by b,d   --d不是索引的一部分
- where a in(...) order by b,c --a属于范围查询
```



创建一个简单的表：



```
CREATE TABLE my_test (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `sex` varchar(5) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `birthday` datetime NOT NULL,
  `user_num` int(11) unique,
  PRIMARY KEY (`id`),
  index(username)
);
```



show index from my_test;



 明明在建表的时候只创建了一个索引，查询出来的有三个，其实**主键，唯一约束列，外键**这些都自动会生成索引，至于外键大家可以去尝试下。



上表格中各个列的说明：

```
table #表名称
non_unique  #如果索引不能包括重复词，为0，如果可以，则为1
key_name  #索引的名称
seq_in_index #索引中的列序号
column_name  #列名称
collation  #列以什么方式存储在索引中，在mysql中，有值'A'（升序）或者NULL（无分类）
cardinality  #索引在唯一值的数据的估值，通过运行analyze table xxx_table;或者 myisamchk -a 可以更新，技术根据被存储为整数的统计数据来计数，所以即使对于小型表，该值也没必要是精确的，基数越大，当进行联合所饮食，mysql使用该索引的机会越大。myisam中，该值是准确的，INNODB中该值数据是估算的，存在偏差
sub_part  #如果列只是部分的编入索引 则为被编入索引的字符的数目，如果整列被编入索引，则为NULL
packed  #指示关键词如何被压缩，如果没有被压缩，则为NULL
NULL   #如果列含有NULL，则含有YES，如果没有，则该列为NO
index_type  #用过的索引方法（BTREE,FULLTEXT,HASH,RTREE）
comment  #备注
index_comment  #为索引创建时提供了一个注释属性的索引的任何评论
```





##### 索引创建原则

1. 索引并非越多越好，一个表中如果有大量的索引，不仅占用磁盘空间，而且会影响INSERT、DELETE、UPDATE等语句的性能，因为在表中的数据更改的同时，索引也会进行调整和更新
2. 避免对经常更新的表进行过多的索引，并且索引中的列尽可能少。而对经常用于查询的字段应该创建索引，但要避免添加不必要的字段。
3. 数据量小的表最好不要使用索引，由于数据较少，查询花费的时间可能比遍历索引的时间还要短，索引可能不会产生优化效果。
4. 在条件表达式中经常用到的不同值较多的列上建立索引，在不同值很少的列上不要建立索引。比如在学生表的“性别”字段上只有“男”与“女”两个不同值，因此就无须建立索引。如果建立索引，不但不会提高查询效率，反而会严重降低数据更新速度。
5. 当唯一性是某种数据本身的特征时，指定唯一索引。使用唯一索引需能确保定义的列的数据完整性，以提高查询速度。
6. 在频繁进行排序或分组（即进行group by或order by操作）的列上建立索引，如果待排序的列有多个，可以在这些列上建立组合索引。
7. 搜索的索引列，不一定是所要选择的列。换句话说，最适合索引的列是出现在WHERE子句中的列，或连接子句中指定的列，而不是出现在SELECT关键字后的选择列表中的列。
8. 使用短索引。如果对字符串列进行索引，应该指定一个前缀长度，只要有可能就应该这样做。例如，有一个CHAR(200)列，如果在前10个或20个字符内，多数值是唯一的，那么就不要对整个列进行索引。对前10个或20个字符进行索引能够节省大量索引空间，也可能会使查询更快。较小的索引涉及的磁盘 IO 较少，较短的值比较起来更快。更为重要的是，对于较短的键值，索引高速缓存中的块能容纳更多的键值，因此，MySQL 也可以在内存中容纳更多的值。这样就增加了找到行而不用读取索引中较多块的可能性。
9. 利用最左前缀。在创建一个n列的索引时，实际是创建了MySQL可利用的n个索引。多列索引可起几个索引的作用，因为可利用索引中最左边的列集来匹配行。这样的列集称为最左前缀。
10. 对于InnoDB存储引擎的表，记录默认会按照一定的顺序保存，如果有明确定义的主键，则按照主键顺序保存。如果没有主键，但是有唯一索引，那么就是按照唯一索引的顺序保存。如果既没有主键又没有唯一索引，那么表中会自动生成一个内部列，按照这个列的顺序保存。按照主键或者内部列进行的访问是最快的，所以InnoDB表尽量自己指定主键，当表中同时有几个列都是唯一的，都可以作为主键的时候，要选择最常作为访问条件的列作为主键，提高查询的效率。另外，还需要注意，InnoDB 表的普通索引都会保存主键的键值，所以主键要尽可能选择较短的数据类型，可以有效地减少索引的磁盘占用，提高索引的缓存效果













##### 普通索引

###### 创建索引

这是最基本的索引，它没有任何限制。它有以下几种创建方式：

```
CREATE INDEX indexName ON table_name (column_name)
```

如果是CHAR，VARCHAR类型，length可以小于字段实际长度；如果是BLOB和TEXT类型，必须指定 length。

###### 修改表结构(添加索引)

```
ALTER table tableName ADD INDEX indexName(columnName)
```

###### 创建表的时候直接指定

```
CREATE TABLE mytable(  
 
ID INT NOT NULL,   
 
username VARCHAR(16) NOT NULL,  
 
INDEX [indexName] (username(length))  
 
);  
```

###### 删除索引的语法

```
DROP INDEX [indexName] ON mytable; 
```





##### 唯一索引

它与前面的普通索引类似，不同的就是：索引列的值必须唯一，但允许有空值。如果是组合索引，则列值的组合必须唯一。它有以下几种创建方式：

###### 创建索引

```
CREATE UNIQUE INDEX indexName ON mytable(username(length)) 
```

###### 修改表结构

```
ALTER table mytable ADD UNIQUE [indexName] (username(length))
```

###### 创建表的时候直接指定

```
CREATE TABLE mytable(  
 
ID INT NOT NULL,   
 
username VARCHAR(16) NOT NULL,  
 
UNIQUE [indexName] (username(length))  
 
);  
```





##### 使用ALTER 命令添加和删除索引

有四种方式来添加数据表的索引：

- **ALTER TABLE tbl_name ADD PRIMARY KEY (column_list)**:

  该语句添加一个主键，这意味着索引值必须是唯一的，且不能为NULL。

- **ALTER TABLE tbl_name ADD UNIQUE index_name (column_list):** 这条语句创建索引的值必须是唯一的（除了NULL外，NULL可能会出现多次）。

  注：UNIQUE，唯一

- **ALTER TABLE tbl_name ADD INDEX index_name (column_list):** 添加普通索引，索引值可出现多次。

- **ALTER TABLE tbl_name ADD FULLTEXT index_name (column_list):**该语句指定了索引为 FULLTEXT ，用于全文索引。

以下实例为在表中添加索引。

```
mysql> ALTER TABLE testalter_tbl ADD INDEX (c);
```

你还可以在 ALTER 命令中使用 DROP 子句来删除索引。尝试以下实例删除索引:

```
mysql> ALTER TABLE testalter_tbl DROP INDEX c;
```

------

##### 使用 ALTER 命令添加和删除主键

主键作用于列上（可以一个列或多个列联合主键），添加主键索引时，你需要确保该主键默认不为空（NOT NULL）。实例如下：

```
mysql> ALTER TABLE testalter_tbl MODIFY i INT NOT NULL;
mysql> ALTER TABLE testalter_tbl ADD PRIMARY KEY (i);
```

你也可以使用 ALTER 命令删除主键：

```
mysql> ALTER TABLE testalter_tbl DROP PRIMARY KEY;
```

删除主键时只需指定PRIMARY KEY，但在删除索引时，你必须知道索引名。

------

##### 显示索引信息

你可以使用 SHOW INDEX 命令来列出表中的相关的索引信息。可以通过添加 \G 来格式化输出信息。

尝试以下实例:

```
mysql> SHOW INDEX FROM table_name\G
```







#### 关于聚簇索引与非聚簇索引



MySQL的InnoDB索引数据结构是B+树，主键索引叶子节点的值存储的就是MySQL的数据行，普通索引的叶子节点的值存储的是主键值，这是了解聚簇索引和非聚簇索引的前提





##### 聚簇索引

很简单记住一句话：找到了索引就找到了需要的数据，那么这个索引就是聚簇索引，所以主键就是聚簇索引，修改聚簇索引其实就是修改主键。

**记住，主键索引就是聚簇索引**





##### 非聚簇索引

索引的存储和数据的存储是分离的，也就是说找到了索引但没找到数据，需要根据索引上的值(主键)再次回表查询,非聚簇索引也叫做辅助索引。



下面我们创建了一个学生表，做三种查询，来说明什么情况下是聚簇索引，什么情况下不是。

```
create table student (
    id bigint,
    no varchar(20) ,
    name varchar(20) ,
    address varchar(20) ,
    PRIMARY KEY (`branch_id`) USING BTREE,
    UNIQUE KEY `idx_no` (`no`) USING BTREE
)ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
```

第一种，直接根据主键查询获去所有字段数据，此时主键时聚簇索引，因为主键对应的索引叶子节点存储了id=1的所有字段的值。

```
select * from student where id = 1
```

第二种，根据编号查询编号和名称，编号本身是一个唯一索引，但查询的列包含了学生编号和学生名称，当命中编号索引时，该索引的节点的数据存储的是主键ID，需要根据主键ID重新查询一次，所以这种查询下no不是聚簇索引

```
select no,name from student where no = 'test'
```

第三种，我们根据编号查询编号（有人会问知道编号了还要查询？要，你可能需要验证该编号在数据库中是否存在），这种查询命中编号索引时，直接返回编号，因为所需要的数据就是该索引，不需要回表查询，这种场景下no是聚簇索引

```
select no from student where no = 'test'
```



##### 总结

主键一定是聚簇索引，MySQL的InnoDB中一定有主键，即便研发人员不手动设置，则会使用unique索引，没有unique索引，则会使用数据库内部的一个行的id来当作主键索引,其它普通索引需要区分SQL场景，当SQL查询的列就是索引本身时，我们称这种场景下该普通索引也可以叫做聚簇索引，MyisAM引擎没有聚簇索引。





#### 查询



##### explain 优化

（查询优化神器）

EXPLAIN语句的基本语法如下：

```
explain select select_option
```

select_options是SELECT语句的查询选项，包括FROM WHERE子句等

```
id: SELECT识别符。这是SELECT的查询序列号,表示查询中执行select子句或操作表的顺序,id相同，执行顺序从上到下,id不同，id值越大执行优先级越高
select_type：表示SELECT语句的类型。它可以是以下几种取值：
    SIMPLE:表示简单查询，其中不包括连接查询和子查询；
    PRIMARY:表示主查询，或者是最外层的查询语句，最外层查询为PRIMARY，也就是最后加载的就是PRIMARY；
    UNION:表示连接查询的第2个或后面的查询语句， 不依赖于外部查询的结果集
    DEPENDENT UNION:连接查询中的第2个或后面的SELECT语句，依赖于外面的查询；
    UNION RESULT:连接查询的结果；
    SUBQUERY:子查询中的第1个SELECT语句；不依赖于外部查询的结果集
    DEPENDENT SUBQUERY:子查询中的第1个SELECT，依赖于外面的查询；
    DERIVED:导出表的SELECT（FROM子句的子查询）,MySQL会递归执行这些子查询，把结果放在临时表里。
    DEPENDENT DERIVED:派生表依赖于另一个表
    MATERIALIZED:物化子查询
    UNCACHEABLE SUBQUERY:子查询，其结果无法缓存，必须针对外部查询的每一行重新进行评估
    UNCACHEABLE UNION:UNION中的第二个或随后的 select 查询，属于不可缓存的子查询
table:表示查询的表
partitions:查询将从中匹配记录的分区。该值适用NULL于未分区的表
type:表示表的连接类型
    system:该表是仅有一行的系统表。这是const连接类型的一个特例
    const: 数据表最多只有一个匹配行，它将在查询开始时被读取，并在余下的查询优化中作为常量对待。const表查询速度很快，因为只读取一次,const用于使用常数值比较PRIMARY KEY或UNIQUE索引的所有部分的场合。
    eq_ref:对于每个来自前面的表的行组合，从该表中读取一行,可以用于使用=运算符进行比较的索引列 。比较值可以是常量，也可以是使用在此表之前读取的表中列的表达式
    ref:对于来自前面的表的任意行组合，将从该表中读取所有匹配的行，ref可以用于使用“＝”或“＜＝＞”操作符的带索引的列。
    fulltext:使用FULLTEXT 索引执行联接
    ref_or_null:这种连接类型类似于ref，但是除了MySQL还会额外搜索包含NULL值的行。此联接类型优化最常用于解析子查询
    index_merge:此联接类型指示使用索引合并优化。在这种情况下，key输出行中的列包含使用的索引列表，并key_len包含使用的索引 的最长键部分的列表
    unique_subquery:类型替换 以下形式的eq_ref某些 IN子查询,unique_subquery 只是一个索引查找函数，它完全替代了子查询以提高效率。
    index_subquery:连接类型类似于 unique_subquery。它代替IN子查询,但只适合子查询中的非唯一索引
    range:只检索给定范围的行，使用一个索引来选择行。key列显示使用了哪个索引。key_len包含所使用索引的最长关键元素。当使用＝、＜＞、＞、＞＝、＜、＜＝、IS NULL、＜＝＞、BETWEEN或者IN操作符用常量比较关键字列时，类型为range
    index:该index联接类型是一样的 ALL，只是索引树被扫描。这发生两种方式：1、如果索引是查询的覆盖索引，并且可用于满足表中所需的所有数据，则仅扫描索引树。在这种情况下，Extra列显示为 Using index，2、使用对索引的读取执行全表扫描，以按索引顺序查找数据行。 Uses index没有出现在 Extra列中。
    ALL:对于前面的表的任意行组合进行完整的表扫描    
possible_keys:指出MySQL能使用哪个索引在该表中找到行。若该列是NULL，则没有相关的索引。在这种情况下，可以通过检查WHERE子句看它是否引用某些列或适合索引的列来提高查询性能。如果是这样，可以创建适合的索引来提高查询的性能。
kye:表示查询实际使用的索引，如果没有选择索引，该列的值是NULL。要想强制MySQL使用或忽视possible_keys列中的索引，在查询中使用FORCE INDEX、USE INDEX或者IGNORE INDEX
key_len：表示MySQL选择的索引字段按字节计算的长度，若键是NULL，则长度为NULL。注意，通过key_len值可以确定MySQL将实际使用一个多列索引中的几个字段
ref：表示使用哪个列或常数与索引一起来查询记录。
rows：显示MySQL在表中进行查询时必须检查的行数。
Extra：表示MySQL在处理查询时的详细信息
```





参考：

[MySQL索引原理及慢查询优化](https://tech.meituan.com/2014/06/30/mysql-index.html)





##### 关键选项

- union	去重查询
- union all	不去重查询
- distinct	字段去重







### other



###### 建表语句

```
cerate database if not exists db_test default charset utf8mb4;
use db_test;
drop table if exists tbl_test;
create table if not exists tbl_test(
	id int primary key auto_increment,
    tt varchar(19) default null comment 'tt'
)engine=InnoDB default charset=utf8mb4 comment 'test';

```





###### 注释

- 单行

  ```
  # select
  -- select
  ```

  

- 多行

  ```
  /*
  select
  */
  ```

  



###### 查询所占空间

1.直接查询

```
select
table_schema as '数据库',
sum(table_rows) as '记录数',
sum(truncate(data_length/1024/1024, 2)) as '数据容量(MB)',
sum(truncate(index_length/1024/1024, 2)) as '索引容量(MB)'
from information_schema.tables
where table_schema='mysql';
```

2.使用optimize命令

```
optimize table tb_report_inventory;
```

使用的时间比较长，需要耐心等待。

注意：optimize执行时会将表锁住，所以不要在高峰期使用。也不要经常使用，每月一次就足够了







###### 执行



如果是sql语句文件

```
mysql -u $user -p $pass < $file.sql
```

如果不是

```
echo "$sql" | mysql -u $user -p$pass
```



如果把账号密码放到一个文件

```
# pwd.cnf
[client]
user=root
password=root
```

如果是sql语句文件

```
mysql --defaults-extra-file=pwd.cnf < $file.sql
```

如果不是

```
echo "$sql" | mysql --defaults-extra-file=pwd.cnf
```





###### 外键约束

外键约束（表2）对父表（表1）的含义:

在父表上进行update/delete以更新或删除在子表中有一条或多条对应匹配行的候选键时，父表的行为取决于：在定义子表的外键时指定的on update/on delete子句。

关键字

含义

- CASCADE

  删除包含与已删除键值有参照关系的所有记录

- SET NULL

  修改包含与已删除键值有参照关系的所有记录，使用NULL值替换(只能用于已标记为NOT NULL的字段)

- RESTRICT

  拒绝删除要求，直到使用删除键值的辅助表被手工删除，并且没有参照时(这是默认设置，也是最安全的设置)

- NO ACTION

  啥也不做





###### mysql8.0



创建用户

```
create user 'username'@'%' identified by 'password';

username	用户名
%	主机名，本机可用localhost，%表示所有（通配符）
```

查看用户权限

```
show grants for username@localhost;
```

为username@localhost赋予超级用户权限：

```
grant all privileges on *.* to username@localhost with grant option;

grant	授权
all privileges	所有权限
on *.*	所有数据库，所有表
to username@localhost	哪个用户的哪个主机
with grant option	是否将username自身的权限赋予其他账户
```

普通用户权限添加

```
grant usage,select,insert,update,delete,create temporary tables,execute on jikedb.* to
username@localhost; //此时没有with grant option 表示不给其他用户赋权限
flush privileges;

usage:无权限，当你想创建一个没有权限的用户时候，指定usage
show:的权限
view:视图的权限(mysql8.0+赋权限出错)ERROR 3619 (HY000): Illegal privilege level specified for VIEW
create temporary tables:创建临时表的权限
excute：执行的权限
```

收回权限

```
revoke delete on jikedb.* from username@localhost; 
//意思是收回username@localhost下jikedb库所有的表的删除操作
```

新创建的用户username@localhost 要想使用，登录后需要修改密码

```
alter user username@localhost identified by '12345678'
```

删除用户

```
 drop user username@localhost; //username，localhost加不加引号都可
```

有时候需要重载一下表数据

```
grant reload on *.* to username@'%';
```







###### 关于字符集



直接修改数据表的字符集不一定行

得删除表重新建表的时候弄字符集



直接修改字符集（不一定有用）

```
select 
	concat(
    	'alter table ',
        TABLE_NAME,
        ' convert to character set utf8mb4 collate utf8mb4_general_ci;'
    )
from
	information_schema.'TABLES'
where
	TABLE_SCHEMA = '$database';
```

这个结果为更改语句，直接复制执行即可

