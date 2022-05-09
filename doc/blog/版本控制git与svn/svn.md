## svn

###### 安装

```
apt install subversion
```

###### 配置，

其实不需要怎么配置，

遇到的问题是普通用户每次都需要输入密码

修改

```
# ~/.subversion/config

# 允许明码记住密码
password-stores = simple
```

```
# 也可以在这里设置选项
# ~/.subversion/servers
store-plaintest-passwords
```

```
# 解压到指定路径 这个时候是 $svn_path 下的所有文件 在 $local_path下面
svn checkout $svn_path $local_path

# 先进去再解压 这个时候是svn地址 当前文件开始命名
cd $local_path && svn checkout $svn_path

# 更新
cd $local_path
svn update
```

###### 关于错误：svn "cannot set LC_CTYPE locale"的问题

解决

```
# 修改/etc/profile
# 加入
export LC_ALL=C
# 然后在终端执行：
source /etc/profile
```

毛用没有，

这样弄才解决的

```
sudo dpkg-reconfigure locales
```

重新安装了一下语言为en_US.UTF-8

看了一下 /etc/default/locale的内容，变成了

```
LC_CTYPE="en_US.UTF-8"
LC_ALL="en_US.UTF-8"
LANG="en_US.UTF-8"
```

（之前设置的环境为中文，所以可能脚本不兼容我这个系统）

后面有时间看看这几个变量的区别

参考链接： https://askubuntu.com/questions/599808/cannot-set-lc-ctype-to-default-locale-no-such-file-or-directory

###### 关于冲突的问题

使用 svn cleanup 无效

然后删除了重新checkout的

###### svn blame

查看具体的每一行代码的变更信息

