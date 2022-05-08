### mysql8.0

（因为是命令行的所以也放在这了）

创建用户

```
create user 'username'@'%' identified by 'password';

username    用户名
%    主机名，本机可用localhost，%表示所有（通配符）
```

查看用户权限

```
show grants for username@localhost;
```

为username@localhost赋予超级用户权限：

```
grant all privileges on *.* to username@localhost with grant option;

grant    授权
all privileges    所有权限
on *.*    所有数据库，所有表
to username@localhost    哪个用户的哪个主机
with grant option    是否将username自身的权限赋予其他账户
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