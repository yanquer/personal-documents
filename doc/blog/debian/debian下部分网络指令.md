### 安装net-tools

- 之前用的ubuntu系统，不知道是系统不稳定，还是我操作有问题。经常无缘无故的崩溃，选择许久，换成了Debian系统。相当稳定，流畅。

- Debian系统默认不带netstat等命令，如果使用就会报错
  
  ```
  bash: netstat: command not found - Debian/Ubuntu Linux
  ```

- 解决方法：
  
  ```
  sudo apt-get install net-tools
  
  #如果需要ping的话，安装如下软件
  sudo apt-get install iputils-ping
  ```

- net-tools包含arp, ifconfig, netstat, rarp, nameif and route命令，如果使用这些命令报错，可以尝试安装。

- 参考链接：[bash: netstat: command not found - Debian/Ubuntu Linux](https://linuxconfig.org/bash-netstat-command-not-found-debian-ubuntu-linux)

