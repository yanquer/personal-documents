## Python模块及pip的安装

1、安装pip

```
apt install python-pip				#py2使用

apt install python3-pip				#py3使用
```



2、配置pip源（需要自定义才配置，默认国外的太慢）

在用户目录下创建 ~/.pip/pip.conf 配置文件，内容


    [global]
    index-url = http://pypi.douban.com/simple 	#豆瓣源;可以换成其他的源
    disable-pip-version-check = true     		#取消pip版本检查&#xff0c;排除每次都报最新的pip
    timeout = 120
    [install]
    trusted-host = pypi.douban.com      		#添加豆瓣源为可信主机&#xff0c;要不然可能报错


或者执行的时候直接指定


    pip instal soft -i "http://pypi.douban.com/simple" --trusted-host pypi.douban.com




