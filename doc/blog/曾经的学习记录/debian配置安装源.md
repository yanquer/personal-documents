## debian配置安装源



### 1、配置方法

```
#修改sources.list文件，注释原有的镜像并添加需要的镜像
vi /etc/apt/soures.list

#添加之后保存，更新源使其生效 可以先apt-get clean all清理缓存
apt-get update
```



#### 系统发行代号及对应版本

```
wheezy  -- 7.x
jessie  -- 8.x
stretch -- 9.x
buster  -- 10.x
testing -- 当前开发中的最新版本
```

#### 官方源


	# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
	deb http://ftp.cn.debian.org/debian/ buster main contrib non-free
	# deb-src http://ftp.cn.debian.org/debian/ buster main contrib non-free
	deb http://ftp.cn.debian.org/debian/ buster-updates main contrib non-free
	# deb-src http://ftp.cn.debian.org/debian/ buster-updates main contrib non-free
	deb http://ftp.cn.debian.org/debian/ buster-backports main contrib non-free
	# deb-src http://ftp.cn.debian.org/debian/ buster-backports main contrib non-free
	deb http://ftp.cn.debian.org/debian-security buster/updates main contrib non-free
	# deb-src http://ftp.cn.debian.org/debian-security buster/updates main contrib non-free

#### 国内镜像源

**清华大学：**

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free
```

**腾讯云：**

```
deb https://mirrors.cloud.tencent.com/debian/ buster main contrib non-free
deb https://mirrors.cloud.tencent.com/debian/ buster-updates main contrib non-free
deb https://mirrors.cloud.tencent.com/debian/ buster-backports main contrib non-free
deb https://mirrors.cloud.tencent.com/debian-security buster/updates main contrib non-free
#deb-src https://mirrors.cloud.tencent.com/debian/ buster main contrib non-free
#deb-src https://mirrors.cloud.tencent.com/debian/ buster-updates main contrib non-free
#deb-src https://mirrors.cloud.tencent.com/debian/ buster-backports main contrib non-free
#deb-src https://mirrors.cloud.tencent.com/debian-security buster/updates main contrib non-free
```

**阿里云：**


	deb http://mirrors.aliyun.com/debian/ stretch main non-free contrib
	#deb-src http://mirrors.aliyun.com/debian/ stretch main non-free contrib
	deb http://mirrors.aliyun.com/debian-security stretch/updates main
	#deb-src http://mirrors.aliyun.com/debian-security stretch/updates main
	deb http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib
	#deb-src http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib
	deb http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib
	#deb-src http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib


**163：**

	
	deb http://mirrors.163.com/debian/ stretch main non-free contrib
	#deb-src http://mirrors.163.com/debian/ stretch main non-free contrib
	deb http://mirrors.163.com/debian/ stretch-updates main non-free contrib
	#deb-src http://mirrors.163.com/debian/ stretch-updates main non-free contrib
	deb http://mirrors.163.com/debian/ stretch-backports main non-free contrib
	#deb-src http://mirrors.163.com/debian/ stretch-backports main non-free contrib
	deb http://mirrors.163.com/debian-security/ stretch/updates main non-free contrib
	#deb-src http://mirrors.163.com/debian-security/ stretch/updates main non-free contrib




### 2、apt系列常用命令

**install**
	install 命令用来安装或者升级包。每个包都有一个包名，而不是一个完全限定的文件名(例如，在 Debian 系统中，提供的参数是 apt-utils，而不是 apt-utils_1.6.1_amd64.deb)。被安装的包依赖的包也将被安装。配置文件 /etc/apt/sources.list 中包含了用于获取包的源(服务器)。install 命令还可以用来更新指定的包。

**upgrade**
	upgrade 命令用于从 /etc/apt/sources.list 中列出的源安装系统上当前安装的所有包的最新版本。在任何情况下，当前安装的软件包都不会被删除，尚未安装的软件包也不会被检索和安装。如果当前安装的包的新版本不能在不更改另一个包的安装状态的情况下升级，则将保留当前版本。必须提前执行 update 命令以便 apt-get 知道已安装的包是否有新版本可用。
注意 update 与 upgrade 的区别：
update 是更新软件列表，upgrade 是更新软件。

**dist-upgrade**
除执行升级功能外，dist-upgrade 还智能地处理与新版本包的依赖关系的变化。apt-get 有一个 "智能" 的冲突解决系统，如果有必要，它将尝试升级最重要的包，以牺牲不那么重要的包为代价。因此，distr -upgrade 命令可能会删除一些包。因此在更新系统中的包时，建议按顺序执行下面的命令：
$ apt-get update
$ apt-get upgrade -y
$ apt-get dis-upgrade -y

**remove**
remove 与 install 类似，不同之处是删除包而不是安装包。注意，使用 remove 命令删除一个包会将其配置文件留在系统上。

**purge**
purge 命令与 remove 命令类似，purge 命令在删除包的同时也删除了包的配置文件。

**autoremove**
autoremove 命令用于删除自动安装的软件包，这些软件包当初是为了满足其他软件包对它的依赖关系而安装的，而现在已经不再需要了。

**download**
download 命令把指定包的二进制文件下载到当前目录中。注意，是类似 *.deb 这样的包文件。

**clean**
clean 命令清除在本地库中检索到的包。它从 /var/cache/apt/archives/ 和 /var/cache/apt/archives/partial/ 目录删除除锁文件之外的所有内容。

**autoclean**
与 clean 命令类似，autoclean 命令清除检索到的包文件的本地存储库。不同之处在于，它只删除不能再下载的软件包文件，而且这些文件在很大程度上是无用的。这允许长时间维护缓存，而不至于大小失控。

**source**
source 命令下载包的源代码。默认会下载最新可用版本的源代码到当前目录中。

**changelog**
changelog 命令尝试下载并显示包的更新日志。