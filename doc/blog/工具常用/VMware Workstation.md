### VMware Workstation

当我们安装VMware Workstation后，在[宿主机](https://cloud.tencent.com/product/cdh?from=10680)（物理电脑）上会多出两个网卡，VMNet1、VMNet8，在虚拟机设置里会多出一个配置 VMNet0。

![img](https://ask.qcloudimg.com/http-save/yehe-6175518/7coh1ddgpz.png?imageView2/2/w/1620)

![img](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/image-20211207115747817.png)

　　vmnet1和vmnet8是两个虚拟网卡，主要作用是让虚拟机可以通过你的宿主机的网线上网。注意：如果有“！”，说明不能用。 　vmnet1是为host-only方式服务的，vmnet8是为NAT方式服务的。

　　一个是设置私有网络（Host Only）时，用来和主机通信的，禁用以后就无法正常使用Host-Only模式了，另一个是设置网络地址翻译（NAT）时，和主机通讯使用的，如果禁用，那么虚拟机在NAT模式下依然可以通过主机网卡访问外网，但不能通过内部网络和主机直接通信。而使用桥接网络时，则不需要这两个网卡了。 　　通过NAT方式上网的guest系统与主机通信需要VMnet8网卡的支持，使用Host-Only模式的guest系统与主机通信需要VMnet1网卡的支持，使用桥接模式上网需要网络中存在DHCP服务器，且提供服务。 VMnet8提供NAT和DHCP服务，VMnet1提供DHCP服务。

- VMNet1 

　　　　使用的是host-only的链接模式，即虚拟机只能与主机构成内部通信，无法对外网进行访问。

- VMNet8 

　　　　模式：

　　　　　　NAT网络模式

　　　　场景：

 　　　  　　在宿主机安装多台虚拟机，和宿主组成一个小局域网，宿主机，虚拟机之间都可以互相通信，虚拟机也可访问外网，例如 搭建 hadoop 集群，分布式服务

​                        使用Vmnet8虚拟交换机，此时虚拟机可以通过主机单向网络上的其他工作站，其他工作站不能访问虚拟机。

- VMNet0 

　　　　模式：

　　　　　　使用桥接模式，安装VM后，在VM里建立虚拟机 默认 就是该模式。

　　　　场景：

　　　　　　如果你只是需要一台虚拟机可以和宿主互通，并可以访问外网，此模式即可。

　　　　描述：

　　　　　　安装虚拟机系统后不需要调整网络，物理网络中的 “路由” 所包含的DHCP服务器会自动识别该虚拟机并为其分配IP地址；

　　　　　　如果没有路由，可以自己手动在系统分配，原则是和宿主机在同一网段并指向相同的网关即可通信。

#### [Vmware虚拟机三种网络模式详解](https://www.cnblogs.com/linjiaxin/p/6476480.html)

**虚拟机支持3种常用网络模式：**

**1、Bridge模式：虚拟机作为独立的计算，和宿主机同样连接到外部网络。如果局域网中是DHCP，将虚拟机设置为静态ip，存在ip冲突的风险。**

​    桥接模式就是将主机网卡与虚拟机虚拟的网卡利用虚拟网桥进行通信。在桥接的作用下，类似于把物理主机虚拟为一个交换机，所有桥接设置的虚拟机连接到这个交换机的一个接口上，物理主机也同样插在这个交换机当中，所以所有桥接下的网卡与网卡都是交换模式的，相互可以访问而不干扰。在桥接模式下，虚拟机ip地址需要与主机在同一个网段，如果需要联网，则网关与DNS需要与主机网卡一致。

![https://note.youdao.com/yws/public/resource/236896997b6ffbaa8e0d92eacd13abbf/8151318698234E84A9952FF27E73AC44](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/8151318698234E84A9952FF27E73AC44)

**2、NAT模式，虚拟机可以访问宿主机和网络，宿主机不能访问虚拟机。**

​    如果你的网络ip资源紧缺，但是你又希望你的虚拟机能够联网，这时候NAT模式是最好的选择。NAT模式借助虚拟NAT设备和虚拟DHCP服务器，使得虚拟机可以联网。

​    在NAT模式中，主机网卡直接与虚拟NAT设备相连，然后虚拟NAT设备与虚拟DHCP服务器一起连接在虚拟交换机VMnet8上，这样就实现了虚拟机联网。那么我们会觉得很奇怪，为什么需要虚拟网卡VMware Network Adapter VMnet8呢？原来我们的VMware Network Adapter VMnet8虚拟网卡主要是为了实现主机与虚拟机之间的通信。

![https://note.youdao.com/yws/public/resource/236896997b6ffbaa8e0d92eacd13abbf/D9D67F69F39B47F2ACBF8C29383E33DC](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/D9D67F69F39B47F2ACBF8C29383E33DC)

![https://note.youdao.com/yws/public/resource/236896997b6ffbaa8e0d92eacd13abbf/D9F4EAFA17D04025949A8100760B4B6B](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/D9F4EAFA17D04025949A8100760B4B6B)

![https://note.youdao.com/yws/public/resource/236896997b6ffbaa8e0d92eacd13abbf/167E95C63FBB45DA8FB1B1A6EA98AF36](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/167E95C63FBB45DA8FB1B1A6EA98AF36)

**3、Host-Only模式，虚拟机和宿主机可以互相访问，但是虚拟机不能访问网络。**

​    Host-Only模式其实就是NAT模式去除了虚拟NAT设备，然后使用VMware Network Adapter VMnet1虚拟网卡连接VMnet1虚拟交换机来与虚拟机通信的，Host-Only模式将虚拟机与外网隔开，使得虚拟机成为一个独立的系统，只与主机相互通讯。

![https://note.youdao.com/yws/public/resource/236896997b6ffbaa8e0d92eacd13abbf/9A71328903184374A84E0097D6776105](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/9A71328903184374A84E0097D6776105)

​    

#### [NAT模式下，虚拟机无法ping通物理机](https://bbs.csdn.net/topics/391861844)

虚拟机A1、A2是主机A中的虚拟机，虚拟机B1是主机B中的虚拟机。其中的“NAT路由器”是只启用了NAT功能的路由器，用来把VMnet8交换机上连接的计算机通过NAT功能连接到VMnet0虚拟交换机。A1、A2、B1设置为NAT方式，此时A1、A2可以单向访问主机B、C，而B、C不能访问A1、A2；B1可以单向访问主机A、C，而A、C不能访问B1；A1、A2与A，B1与B可以互访。
![img](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/1447937435_669638.jpg)

#### [Linux 下VMWare虚拟机下的几种网络连接方式以及和windows之间的文件传输](https://www.iteye.com/blog/wangshirufeng-2276231)

![image-20220214202355316](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/image-20220214202355316.png)

![image-20220214202402820](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/image-20220214202402820.png)

设置IP地址的时候 以下不能使用：
192.168.191.0   代表网络号

192.168.191.255 代表广播地址

192.168.191.2   代表网关

192.168.191.1   这个被主机用了 (windows主机)

 所以能用的IP地址就只有3~254了。


