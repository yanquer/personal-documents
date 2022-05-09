
## 在 Linux 下使用 RAID


### 在 Linux 下使用 RAID（一）：介绍 RAID 的级别和概念

作者： [Babin Lonston](http://www.tecmint.com/understanding-raid-setup-in-linux/) 译者： [LCTT](https://linux.cn/lctt/) [struggling](https://linux.cn/lctt/strugglingyouth) | 2015-08-24 17:33  评论: [*4*](https://linux.cn/portal.php?mod=comment&id=6085&idtype=aid) 收藏: *20*  

RAID 的意思是廉价磁盘冗余阵列（Redundant Array of Inexpensive Disks），但现在它被称为独立磁盘冗余阵列（Redundant Array of Independent Drives）。早先一个容量很小的磁盘都是非常昂贵的，但是现在我们可以很便宜的买到一个更大的磁盘。Raid 是一系列放在一起，成为一个逻辑卷的磁盘集合。

 [在 Linux 中理解 RAID 设置]
*在 Linux 中理解 RAID 设置*

RAID 包含一组或者一个集合甚至一个阵列。使用一组磁盘结合驱动器组成 RAID 阵列或 RAID 集。将至少两个磁盘连接到一个 RAID 控制器，而成为一个逻辑卷，也可以将多个驱动器放在一个组中。一组磁盘只能使用一个 RAID 级别。使用 RAID 可以提高服务器的性能。不同 RAID 的级别，性能会有所不同。它通过容错和高可用性来保存我们的数据。

这个系列被命名为“在 Linux 下使用 RAID”，分为9个部分，包括以下主题：

- 第1部分：[介绍 RAID 的级别和概念](https://linux.cn/article-6085-1.html)
- 第2部分：[在Linux中如何设置 RAID0（条带化）](https://linux.cn/article-6087-1.html)
- 第3部分：[在Linux中如何设置 RAID1（镜像化）](https://linux.cn/article-6093-1.html)
- 第4部分：[在Linux中如何设置 RAID5（条带化与分布式奇偶校验）](https://linux.cn/article-6102-1.html)
- 第5部分：[在Linux中如何设置 RAID6（条带双分布式奇偶校验）](https://linux.cn/article-6121-1.html)
- 第6部分：[在Linux中设置 RAID 10 或1 + 0（嵌套）](https://linux.cn/article-6122-1.html)
- 第7部分：[扩展现有的 RAID 阵列和删除故障的磁盘](https://linux.cn/article-6123-1.html)
- 第8部分：[在 RAID 中恢复（重建）损坏的驱动器](https://linux.cn/article-6448-1.html)
- 第9部分：[在 Linux 中管理 RAID](https://linux.cn/article-6463-1.html)

这是9篇系列教程的第1部分，在这里我们将介绍 RAID 的概念和 RAID 级别，这是在 Linux 中构建 RAID 需要理解的。

#### 软件 RAID 和硬件 RAID

软件 RAID 的性能较低，因为其使用主机的资源。 需要加载 RAID 软件以从软件 RAID 卷中读取数据。在加载 RAID 软件前，操作系统需要引导起来才能加载 RAID 软件。在软件 RAID 中无需物理硬件。零成本投资。

硬件 RAID 的性能较高。他们采用 PCI Express 卡物理地提供有专用的 RAID 控制器。它不会使用主机资源。他们有 NVRAM 用于缓存的读取和写入。缓存用于 RAID 重建时，即使出现电源故障，它会使用后备的电池电源保持缓存。对于大规模使用是非常昂贵的投资。

硬件 RAID 卡如下所示：

[硬件 RAID]

*硬件 RAID*

##### 重要的 RAID 概念

- **校验**方式用在 RAID 重建中从校验所保存的信息中重新生成丢失的内容。 RAID 5，RAID 6 基于校验。
- **条带化**是将切片数据随机存储到多个磁盘。它不会在单个磁盘中保存完整的数据。如果我们使用2个磁盘，则每个磁盘存储我们的一半数据。
- **镜像**被用于 RAID 1 和 RAID 10。镜像会自动备份数据。在 RAID 1 中，它会保存相同的内容到其他盘上。
- **热备份**只是我们的服务器上的一个备用驱动器，它可以自动更换发生故障的驱动器。在我们的阵列中，如果任何一个驱动器损坏，热备份驱动器会自动用于重建 RAID。
- **块**是 RAID 控制器每次读写数据时的最小单位，最小 4KB。通过定义块大小，我们可以增加 I/O 性能。

RAID有不同的级别。在这里，我们仅列出在真实环境下的使用最多的 RAID 级别。

- RAID0 = 条带化
- RAID1 = 镜像
- RAID5 = 单磁盘分布式奇偶校验
- RAID6 = 双磁盘分布式奇偶校验
- RAID10 = 镜像 + 条带。（嵌套RAID）

RAID 在大多数 Linux 发行版上使用名为 mdadm 的软件包进行管理。让我们先对每个 RAID 级别认识一下。

##### RAID 0 / 条带化


条带化有很好的性能。在 RAID 0（条带化）中数据将使用切片的方式被写入到磁盘。一半的内容放在一个磁盘上，另一半内容将被写入到另一个磁盘。

假设我们有2个磁盘驱动器，例如，如果我们将数据“TECMINT”写到逻辑卷中，“T”将被保存在第一盘中，“E”将保存在第二盘，'C'将被保存在第一盘，“M”将保存在第二盘，它会一直继续此循环过程。（LCTT 译注：实际上不可能按字节切片，是按数据块切片的。）

在这种情况下，如果驱动器中的任何一个发生故障，我们就会丢失数据，因为一个盘中只有一半的数据，不能用于重建 RAID。不过，当比较写入速度和性能时，RAID 0 是非常好的。创建 RAID 0（条带化）至少需要2个磁盘。如果你的数据是非常宝贵的，那么不要使用此 RAID 级别。

- 高性能。
- RAID 0 中容量零损失。
- 零容错。
- 写和读有很高的性能。

##### RAID 1 / 镜像化



镜像也有不错的性能。镜像可以对我们的数据做一份相同的副本。假设我们有两个2TB的硬盘驱动器，我们总共有4TB，但在镜像中，但是放在 RAID 控制器后面的驱动器形成了一个逻辑驱动器，我们只能看到这个逻辑驱动器有2TB。

当我们保存数据时，它将同时写入这两个2TB驱动器中。创建 RAID 1（镜像化）最少需要两个驱动器。如果发生磁盘故障，我们可以通过更换一个新的磁盘恢复 RAID 。如果在 RAID 1 中任何一个磁盘发生故障，我们可以从另一个磁盘中获取相同的数据，因为另外的磁盘中也有相同的数据。所以是零数据丢失。

- 良好的性能。
- 总容量丢失一半可用空间。
- 完全容错。
- 重建会更快。
- 写性能变慢。
- 读性能变好。
- 能用于操作系统和小规模的数据库。

##### RAID 5 / 分布式奇偶校验



RAID 5 多用于企业级。 RAID 5 的以分布式奇偶校验的方式工作。奇偶校验信息将被用于重建数据。它从剩下的正常驱动器上的信息来重建。在驱动器发生故障时，这可以保护我们的数据。

假设我们有4个驱动器，如果一个驱动器发生故障而后我们更换发生故障的驱动器后，我们可以从奇偶校验中重建数据到更换的驱动器上。奇偶校验信息存储在所有的4个驱动器上，如果我们有4个 1TB 的驱动器。奇偶校验信息将被存储在每个驱动器的256G中，而其它768GB是用户自己使用的。单个驱动器故障后，RAID 5 依旧正常工作，如果驱动器损坏个数超过1个会导致数据的丢失。

- 性能卓越
- 读速度将非常好。
- 写速度处于平均水准，如果我们不使用硬件 RAID 控制器，写速度缓慢。
- 从所有驱动器的奇偶校验信息中重建。
- 完全容错。
- 1个磁盘空间将用于奇偶校验。
- 可以被用在文件服务器，Web服务器，非常重要的备份中。

##### RAID 6 双分布式奇偶校验磁盘



RAID 6 和 RAID 5 相似但它有两个分布式奇偶校验。大多用在大数量的阵列中。我们最少需要4个驱动器，即使有2个驱动器发生故障，我们依然可以更换新的驱动器后重建数据。

它比 RAID 5 慢，因为它将数据同时写到4个驱动器上。当我们使用硬件 RAID 控制器时速度就处于平均水准。如果我们有6个的1TB驱动器，4个驱动器将用于数据保存，2个驱动器将用于校验。

- 性能不佳。
- 读的性能很好。
- 如果我们不使用硬件 RAID 控制器写的性能会很差。
- 从两个奇偶校验驱动器上重建。
- 完全容错。
- 2个磁盘空间将用于奇偶校验。
- 可用于大型阵列。
- 用于备份和视频流中，用于大规模。

##### RAID 10 / 镜像+条带





RAID 10 可以被称为1 + 0或0 +1。它将做镜像+条带两个工作。在 RAID 10 中首先做镜像然后做条带。在 RAID 01 上首先做条带，然后做镜像。RAID 10 比 01 好。

假设，我们有4个驱动器。当我逻辑卷上写数据时，它会使用镜像和条带的方式将数据保存到4个驱动器上。

如果我在 RAID 10 上写入数据“TECMINT”，数据将使用如下方式保存。首先将“T”同时写入两个磁盘，“E”也将同时写入另外两个磁盘，所有数据都写入两块磁盘。这样可以将每个数据复制到另外的磁盘。

同时它将使用 RAID 0 方式写入数据，遵循将“T”写入第一组盘，“E”写入第二组盘。再次将“C”写入第一组盘，“M”到第二组盘。

- 良好的读写性能。
- 总容量丢失一半的可用空间。
- 容错。
- 从副本数据中快速重建。
- 由于其高性能和高可用性，常被用于数据库的存储中。

#### 结论

在这篇文章中，我们已经了解了什么是 RAID 和在实际环境大多采用哪个级别的 RAID。希望你已经学会了上面所写的。对于 RAID 的构建必须了解有关 RAID 的基本知识。以上内容可以基本满足你对 RAID 的了解。

在接下来的文章中，我将介绍如何设置和使用各种级别创建 RAID，增加 RAID 组（阵列）和驱动器故障排除等。











### 在 Linux 下使用 RAID（二）：使用 mdadm 工具创建软件 RAID 0 （条带化）

作者： [Babin Lonston](http://www.tecmint.com/create-raid0-in-linux/) 译者： [LCTT](https://linux.cn/lctt/) [struggling](https://linux.cn/lctt/strugglingyouth) | 2015-08-25 09:25  评论: [*9*](https://linux.cn/portal.php?mod=comment&id=6087&idtype=aid) 收藏: *10*  

RAID 即廉价磁盘冗余阵列，其高可用性和可靠性适用于大规模环境中，相比正常使用，数据更需要被保护。RAID 是一些磁盘的集合，是包含一个阵列的逻辑卷。驱动器可以组合起来成为一个阵列或称为（组的）集合。

创建 RAID 最少应使用2个连接到 RAID 控制器的磁盘组成，来构成逻辑卷，可以根据定义的 RAID 级别将更多的驱动器添加到一个阵列中。不使用物理硬件创建的 RAID 被称为软件 RAID。软件 RAID 也叫做穷人 RAID。



*在 Linux 中创建 RAID0*

使用 RAID 的主要目的是为了在发生单点故障时保存数据，如果我们使用单个磁盘来存储数据，如果它损坏了，那么就没有机会取回我们的数据了，为了防止数据丢失我们需要一个容错的方法。所以，我们可以使用多个磁盘组成 RAID 阵列。

##### 在 RAID 0 中条带是什么

条带是通过将数据在同时分割到多个磁盘上。假设我们有两个磁盘，如果我们将数据保存到该逻辑卷上，它会将数据保存在两个磁盘上。使用 RAID 0 是为了获得更好的性能，但是如果驱动器中一个出现故障，我们将不能得到完整的数据。因此，使用 RAID 0 不是一种好的做法。唯一的解决办法就是安装有 RAID 0 逻辑卷的操作系统来提高重要文件的安全性。

- RAID 0 性能较高。
- 在 RAID 0 上，空间零浪费。
- 零容错（如果硬盘中的任何一个发生故障，无法取回数据）。
- 写和读性能都很好。

##### 要求

创建 RAID 0 允许的最小磁盘数目是2个，但你可以添加更多的磁盘，不过数目应该是2，4，6，8等的偶数。如果你有一个物理 RAID 卡并且有足够的端口，你可以添加更多磁盘。

在这里，我们没有使用硬件 RAID，此设置只需要软件 RAID。如果我们有一个物理硬件 RAID 卡，我们可以从它的功能界面访问它。有些主板默认内建 RAID 功能，还可以使用 Ctrl + I 键访问它的界面。

如果你是刚开始设置 RAID，请阅读我们前面的文章，我们已经介绍了一些关于 RAID 基本的概念。

- [介绍 RAID 的级别和概念](https://linux.cn/article-6085-1.html)

**我的服务器设置**

```
操作系统 :  CentOS 6.5 FinalIP 地址    :  192.168.0.225两块盘    :  20 GB each
```

这是9篇系列教程的第2部分，在这部分，我们将看看如何能够在 Linux 上创建和使用 RAID 0（条带化），以名为 sdb 和 sdc 两个 20GB 的硬盘为例。

#### 第1步：更新系统和安装管理 RAID 的 mdadm 软件

1、 在 Linux 上设置 RAID 0 前，我们先更新一下系统，然后安装`mdadm` 包。mdadm 是一个小程序，这将使我们能够在Linux下配置和管理 RAID 设备。

```
### yum clean all && yum update### yum install mdadm -y
```



*安装 mdadm 工具*

#### 第2步：确认连接了两个 20GB 的硬盘

2、 在创建 RAID 0 前，请务必确认两个硬盘能被检测到，使用下面的命令确认。

```
### ls -l /dev | grep sd
```



*检查硬盘*

3、 一旦检测到新的硬盘驱动器，同时检查是否连接的驱动器已经被现有的 RAID 使用，使用下面的`mdadm` 命令来查看。

```
### mdadm --examine /dev/sd[b-c]
```



*检查 RAID 设备*

从上面的输出我们可以看到，没有任何 RAID 使用 sdb 和 sdc 这两个驱动器。

#### 第3步：创建 RAID 分区

4、 现在用 sdb 和 sdc 创建 RAID 的分区，使用 fdisk 命令来创建。在这里，我将展示如何创建 sdb 驱动器上的分区。

```
### fdisk /dev/sdb
```

请按照以下说明创建分区。

- 按`n` 创建新的分区。
- 然后按`P` 选择主分区。
- 接下来选择分区号为1。
- 只需按两次回车键选择默认值即可。
- 然后，按`P` 来显示创建好的分区。



*创建分区*

请按照以下说明将分区创建为 Linux 的 RAID 类型。

- 按`L`，列出所有可用的类型。
- 按`t` 去修改分区。
- 键入`fd` 设置为 Linux 的 RAID 类型，然后按回车确认。
- 然后再次使用`p`查看我们所做的更改。
- 使用`w`保存更改。



*在 Linux 上创建 RAID 分区*

**注**: 请使用上述步骤同样在 sdc 驱动器上创建分区。

5、 创建分区后，验证这两个驱动器是否正确定义 RAID，使用下面的命令。

```
### mdadm --examine /dev/sd[b-c]### mdadm --examine /dev/sd[b-c]1
```



*验证 RAID 分区*

#### 第4步：创建 RAID md 设备

6、 现在使用以下命令创建 md 设备（即 /dev/md0），并选择 RAID 合适的级别。

```
### mdadm -C /dev/md0 -l raid0 -n 2 /dev/sd[b-c]1### mdadm --create /dev/md0 --level=stripe --raid-devices=2 /dev/sd[b-c]1
```

- -C – 创建
- -l – 级别
- -n – RAID 设备数

7、 一旦 md 设备已经建立，使用如下命令可以查看 RAID 级别，设备和阵列的使用状态。

```
### cat /proc/mdstat
```



*查看 RAID 级别*

```
### mdadm -E /dev/sd[b-c]1
```



*查看 RAID 设备*

```
### mdadm --detail /dev/md0
```



*查看 RAID 阵列*

#### 第5步：给 RAID 设备创建文件系统

8、 将 RAID 设备 /dev/md0 创建为 ext4 文件系统，并挂载到 /mnt/raid0 下。

```
### mkfs.ext4 /dev/md0
```



*创建 ext4 文件系统*

9、 在 RAID 设备上创建好 ext4 文件系统后，现在创建一个挂载点（即 /mnt/raid0），并将设备 /dev/md0 挂载在它下。

```
### mkdir /mnt/raid0### mount /dev/md0 /mnt/raid0/
```

10、下一步，使用 df 命令验证设备 /dev/md0 是否被挂载在 /mnt/raid0 下。

```
### df -h
```

11、 接下来，在挂载点 /mnt/raid0 下创建一个名为`tecmint.txt` 的文件，为创建的文件添加一些内容，并查看文件和目录的内容。

```
### touch /mnt/raid0/tecmint.txt### echo "Hi everyone how you doing ?" > /mnt/raid0/tecmint.txt### cat /mnt/raid0/tecmint.txt### ls -l /mnt/raid0/
```



*验证挂载的设备*

12、 当你验证挂载点后，就可以将它添加到 /etc/fstab 文件中。

```
### vim /etc/fstab
```

添加以下条目，根据你的安装位置和使用文件系统的不同，自行做修改。

```
/dev/md0                /mnt/raid0              ext4    deaults         0 0
```



*添加设备到 fstab 文件中*

13、 使用 mount 命令的 `-a` 来检查 fstab 的条目是否有误。

```
### mount -av
```



*检查 fstab 文件是否有误*

#### 第6步：保存 RAID 配置

14、 最后，保存 RAID 配置到一个文件中，以供将来使用。我们再次使用带有`-s` (scan) 和`-v` (verbose) 选项的 `mdadm` 命令，如图所示。

```
### mdadm -E -s -v >> /etc/mdadm.conf### mdadm --detail --scan --verbose >> /etc/mdadm.conf  ### cat /etc/mdadm.conf
```



*保存 RAID 配置*

就这样，我们在这里看到，如何通过使用两个硬盘配置具有条带化的 RAID 0 。在接下来的文章中，我们将看到如何设置 RAID 1。

------

via: http://www.tecmint.com/create-raid0-in-linux/

作者：[Babin Lonston](http://www.tecmint.com/author/babinlonston/) 译者：[strugglingyouth](https://github.com/strugglingyouth) 校对：[wxy](https://github.com/wxy)

本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](https://linux.cn/article-6087-1.html) 荣誉推出





#### 最新评论



- 来自北京的 Chrome 43.0|Windows 7 用户 2015-12-02 12:46[4 赞](https://linux.cn/portal.php?mod=review&action=postreview&do=support&idtype=aid&tid=6087&pid=36536&hash=5522402f) [回复](https://linux.cn/portal.php?mod=portalcp&ac=comment&op=reply&cid=36536&aid=6087&idtype=)

  这年头还搞软raid，让硬件生产商如何生活。



- [XYJK1002 [Chrome 42.0|Windows 7\]](https://linux.cn/space/20893/) 2015-10-03 19:13[9 赞](https://linux.cn/portal.php?mod=review&action=postreview&do=support&idtype=aid&tid=6087&pid=35399&hash=5522402f) [回复](https://linux.cn/portal.php?mod=portalcp&ac=comment&op=reply&cid=35399&aid=6087&idtype=)

  讨论的这么激烈。。。



- [linux [Chrome 44.0|Mac 10.10\]](https://linux.cn/space/1/) 2015-08-28 09:01[3 赞](https://linux.cn/portal.php?mod=review&action=postreview&do=support&idtype=aid&tid=6087&pid=34761&hash=5522402f) [回复](https://linux.cn/portal.php?mod=portalcp&ac=comment&op=reply&cid=34761&aid=6087&idtype=)

  系统崩溃时，输出的数据没准都是错误的，硬件 RAID 卡也无法防范这点。只是避免了在 IO 系统将数据送到 RAID 卡后的错误。



- 来自云南昆明的 Chrome 41.0|Windows 7 用户 2015-08-26 11:27[4 赞](https://linux.cn/portal.php?mod=review&action=postreview&do=support&idtype=aid&tid=6087&pid=34719&hash=5522402f) [回复](https://linux.cn/portal.php?mod=portalcp&ac=comment&op=reply&cid=34719&aid=6087&idtype=)

  以前建 RAID5 时，重启后 /dev/md0 名字就变了，也不知道怎么改回来，后面才知道是 /etc/mdadm.conf 的问题











### 在 Linux 下使用 RAID（三）：用两块磁盘创建 RAID 1（镜像）

作者： [Babin Lonston](http://www.tecmint.com/create-raid1-in-linux/) 译者： [LCTT](https://linux.cn/lctt/) [struggling](https://linux.cn/lctt/strugglingyouth) | 2015-08-26 09:33  评论: [*9*](https://linux.cn/portal.php?mod=comment&id=6093&idtype=aid) 收藏: *9*  

**RAID 镜像**意味着相同数据的完整克隆（或镜像），分别写入到两个磁盘中。创建 RAID 1 至少需要两个磁盘，而且仅用于读取性能或者可靠性要比数据存储容量更重要的场合。



*在 Linux 中设置 RAID 1*

创建镜像是为了防止因硬盘故障导致数据丢失。镜像中的每个磁盘包含数据的完整副本。当一个磁盘发生故障时，相同的数据可以从其它正常磁盘中读取。而后，可以从正在运行的计算机中直接更换发生故障的磁盘，无需任何中断。

#### RAID 1 的特点

- 镜像具有良好的性能。
- 磁盘利用率为50％。也就是说，如果我们有两个磁盘每个500GB，总共是1TB，但在镜像中它只会显示500GB。
- 在镜像如果一个磁盘发生故障不会有数据丢失，因为两个磁盘中的内容相同。
- 读取性能会比写入性能更好。

##### 要求

创建 RAID 1 至少要有两个磁盘，你也可以添加更多的磁盘，磁盘数需为2，4，6，8等偶数。要添加更多的磁盘，你的系统必须有 RAID 物理适配器（硬件卡）。

这里，我们使用软件 RAID 不是硬件 RAID，如果你的系统有一个内置的物理硬件 RAID 卡，你可以从它的功能界面或使用 Ctrl + I 键来访问它。

需要阅读: [介绍 RAID 的级别和概念](https://linux.cn/article-6085-1.html)

##### 在我的服务器安装

```
操作系统 :  CentOS 6.5 FinalIP 地址    :  192.168.0.226主机名    :  rd1.tecmintlocal.com磁盘 1 [20GB]  :  /dev/sdb磁盘 2 [20GB]  :  /dev/sdc
```

本文将指导你在 Linux 平台上使用 mdadm （用于创建和管理 RAID ）一步步的建立一个软件 RAID 1 （镜像）。同样的做法也适用于如 RedHat，CentOS，Fedora 等 Linux 发行版。

#### 第1步：安装所需软件并且检查磁盘

1、 正如我前面所说，在 Linux 中我们需要使用 mdadm 软件来创建和管理 RAID。所以，让我们用 yum 或 apt-get 的软件包管理工具在 Linux 上安装 mdadm 软件包。

```
### yum install mdadm     [在 RedHat 系统]### apt-get install mdadm     [在 Debain 系统]
```

2、 一旦安装好`mdadm`包，我们需要使用下面的命令来检查磁盘是否已经配置好。

```
### mdadm -E /dev/sd[b-c]
```



*检查 RAID 的磁盘*

正如你从上面图片看到的，没有检测到任何超级块，这意味着还没有创建RAID。

#### 第2步：为 RAID 创建分区

3、 正如我提到的，我们使用最少的两个分区 /dev/sdb 和 /dev/sdc 来创建 RAID 1。我们首先使用`fdisk`命令来创建这两个分区并更改其类型为 raid。

```
### fdisk /dev/sdb
```

按照下面的说明

- 按 `n` 创建新的分区。
- 然后按 `P` 选择主分区。
- 接下来选择分区号为1。
- 按两次回车键默认将整个容量分配给它。
- 然后，按 `P` 来打印创建好的分区。
- 按 `L`，列出所有可用的类型。
- 按 `t` 修改分区类型。
- 键入 `fd` 设置为 Linux 的 RAID 类型，然后按 Enter 确认。
- 然后再次使用`p`查看我们所做的更改。
- 使用`w`保存更改。



*创建磁盘分区*

在创建“/dev/sdb”分区后，接下来按照同样的方法创建分区 /dev/sdc 。

```
### fdisk /dev/sdc
```



*创建第二个分区*

4、 一旦这两个分区创建成功后，使用相同的命令来检查 sdb 和 sdc 分区并确认 RAID 分区的类型如上图所示。

```
### mdadm -E /dev/sd[b-c]
```



*验证分区变化*



*检查 RAID 类型*

**注意**: 正如你在上图所看到的，在 sdb1 和 sdc1 中没有任何对 RAID 的定义，这就是我们没有检测到超级块的原因。

#### 第3步：创建 RAID 1 设备

5、 接下来使用以下命令来创建一个名为 /dev/md0 的“RAID 1”设备并验证它

```
### mdadm --create /dev/md0 --level=mirror --raid-devices=2 /dev/sd[b-c]1### cat /proc/mdstat
```



*创建RAID设备*

6、 接下来使用如下命令来检查 RAID 设备类型和 RAID 阵列

```
### mdadm -E /dev/sd[b-c]1### mdadm --detail /dev/md0
```



*检查 RAID 设备类型*

![检查 RAID 设备阵列](https://img.linux.net.cn/data/attachment/album/201508/25/233650tr1n1dgr9kw11eed.png)

*检查 RAID 设备阵列*

从上图中，人们很容易理解，RAID 1 已经创建好了，使用了 /dev/sdb1 和 /dev/sdc1 分区，你也可以看到状态为 resyncing（重新同步中）。

#### 第4步：在 RAID 设备上创建文件系统

7、 给 md0 上创建 ext4 文件系统

```
### mkfs.ext4 /dev/md0
```

![创建 RAID 设备文件系统](https://img.linux.net.cn/data/attachment/album/201508/25/233651cuh9wdfud340lgx4.png)

*创建 RAID 设备文件系统*

8、 接下来，挂载新创建的文件系统到“/mnt/raid1”，并创建一些文件，验证在挂载点的数据

```
### mkdir /mnt/raid1### mount /dev/md0 /mnt/raid1/### touch /mnt/raid1/tecmint.txt### echo "tecmint raid setups" > /mnt/raid1/tecmint.txt
```

![挂载 RAID 设备](https://img.linux.net.cn/data/attachment/album/201508/25/233654e8811zd8s112758z.png)

*挂载 RAID 设备*

9、为了在系统重新启动自动挂载 RAID 1，需要在 fstab 文件中添加条目。打开`/etc/fstab`文件并添加以下行：

```
/dev/md0                /mnt/raid1              ext4    defaults        0 0
```

![自动挂载 Raid 设备](https://img.linux.net.cn/data/attachment/album/201508/25/233656biaaun89ffnbybed.png)

*自动挂载 Raid 设备*

10、 运行`mount -av`，检查 fstab 中的条目是否有错误

```
### mount -av
```

![检查 fstab 中的错误](https://img.linux.net.cn/data/attachment/album/201508/25/233657q5rg2ag1ah8x3xym.png)

*检查 fstab 中的错误*

11、 接下来，使用下面的命令保存 RAID 的配置到文件“mdadm.conf”中。

```
### mdadm --detail --scan --verbose >> /etc/mdadm.conf
```

![保存 Raid 的配置](https://img.linux.net.cn/data/attachment/album/201508/25/233658kuh9nn3hk08ejdjk.png)

*保存 Raid 的配置*

上述配置文件在系统重启时会读取并加载 RAID 设备。

#### 第5步：在磁盘故障后检查数据

12、我们的主要目的是，即使在任何磁盘故障或死机时必须保证数据是可用的。让我们来看看，当任何一个磁盘不可用时会发生什么。

```
### mdadm --detail /dev/md0
```

![验证 RAID 设备](https://img.linux.net.cn/data/attachment/album/201508/25/233702k70s9wjjk9i10prp.png)

*验证 RAID 设备*

在上面的图片中，我们可以看到在 RAID 中有2个设备是可用的，并且 Active Devices 是2。现在让我们看看，当一个磁盘拔出（移除 sdc 磁盘）或损坏后会发生什么。

```
### ls -l /dev | grep sd### mdadm --detail /dev/md0
```

![测试 RAID 设备](https://img.linux.net.cn/data/attachment/album/201508/25/233706gurve5xd113xu5p3.png)

*测试 RAID 设备*

现在，在上面的图片中你可以看到，一个磁盘不见了。我从虚拟机上删除了一个磁盘。此时让我们来检查我们宝贵的数据。

```
### cd /mnt/raid1/### cat tecmint.txt
```

![验证 RAID 数据](https://img.linux.net.cn/data/attachment/album/201508/25/233708stgpt5dxz5yahkpm.png)

*验证 RAID 数据*

你可以看到我们的数据仍然可用。由此，我们可以了解 RAID 1（镜像）的优势。在接下来的文章中，我们将看到如何设置一个 RAID 5 条带化分布式奇偶校验。希望这可以帮助你了解 RAID 1（镜像）是如何工作的。









### 在 Linux 下使用 RAID（四）：创建 RAID 5（条带化与分布式奇偶校验）

作者： [Babin Lonston](http://www.tecmint.com/create-raid-5-in-linux/) 译者： [LCTT](https://linux.cn/lctt/) [struggling](https://linux.cn/lctt/strugglingyouth) | 2015-08-27 13:08  收藏: *9*  

在 RAID 5 中，数据条带化后存储在分布式奇偶校验的多个磁盘上。分布式奇偶校验的条带化意味着它将奇偶校验信息和条带化数据分布在多个磁盘上，这样会有很好的数据冗余。

![在 Linux 中配置 RAID 5](https://img.linux.net.cn/data/attachment/album/201508/27/130847s7r7w37hd47reviu.jpg)

*在 Linux 中配置 RAID 5*

对于此 RAID 级别它至少应该有三个或更多个磁盘。RAID 5 通常被用于大规模生产环境中，以花费更多的成本来提供更好的数据冗余性能。

##### 什么是奇偶校验？

奇偶校验是在数据存储中检测错误最简单的常见方式。奇偶校验信息存储在每个磁盘中，比如说，我们有4个磁盘，其中相当于一个磁盘大小的空间被分割去存储所有磁盘的奇偶校验信息。如果任何一个磁盘出现故障，我们可以通过更换故障磁盘后，从奇偶校验信息重建得到原来的数据。

##### RAID 5 的优点和缺点

- 提供更好的性能。
- 支持冗余和容错。
- 支持热备份。
- 将用掉一个磁盘的容量存储奇偶校验信息。
- 单个磁盘发生故障后不会丢失数据。我们可以更换故障硬盘后从奇偶校验信息中重建数据。
- 适合于面向事务处理的环境，读操作会更快。
- 由于奇偶校验占用资源，写操作会慢一些。
- 重建需要很长的时间。

##### 要求

创建 RAID 5 最少需要3个磁盘，你也可以添加更多的磁盘，前提是你要有多端口的专用硬件 RAID 控制器。在这里，我们使用“mdadm”包来创建软件 RAID。

mdadm 是一个允许我们在 Linux 下配置和管理 RAID 设备的包。默认情况下没有 RAID 的配置文件，我们在创建和配置 RAID 后必须将配置文件保存在一个单独的文件 mdadm.conf 中。

在进一步学习之前，我建议你通过下面的文章去了解 Linux 中 RAID 的基础知识。

- [介绍 RAID 的级别和概念](https://linux.cn/article-6085-1.html)
- [使用 mdadm 工具创建软件 RAID 0 （条带化）](https://linux.cn/article-6087-1.html)
- [用两块磁盘创建 RAID 1（镜像）](https://linux.cn/article-6093-1.html)

##### 我的服务器设置

```
操作系统 :  CentOS 6.5 FinalIP 地址  :    192.168.0.227主机名    :  rd5.tecmintlocal.com磁盘 1 [20GB]  :  /dev/sdb磁盘 2 [20GB]  :  /dev/sdc磁盘 3 [20GB]  :  /dev/sdd
```

这是9篇系列教程的第4部分，在这里我们要在 Linux 系统或服务器上使用三个20GB（名为/dev/sdb, /dev/sdc 和 /dev/sdd）的磁盘建立带有分布式奇偶校验的软件 RAID 5。

#### 第1步：安装 mdadm 并检验磁盘

1、 正如我们前面所说，我们使用 CentOS 6.5 Final 版本来创建 RAID 设置，但同样的做法也适用于其他 Linux 发行版。

```
### lsb_release -a### ifconfig | grep inet
```

![CentOS 6.5 摘要](https://img.linux.net.cn/data/attachment/album/201508/27/130850ee55ppie744v2tfz.png)

*CentOS 6.5 摘要*

2、 如果你按照我们的 RAID 系列去配置的，我们假设你已经安装了“mdadm”包，如果没有，根据你的 Linux 发行版使用下面的命令安装。

```
### yum install mdadm     [在 RedHat 系统]### apt-get install mdadm     [在 Debain 系统]
```

3、 “mdadm”包安装后，先使用`fdisk`命令列出我们在系统上增加的三个20GB的硬盘。

```
### fdisk -l | grep sd
```

![安装 mdadm 工具](https://img.linux.net.cn/data/attachment/album/201508/27/130852c3lo7o7us388272i.png)

*安装 mdadm 工具*

4、 现在该检查这三个磁盘是否存在 RAID 块，使用下面的命令来检查。

```
### mdadm -E /dev/sd[b-d]### mdadm --examine /dev/sdb /dev/sdc /dev/sdd ### 或
```

![检查 Raid 磁盘](https://img.linux.net.cn/data/attachment/album/201508/27/130853i6x2mit2623ii22a.png)

*检查 Raid 磁盘*

**注意**: 上面的图片说明，没有检测到任何超级块。所以，这三个磁盘中没有定义 RAID。让我们现在开始创建一个吧！

#### 第2步：为磁盘创建 RAID 分区

5、 首先，在创建 RAID 前磁盘（/dev/sdb, /dev/sdc 和 /dev/sdd）必须有分区，因此，在进行下一步之前，先使用`fdisk`命令进行分区。

```
### fdisk /dev/sdb### fdisk /dev/sdc### fdisk /dev/sdd
```

##### 创建 /dev/sdb 分区

请按照下面的说明在 /dev/sdb 硬盘上创建分区。

- 按 `n` 创建新的分区。
- 然后按 `P` 选择主分区。选择主分区是因为还没有定义过分区。
- 接下来选择分区号为1。默认就是1。
- 这里是选择柱面大小，我们没必要选择指定的大小，因为我们需要为 RAID 使用整个分区，所以只需按两次 Enter 键默认将整个容量分配给它。
- 然后，按 `P` 来打印创建好的分区。
- 改变分区类型，按 `L`可以列出所有可用的类型。
- 按 `t` 修改分区类型。
- 这里使用`fd`设置为 RAID 的类型。
- 然后再次使用`p`查看我们所做的更改。
- 使用`w`保存更改。

![创建 sdb 分区](https://img.linux.net.cn/data/attachment/album/201508/27/130856poxxznqnlvxlq9vi.png)

*创建 sdb 分区*

**注意**: 我们仍要按照上面的步骤来创建 sdc 和 sdd 的分区。

##### 创建 /dev/sdc 分区

现在，通过下面的截图给出创建 sdc 和 sdd 磁盘分区的方法，或者你可以按照上面的步骤。

```
### fdisk /dev/sdc
```

![创建 sdc 分区](https://img.linux.net.cn/data/attachment/album/201508/27/130901h6ip9bdrd6oipybe.png)

*创建 sdc 分区*

##### 创建 /dev/sdd 分区

```
### fdisk /dev/sdd
```

![创建 sdd 分区](https://img.linux.net.cn/data/attachment/album/201508/27/130905x909oandrn589x95.png)

*创建 sdd 分区*

6、 创建分区后，检查三个磁盘 sdb, sdc, sdd 的变化。

```
### mdadm --examine /dev/sdb /dev/sdc /dev/sdd### mdadm -E /dev/sd[b-c]  ### 或
```

![检查磁盘变化](https://img.linux.net.cn/data/attachment/album/201508/27/130906om143zq61i42e3rn.png)

*检查磁盘变化*

**注意**: 在上面的图片中，磁盘的类型是 fd。

7、 现在在新创建的分区检查 RAID 块。如果没有检测到超级块，我们就能够继续下一步，在这些磁盘中创建一个新的 RAID 5 配置。

![Check Raid on Partition](https://img.linux.net.cn/data/attachment/album/201508/27/130907qx999fbytybtx8ny.png)

*Check Raid on Partition*

*在分区中检查 RAID *

#### 第3步：创建 md 设备 md0

8、 现在使用所有新创建的分区(sdb1, sdc1 和 sdd1)创建一个 RAID 设备“md0”（即 /dev/md0），使用以下命令。

```
### mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sdb1 /dev/sdc1 /dev/sdd1### mdadm -C /dev/md0 -l=5 -n=3 /dev/sd[b-d]1   ### 或
```

9、 创建 RAID 设备后，检查并确认 RAID，从 mdstat 中输出中可以看到包括的设备的 RAID 级别。

```
### cat /proc/mdstat
```

![验证 Raid 设备](https://img.linux.net.cn/data/attachment/album/201508/27/130912pomyk5yrz5ixdqyx.png)

*验证 Raid 设备*

如果你想监视当前的创建过程，你可以使用`watch`命令，将 `cat /proc/mdstat` 传递给它，它会在屏幕上显示且每隔1秒刷新一次。

```
### watch -n1 cat /proc/mdstat
```

![监控 RAID 5 构建过程](https://img.linux.net.cn/data/attachment/album/201508/27/130913qaznva7r27626cr1.png)

*监控 RAID 5 构建过程*

![Raid 5 过程概要](https://img.linux.net.cn/data/attachment/album/201508/27/130913anszz9g69ne99gza.png)

*Raid 5 过程概要*

10、 创建 RAID 后，使用以下命令验证 RAID 设备

```
### mdadm -E /dev/sd[b-d]1
```

![验证 Raid 级别](https://img.linux.net.cn/data/attachment/album/201508/27/130915wjyiadnfjyd4vcnm.png)

*验证 Raid 级别*

**注意**: 因为它显示三个磁盘的信息，上述命令的输出会有点长。

11、 接下来，验证 RAID 阵列，假定包含 RAID 的设备正在运行并已经开始了重新同步。

```
### mdadm --detail /dev/md0
```

![验证 RAID 阵列](https://img.linux.net.cn/data/attachment/album/201508/27/130916z8l7c2t8k0z3027t.png)

*验证 RAID 阵列*

#### 第4步：为 md0 创建文件系统

12、 在挂载前为“md0”设备创建 ext4 文件系统。

```
### mkfs.ext4 /dev/md0
```

![创建 md0 文件系统](https://img.linux.net.cn/data/attachment/album/201508/27/130918miicsftizs58i8zc.png)

*创建 md0 文件系统*

13、 现在，在`/mnt`下创建目录 raid5，然后挂载文件系统到 /mnt/raid5/ 下，并检查挂载点下的文件，你会看到 lost+found 目录。

```
### mkdir /mnt/raid5### mount /dev/md0 /mnt/raid5/### ls -l /mnt/raid5/
```

14、 在挂载点 /mnt/raid5 下创建几个文件，并在其中一个文件中添加一些内容然后去验证。

```
### touch /mnt/raid5/raid5_tecmint_{1..5}### ls -l /mnt/raid5/### echo "tecmint raid setups" > /mnt/raid5/raid5_tecmint_1### cat /mnt/raid5/raid5_tecmint_1### cat /proc/mdstat
```

![挂载 RAID 设备](https://img.linux.net.cn/data/attachment/album/201508/27/130923l44wlw00wwpqcjbm.png)

*挂载 RAID 设备*

15、 我们需要在 fstab 中添加条目，否则系统重启后将不会显示我们的挂载点。编辑 fstab 文件添加条目，在文件尾追加以下行。挂载点会根据你环境的不同而不同。

```
### vim /etc/fstab/dev/md0                /mnt/raid5              ext4    defaults        0 0
```

![自动挂载 RAID 5](https://img.linux.net.cn/data/attachment/album/201508/27/130926fery778hefhj7hih.png)

*自动挂载 RAID 5*

16、 接下来，运行`mount -av`命令检查 fstab 条目中是否有错误。

```
### mount -av
```

![检查 Fstab 错误](https://img.linux.net.cn/data/attachment/album/201508/27/130927wuguug4tuuu4tua1.png)

*检查 Fstab 错误*

#### 第5步：保存 Raid 5 的配置

17、 在前面章节已经说过，默认情况下 RAID 没有配置文件。我们必须手动保存。如果此步中没有跟随不属于 md0 的 RAID 设备，它会是一些其他随机数字。

所以，我们必须要在系统重新启动之前保存配置。如果配置保存它在系统重新启动时会被加载到内核中然后 RAID 也将被加载。

```
### mdadm --detail --scan --verbose >> /etc/mdadm.conf
```

![保存 RAID 5 配置](https://img.linux.net.cn/data/attachment/album/201508/27/130927bjz2ha7f27fmxu5y.png)

*保存 RAID 5 配置*

注意：保存配置将保持 md0 设备的 RAID 级别稳定不变。

#### 第6步：添加备用磁盘

18、 备用磁盘有什么用？它是非常有用的，如果我们有一个备用磁盘，当我们阵列中的任何一个磁盘发生故障后，这个备用磁盘会进入激活重建过程，并从其他磁盘上同步数据，这样就有了冗余。

更多关于添加备用磁盘和检查 RAID 5 容错的指令，请阅读下面文章中的第6步和第7步。

- [在 RAID 5 中添加备用磁盘](http://www.tecmint.com/create-raid-6-in-linux/)

#### 结论

在这篇文章中，我们已经看到了如何使用三个磁盘配置一个 RAID 5 。在接下来的文章中，我们将看到如何故障排除并且当 RAID 5 中的一个磁盘损坏后如何恢复。











### 在 Linux 下使用 RAID（五）：安装 RAID 6（条带化双分布式奇偶校验）

作者： [Babin Lonston](http://www.tecmint.com/create-raid-6-in-linux/) 译者： [LCTT](https://linux.cn/lctt/) [struggling](https://linux.cn/lctt/strugglingyouth) | 2015-08-31 15:50  评论: [*1*](https://linux.cn/portal.php?mod=comment&id=6121&idtype=aid) 收藏: *9*  

RAID 6 是 RAID 5 的升级版，它有两个分布式奇偶校验，即使两个磁盘发生故障后依然有容错能力。在两个磁盘同时发生故障时，系统的关键任务仍然能运行。它与 RAID 5 相似，但性能更健壮，因为它多用了一个磁盘来进行奇偶校验。

在之前的文章中，我们已经在 RAID 5 看了分布式奇偶校验，但在本文中，我们将看到的是 RAID 6 双分布式奇偶校验。不要期望比其他 RAID 有更好的性能，除非你也安装了一个专用的 RAID 控制器。在 RAID 6 中，即使我们失去了2个磁盘，我们仍可以通过更换磁盘，从校验中构建数据，然后取回数据。

![在 Linux 中安装 RAID 6](https://img.linux.net.cn/data/attachment/album/201508/31/155102zhhhwnlh2u6lhlnl.jpg)

*在 Linux 中安装 RAID 6*

要建立一个 RAID 6，一组最少需要4个磁盘。RAID 6 甚至在有些组中会有更多磁盘，这样将多个硬盘捆在一起，当读取数据时，它会同时从所有磁盘读取，所以读取速度会更快，当写数据时，因为它要将数据写在条带化的多个磁盘上，所以性能会较差。

现在，很多人都在讨论为什么我们需要使用 RAID 6，它的性能和其他 RAID 相比并不太好。提出这个问题首先需要知道的是，如果需要高容错性就选择 RAID 6。在每一个用于数据库的高可用性要求较高的环境中，他们需要 RAID 6 因为数据库是最重要，无论花费多少都需要保护其安全，它在视频流环境中也是非常有用的。

##### RAID 6 的的优点和缺点

- 性能不错。
- RAID 6 比较昂贵，因为它要求两个独立的磁盘用于奇偶校验功能。
- 将失去两个磁盘的容量来保存奇偶校验信息（双奇偶校验）。
- 即使两个磁盘损坏，数据也不会丢失。我们可以在更换损坏的磁盘后从校验中重建数据。
- 读性能比 RAID 5 更好，因为它从多个磁盘读取，但对于没有专用的 RAID 控制器的设备写性能将非常差。

##### 要求

要创建一个 RAID 6 最少需要4个磁盘。你也可以添加更多的磁盘，但你必须有专用的 RAID 控制器。使用软件 RAID 我们在 RAID 6 中不会得到更好的性能，所以我们需要一个物理 RAID 控制器。

如果你新接触 RAID 设置，我们建议先看完以下 RAID 文章。

- [介绍 RAID 的级别和概念](https://linux.cn/article-6085-1.html)
- [使用 mdadm 工具创建软件 RAID 0 （条带化）](https://linux.cn/article-6087-1.html)
- [用两块磁盘创建 RAID 1（镜像）](https://linux.cn/article-6093-1.html)
- [创建 RAID 5（条带化与分布式奇偶校验）](https://linux.cn/article-6102-1.html)

##### 我的服务器设置

```
操作系统 :  CentOS 6.5 FinalIP 地址    :  192.168.0.228主机名    :  rd6.tecmintlocal.com磁盘 1 [20GB]  :  /dev/sdb磁盘 2 [20GB]  :  /dev/sdc磁盘 3 [20GB]  :  /dev/sdd磁盘 4 [20GB]  :  /dev/sde
```

这是9篇系列教程的第5部分，在这里我们将看到如何在 Linux 系统或者服务器上使用四个 20GB 的磁盘（名为 /dev/sdb、 /dev/sdc、 /dev/sdd 和 /dev/sde）创建和设置软件 RAID 6 （条带化双分布式奇偶校验）。

#### 第1步：安装 mdadm 工具，并检查磁盘

1、 如果你按照我们最进的两篇 RAID 文章（第2篇和第3篇），我们已经展示了如何安装`mdadm`工具。如果你直接看的这篇文章，我们先来解释下在 Linux 系统中如何使用`mdadm`工具来创建和管理 RAID，首先根据你的 Linux 发行版使用以下命令来安装。

```
### yum install mdadm     [在 RedHat 系统]### apt-get install mdadm     [在 Debain 系统]
```

2、 安装该工具后，然后来验证所需的四个磁盘，我们将会使用下面的`fdisk`命令来检查用于创建 RAID 的磁盘。

```
### fdisk -l | grep sd
```

![在 Linux 中检查磁盘](https://img.linux.net.cn/data/attachment/album/201508/31/155104nggs3s38fbqufq6o.png)

*在 Linux 中检查磁盘*

3、 在创建 RAID 磁盘前，先检查下我们的磁盘是否创建过 RAID 分区。

```
### mdadm -E /dev/sd[b-e]### mdadm --examine /dev/sdb /dev/sdc /dev/sdd /dev/sde ### 或
```

![在磁盘上检查 RAID 分区](https://img.linux.net.cn/data/attachment/album/201508/31/155109xail6i1omli2211b.png)

*在磁盘上检查 RAID 分区*

**注意**: 在上面的图片中，没有检测到任何 super-block 或者说在四个磁盘上没有 RAID 存在。现在我们开始创建 RAID 6。

#### 第2步：为 RAID 6 创建磁盘分区

4、 现在在 `/dev/sdb`, `/dev/sdc`, `/dev/sdd` 和 `/dev/sde`上为 RAID 创建分区，使用下面的 fdisk 命令。在这里，我们将展示如何在 sdb 磁盘创建分区，同样的步骤也适用于其他分区。

**创建 /dev/sdb 分区**

```
### fdisk /dev/sdb
```

请按照说明进行操作，如下图所示创建分区。

- 按 `n`创建新的分区。
- 然后按 `P` 选择主分区。
- 接下来选择分区号为1。
- 只需按两次回车键选择默认值即可。
- 然后，按 `P` 来打印创建好的分区。
- 按 `L`，列出所有可用的类型。
- 按 `t` 去修改分区。
- 键入 `fd` 设置为 Linux 的 RAID 类型，然后按回车确认。
- 然后再次使用`p`查看我们所做的更改。
- 使用`w`保存更改。

![创建 /dev/sdb 分区](https://img.linux.net.cn/data/attachment/album/201508/31/155113dpzpm7seeevheu2m.png)

*创建 /dev/sdb 分区*

**创建 /dev/sdc 分区**

```
### fdisk /dev/sdc
```

![创建 /dev/sdc 分区](https://img.linux.net.cn/data/attachment/album/201508/31/155118a9p104t94tgdvq09.png)

*创建 /dev/sdc 分区*

**创建 /dev/sdd 分区**

```
### fdisk /dev/sdd
```

![创建 /dev/sdd 分区](https://img.linux.net.cn/data/attachment/album/201508/31/155121d0wawwy0xbw0jz45.png)

*创建 /dev/sdd 分区*

**创建 /dev/sde 分区**

```
### fdisk /dev/sde
```

![创建 /dev/sde 分区](https://img.linux.net.cn/data/attachment/album/201508/31/155125ne7ub73ycb233lij.png)

*创建 /dev/sde 分区*

5、 创建好分区后，检查磁盘的 super-blocks 是个好的习惯。如果 super-blocks 不存在我们可以按前面的创建一个新的 RAID。

```
### mdadm -E /dev/sd[b-e]1    ### mdadm --examine /dev/sdb1 /dev/sdc1 /dev/sdd1 /dev/sde1 ### 或
```

![Check Raid on New Partitions](https://img.linux.net.cn/data/attachment/album/201508/31/155126mysvdaqmysdsqda1.png)

*Check Raid on New Partitions*

*在新分区中检查 RAID *

#### 第3步：创建 md 设备（RAID）

6、 现在可以使用以下命令创建 RAID 设备`md0` （即 /dev/md0），并在所有新创建的分区中应用 RAID 级别，然后确认 RAID 设置。

```
### mdadm --create /dev/md0 --level=6 --raid-devices=4 /dev/sdb1 /dev/sdc1 /dev/sdd1 /dev/sde1### cat /proc/mdstat
```

![创建 Raid 6 设备](https://img.linux.net.cn/data/attachment/album/201508/31/155128h94u4tx9vxywvtxh.png)

*创建 Raid 6 设备*

7、 你还可以使用 watch 命令来查看当前创建 RAID 的进程，如下图所示。

```
### watch -n1 cat /proc/mdstat
```

![检查 RAID 6 创建过程](https://img.linux.net.cn/data/attachment/album/201508/31/155128un714551q7nqquw4.png)

*检查 RAID 6 创建过程*

8、 使用以下命令验证 RAID 设备。

```
### mdadm -E /dev/sd[b-e]1
```

**注意**::上述命令将显示四个磁盘的信息，这是相当长的，所以没有截取其完整的输出。

9、 接下来，验证 RAID 阵列，以确认重新同步过程已经开始。

```
### mdadm --detail /dev/md0
```

![检查 Raid 6 阵列](https://img.linux.net.cn/data/attachment/album/201508/31/155131pb51cm5bcrz25er5.png)

*检查 Raid 6 阵列*

#### 第4步：在 RAID 设备上创建文件系统

10、 使用 ext4 为`/dev/md0`创建一个文件系统，并将它挂载在 /mnt/raid6 。这里我们使用的是 ext4，但你可以根据你的选择使用任意类型的文件系统。

```
### mkfs.ext4 /dev/md0
```

![在 RAID 6 上创建文件系统](https://img.linux.net.cn/data/attachment/album/201508/31/155134h5co65n656433cmn.png)

*在 RAID 6 上创建文件系统*

11、 将创建的文件系统挂载到 /mnt/raid6，并验证挂载点下的文件，我们可以看到 lost+found 目录。

```
### mkdir /mnt/raid6### mount /dev/md0 /mnt/raid6/### ls -l /mnt/raid6/
```

12、 在挂载点下创建一些文件，在任意文件中添加一些文字并验证其内容。

```
### touch /mnt/raid6/raid6_test.txt### ls -l /mnt/raid6/### echo "tecmint raid setups" > /mnt/raid6/raid6_test.txt### cat /mnt/raid6/raid6_test.txt
```

![验证 RAID 内容](https://img.linux.net.cn/data/attachment/album/201508/31/155136m5019d20c0b5f9wh.png)

*验证 RAID 内容*

13、 在 /etc/fstab 中添加以下条目使系统启动时自动挂载设备，操作系统环境不同挂载点可能会有所不同。

```
### vim /etc/fstab/dev/md0                /mnt/raid6              ext4    defaults        0 0
```

![自动挂载 RAID 6 设备](https://img.linux.net.cn/data/attachment/album/201508/31/155138wcfizczrk7f7pi2o.png)

*自动挂载 RAID 6 设备*

14、 接下来，执行`mount -a`命令来验证 fstab 中的条目是否有错误。

```
### mount -av
```

![验证 RAID 是否自动挂载](https://img.linux.net.cn/data/attachment/album/201508/31/155139s0y4virc9k0w6cwc.png)

*验证 RAID 是否自动挂载*

#### 第5步：保存 RAID 6 的配置

15、 请注意，默认情况下 RAID 没有配置文件。我们需要使用以下命令手动保存它，然后检查设备`/dev/md0`的状态。

```
### mdadm --detail --scan --verbose >> /etc/mdadm.conf### cat /etc/mdadm.conf### mdadm --detail /dev/md0
```

![保存 RAID 6 配置](https://img.linux.net.cn/data/attachment/album/201508/31/155142fxwvu134f84ghv4f.png)

*保存 RAID 6 配置*

![检查 RAID 6 状态](https://img.linux.net.cn/data/attachment/album/201508/31/155142fxwvu134f84ghv4f.png)

*检查 RAID 6 状态*

#### 第6步：添加备用磁盘

16、 现在，已经使用了4个磁盘，并且其中两个作为奇偶校验信息来使用。在某些情况下，如果任意一个磁盘出现故障，我们仍可以得到数据，因为在 RAID 6 使用双奇偶校验。

如果第二个磁盘也出现故障，在第三块磁盘损坏前我们可以添加一个新的。可以在创建 RAID 集时加入一个备用磁盘，但我在创建 RAID 集合前没有定义备用的磁盘。不过，我们可以在磁盘损坏后或者创建 RAID 集合时添加一块备用磁盘。现在，我们已经创建好了 RAID，下面让我演示如何添加备用磁盘。

为了达到演示的目的，我已经热插入了一个新的 HDD 磁盘（即 /dev/sdf），让我们来验证接入的磁盘。

```
### ls -l /dev/ | grep sd
```

![检查新磁盘](https://img.linux.net.cn/data/attachment/album/201508/31/155145aiwjm64fhs6sedkh.png)

*检查新磁盘*

17、 现在再次确认新连接的磁盘没有配置过 RAID ，使用 mdadm 来检查。

```
### mdadm --examine /dev/sdf
```

![在新磁盘中检查 RAID](https://img.linux.net.cn/data/attachment/album/201508/31/155146uasasfvig88v8za6.png)

*在新磁盘中检查 RAID*

**注意**: 像往常一样，我们早前已经为四个磁盘创建了分区，同样，我们使用 fdisk 命令为新插入的磁盘创建新分区。

```
### fdisk /dev/sdf
```

![为 /dev/sdf 创建分区](https://img.linux.net.cn/data/attachment/album/201508/31/155151lr3zr33q0523u0x3.png)

*为 /dev/sdf 创建分区*

18、 在 /dev/sdf 创建新的分区后，在新分区上确认没有 RAID，然后将备用磁盘添加到 RAID 设备 /dev/md0 中，并验证添加的设备。

```
### mdadm --examine /dev/sdf### mdadm --examine /dev/sdf1### mdadm --add /dev/md0 /dev/sdf1### mdadm --detail /dev/md0
```

![在 sdf 分区上验证 Raid](https://img.linux.net.cn/data/attachment/album/201508/31/155152ukhd5zck5h1mubmc.png)

*在 sdf 分区上验证 Raid*

![Add sdf Partition to Raid](https://img.linux.net.cn/data/attachment/album/201508/31/155153vzjnm6keptpljlee.png)

*Add sdf Partition to Raid*

*添加 sdf 分区到 RAID *

![验证 sdf 分区信息](https://img.linux.net.cn/data/attachment/album/201508/31/155155w14aezgsphje4hc9.png)

*验证 sdf 分区信息*

#### 第7步：检查 RAID 6 容错

19、 现在，让我们检查备用驱动器是否能自动工作，当我们阵列中的任何一个磁盘出现故障时。为了测试，我将一个磁盘手工标记为故障设备。

在这里，我们标记 /dev/sdd1 为故障磁盘。

```
### mdadm --manage --fail /dev/md0 /dev/sdd1
```

![检查 RAID 6 容错](https://img.linux.net.cn/data/attachment/album/201508/31/155156ugt64vi3gaz3m98q.png)

*检查 RAID 6 容错*

20、 让我们查看 RAID 的详细信息，并检查备用磁盘是否开始同步。

```
### mdadm --detail /dev/md0
```

![检查 RAID 自动同步](https://img.linux.net.cn/data/attachment/album/201508/31/155202rh713mg01zrhhfhl.png)

*检查 RAID 自动同步*

**哇塞!** 这里，我们看到备用磁盘激活了，并开始重建进程。在底部，我们可以看到有故障的磁盘 /dev/sdd1 标记为 faulty。可以使用下面的命令查看进程重建。

```
### cat /proc/mdstat
```

![RAID 6 自动同步](https://img.linux.net.cn/data/attachment/album/201508/31/155204iikvi3req3aqpk2i.png)

*RAID 6 自动同步*

#### 结论:

在这里，我们看到了如何使用四个磁盘设置 RAID 6。这种 RAID 级别是具有高冗余的昂贵设置之一。在接下来的文章中，我们将看到如何建立一个嵌套的 RAID 10 甚至更多。请继续关注。









### 在 Linux 下使用 RAID（六）：设置 RAID 10 或 1 + 0（嵌套）

作者： [Babin Lonston](http://www.tecmint.com/create-raid-10-in-linux/) 译者： [LCTT](https://linux.cn/lctt/) [struggling](https://linux.cn/lctt/strugglingyouth) | 2015-09-01 08:51  评论: [*4*](https://linux.cn/portal.php?mod=comment&id=6122&idtype=aid) 收藏: *9*  

RAID 10 是组合 RAID 1 和 RAID 0 形成的。要设置 RAID 10，我们至少需要4个磁盘。在之前的文章中，我们已经看到了如何使用最少两个磁盘设置 RAID 1 和 RAID 0。

在这里，我们将使用最少4个磁盘组合 RAID 1 和 RAID 0 来设置 RAID 10。假设我们已经在用 RAID 10 创建的逻辑卷保存了一些数据。比如我们要保存数据 “TECMINT”，它将使用以下方法将其保存在4个磁盘中。

![在 Linux 中创建 Raid 10（LCTT 译注：原图有误，已修正）](https://img.linux.net.cn/data/attachment/album/201509/01/093619iqwblqd9od94goq3.jpg)

*在 Linux 中创建 Raid 10（LCTT 译注：原图有误，已修正）*

RAID 10 是先做镜像，再做条带。因此，在 RAID 1 中，相同的数据将被写入到两个磁盘中，“T”将同时被写入到第一和第二个磁盘中。接着的数据被条带化到另外两个磁盘，“E”将被同时写入到第三和第四个磁盘中。它将继续循环此过程，“C”将同时被写入到第一和第二个磁盘，以此类推。

（LCTT 译注：原文中此处描述混淆有误，已经根据实际情况进行修改。）

现在你已经了解 RAID 10 怎样组合 RAID 1 和 RAID 0 来工作的了。如果我们有4个20 GB 的磁盘，总共为 80 GB，但我们将只能得到40 GB 的容量，另一半的容量在构建 RAID 10 中丢失。

##### RAID 10 的优点和缺点

- 提供更好的性能。
- 在 RAID 10 中我们将失去一半的磁盘容量。
- 读与写的性能都很好，因为它会同时进行写入和读取。
- 它能解决数据库的高 I/O 磁盘写操作。

##### 要求

在 RAID 10 中，我们至少需要4个磁盘，前2个磁盘为 RAID 1，其他2个磁盘为 RAID 0，就像我之前说的，RAID 10 仅仅是组合了 RAID 0和1。如果我们需要扩展 RAID 组，最少需要添加4个磁盘。

**我的服务器设置**

```
操作系统 :  CentOS 6.5 FinalIP 地址       :   192.168.0.229主机名       :   rd10.tecmintlocal.com磁盘 1 [20GB]     :   /dev/sdd磁盘 2 [20GB]     :   /dev/sdc磁盘 3 [20GB]     :   /dev/sdd磁盘 4 [20GB]     :   /dev/sde
```

有两种方法来设置 RAID 10，在这里两种方法我都会演示，但我更喜欢第一种方法，使用它来设置 RAID 10 更简单。

#### 方法1：设置 RAID 10

1、 首先，使用以下命令确认所添加的4块磁盘没有被使用。

```
### ls -l /dev | grep sd
```

2、 四个磁盘被检测后，然后来检查磁盘是否存在 RAID 分区。

```
### mdadm -E /dev/sd[b-e]### mdadm --examine /dev/sdb /dev/sdc /dev/sdd /dev/sde ### 或
```

![验证添加的4块磁盘](https://img.linux.net.cn/data/attachment/album/201508/31/215613nikikwi6spexzw5o.png)

*验证添加的4块磁盘*

**注意**: 在上面的输出中，如果没有检测到 super-block 意味着在4块磁盘中没有定义过 RAID。

##### 第1步：为 RAID 分区

3、 现在，使用`fdisk`，命令为4个磁盘(/dev/sdb, /dev/sdc, /dev/sdd 和 /dev/sde)创建新分区。

```
### fdisk /dev/sdb### fdisk /dev/sdc### fdisk /dev/sdd### fdisk /dev/sde
```

###### 为 /dev/sdb 创建分区

我来告诉你如何使用 fdisk 为磁盘(/dev/sdb)进行分区，此步也适用于其他磁盘。

```
### fdisk /dev/sdb
```

请使用以下步骤为 /dev/sdb 创建一个新的分区。

- 按 `n` 创建新的分区。
- 然后按 `P` 选择主分区。
- 接下来选择分区号为1。
- 只需按两次回车键选择默认值即可。
- 然后，按 `P` 来打印创建好的分区。
- 按 `L`，列出所有可用的类型。
- 按 `t` 去修改分区。
- 键入 `fd` 设置为 Linux 的 RAID 类型，然后按 Enter 确认。
- 然后再次使用`p`查看我们所做的更改。
- 使用`w`保存更改。

![为磁盘 sdb 分区](https://img.linux.net.cn/data/attachment/album/201508/31/215615dt03b402t4n42c4h.png)

*为磁盘 sdb 分区*

**注意**: 请使用上面相同的指令对其他磁盘(sdc, sdd sdd sde)进行分区。

4、 创建好4个分区后，需要使用下面的命令来检查磁盘是否存在 raid。

```
### mdadm -E /dev/sd[b-e]### mdadm --examine /dev/sdb /dev/sdc /dev/sdd /dev/sde ### 或### mdadm -E /dev/sd[b-e]1### mdadm --examine /dev/sdb1 /dev/sdc1 /dev/sdd1 /dev/sde1 ### 或
```

![检查磁盘](https://img.linux.net.cn/data/attachment/album/201508/31/215616vp4p39dip8xkkuck.png)

*检查磁盘*

**注意**: 以上输出显示，新创建的四个分区中没有检测到 super-block，这意味着我们可以继续在这些磁盘上创建 RAID 10。

##### 第2步: 创建 RAID 设备 `md`

5、 现在该创建一个`md`（即 /dev/md0）设备了，使用“mdadm” raid 管理工具。在创建设备之前，必须确保系统已经安装了`mdadm`工具，如果没有请使用下面的命令来安装。

```
### yum install mdadm     [在 RedHat 系统]### apt-get install mdadm     [在 Debain 系统]
```

`mdadm`工具安装完成后，可以使用下面的命令创建一个`md` raid 设备。

```
### mdadm --create /dev/md0 --level=10 --raid-devices=4 /dev/sd[b-e]1
```

6、 接下来使用`cat`命令验证新创建的 raid 设备。

```
### cat /proc/mdstat
```

![创建 md RAID 设备](https://img.linux.net.cn/data/attachment/album/201508/31/215616anax4n70g6280iab.png)

*创建 md RAID 设备*

7、 接下来，使用下面的命令来检查4个磁盘。下面命令的输出会很长，因为它会显示4个磁盘的所有信息。

```
### mdadm --examine /dev/sd[b-e]1
```

8、 接下来，使用以下命令来查看 RAID 阵列的详细信息。

```
### mdadm --detail /dev/md0
```

![查看 RAID 阵列详细信息](https://img.linux.net.cn/data/attachment/album/201508/31/215618nk61ijk9yfa9z9oo.png)

*查看 RAID 阵列详细信息*

**注意**: 你在上面看到的结果，该 RAID 的状态是 active 和re-syncing。

##### 第3步：创建文件系统

9、 使用 ext4 作为`md0′的文件系统，并将它挂载到`/mnt/raid10`下。在这里，我用的是 ext4，你可以使用你想要的文件系统类型。

```
### mkfs.ext4 /dev/md0
```

![创建 md 文件系统](https://img.linux.net.cn/data/attachment/album/201508/31/215620liiziljkf9idbzje.png)

*创建 md 文件系统*

10、 在创建文件系统后，挂载文件系统到`/mnt/raid10`下，并使用`ls -l`命令列出挂载点下的内容。

```
### mkdir /mnt/raid10### mount /dev/md0 /mnt/raid10/### ls -l /mnt/raid10/
```

接下来，在挂载点下创建一些文件，并在文件中添加些内容，然后检查内容。

```
### touch /mnt/raid10/raid10_files.txt### ls -l /mnt/raid10/### echo "raid 10 setup with 4 disks" > /mnt/raid10/raid10_files.txt### cat /mnt/raid10/raid10_files.txt
```

![挂载 md 设备](https://img.linux.net.cn/data/attachment/album/201508/31/215620orf26qogf6q0s5vv.png)

*挂载 md 设备*

11、 要想自动挂载，打开`/etc/fstab`文件并添加下面的条目，挂载点根据你环境的不同来添加。使用 wq! 保存并退出。

```
### vim /etc/fstab/dev/md0                /mnt/raid10              ext4    defaults        0 0
```

![挂载 md 设备](https://img.linux.net.cn/data/attachment/album/201508/31/215621tr1yeq3qug6q74xn.png)

*挂载 md 设备*

12、 接下来，在重新启动系统前使用`mount -a`来确认`/etc/fstab`文件是否有错误。

```
### mount -av
```

![检查 Fstab 中的错误](https://img.linux.net.cn/data/attachment/album/201508/31/215622c60crrzbg101lfj0.png)

*检查 Fstab 中的错误*

##### 第四步：保存 RAID 配置

13、 默认情况下 RAID 没有配置文件，所以我们需要在上述步骤完成后手动保存它。

```
### mdadm --detail --scan --verbose >> /etc/mdadm.conf
```

![保存 RAID10 的配置](https://img.linux.net.cn/data/attachment/album/201508/31/215622dsp01cftzpef1977.png)

*保存 RAID10 的配置*

就这样，我们使用方法1创建完了 RAID 10，这种方法是比较容易的。现在，让我们使用方法2来设置 RAID 10。

#### 方法2：创建 RAID 10

1、 在方法2中，我们必须定义2组 RAID 1，然后我们需要使用这些创建好的 RAID 1 的集合来定义一个 RAID 0。在这里，我们将要做的是先创建2个镜像（RAID1），然后创建 RAID0 （条带化）。

首先，列出所有的可用于创建 RAID 10 的磁盘。

```
### ls -l /dev | grep sd
```

![列出了 4 个设备](https://img.linux.net.cn/data/attachment/album/201508/31/215623ul91kzh9kpp1kvww.png)

*列出了 4 个设备*

2、 将4个磁盘使用`fdisk`命令进行分区。对于如何分区，您可以按照上面的第1步。

```
### fdisk /dev/sdb### fdisk /dev/sdc### fdisk /dev/sdd### fdisk /dev/sde
```

3、 在完成4个磁盘的分区后，现在检查磁盘是否存在 RAID块。

```
### mdadm --examine /dev/sd[b-e]### mdadm --examine /dev/sd[b-e]1
```

![检查 4 个磁盘](https://img.linux.net.cn/data/attachment/album/201508/31/215624sf3cgo65cn2on2nv.png)

*检查 4 个磁盘*

##### 第1步：创建 RAID 1

4、 首先，使用4块磁盘创建2组 RAID 1，一组为`sdb1′和`sdc1′，另一组是`sdd1′ 和`sde1′。

```
### mdadm --create /dev/md1 --metadata=1.2 --level=1 --raid-devices=2 /dev/sd[b-c]1### mdadm --create /dev/md2 --metadata=1.2 --level=1 --raid-devices=2 /dev/sd[d-e]1### cat /proc/mdstat
```

![创建 RAID 1](https://img.linux.net.cn/data/attachment/album/201508/31/215625yecy1bc1i6pv6818.png)

*创建 RAID 1*

![查看 RAID 1 的详细信息](https://img.linux.net.cn/data/attachment/album/201508/31/215625yecy1bc1i6pv6818.png)

*查看 RAID 1 的详细信息*

##### 第2步：创建 RAID 0

5、 接下来，使用 md1 和 md2 来创建 RAID 0。

```
### mdadm --create /dev/md0 --level=0 --raid-devices=2 /dev/md1 /dev/md2### cat /proc/mdstat
```

![创建 RAID 0](https://img.linux.net.cn/data/attachment/album/201508/31/215626epch71ryvqr7hj6c.png)

*创建 RAID 0*

##### 第3步：保存 RAID 配置

6、 我们需要将配置文件保存在`/etc/mdadm.conf`文件中，使其每次重新启动后都能加载所有的 RAID 设备。

```
### mdadm --detail --scan --verbose >> /etc/mdadm.conf
```

在此之后，我们需要按照方法1中的第3步来创建文件系统。

就是这样！我们采用的方法2创建完了 RAID 1+0。我们将会失去一半的磁盘空间，但相比其他 RAID ，它的性能将是非常好的。

#### 结论

在这里，我们采用两种方法创建 RAID 10。RAID 10 具有良好的性能和冗余性。希望这篇文章可以帮助你了解 RAID 10 嵌套 RAID。在后面的文章中我们会看到如何扩展现有的 RAID 阵列以及更多精彩的内容。













### 在 Linux 下使用 RAID（七）：在 RAID 中扩展现有的 RAID 阵列和删除故障的磁盘

作者： [Babin Lonston](http://www.tecmint.com/grow-raid-array-in-linux/) 译者： [LCTT](https://linux.cn/lctt/) [struggling](https://linux.cn/lctt/strugglingyouth) | 2015-09-02 09:25  评论: [*6*](https://linux.cn/portal.php?mod=comment&id=6123&idtype=aid) 收藏: *6*  

每个新手都会对阵列（array）这个词所代表的意思产生疑惑。阵列只是磁盘的一个集合。换句话说，我们可以称阵列为一个集合（set）或一组（group）。就像一组鸡蛋中包含6个一样。同样 RAID 阵列中包含着多个磁盘，可能是2，4，6，8，12，16等，希望你现在知道了什么是阵列。

在这里，我们将看到如何扩展现有的阵列或 RAID 组。例如，如果我们在阵列中使用2个磁盘形成一个 raid 1 集合，在某些情况，如果该组中需要更多的空间，就可以使用 mdadm -grow 命令来扩展阵列大小，只需要将一个磁盘加入到现有的阵列中即可。在说完扩展（添加磁盘到现有的阵列中）后，我们将看看如何从阵列中删除故障的磁盘。

![扩展 RAID 阵列和删除故障的磁盘](https://img.linux.net.cn/data/attachment/album/201508/31/222753ilrflallzk1khmrr.jpg)

*扩展 RAID 阵列和删除故障的磁盘*

假设磁盘中的一个有问题了需要删除该磁盘，但我们需要在删除磁盘前添加一个备用磁盘来扩展该镜像，因为我们需要保存我们的数据。当磁盘发生故障时我们需要从阵列中删除它，这是这个主题中我们将要学习到的。

##### 扩展 RAID 的特性

- 我们可以增加（扩展）任意 RAID 集合的大小。
- 我们可以在使用新磁盘扩展 RAID 阵列后删除故障的磁盘。
- 我们可以扩展 RAID 阵列而无需停机。

##### 要求

- 为了扩展一个RAID阵列，我们需要一个已有的 RAID 组（阵列）。
- 我们需要额外的磁盘来扩展阵列。
- 在这里，我们使用一块磁盘来扩展现有的阵列。

在我们了解扩展和恢复阵列前，我们必须了解有关 RAID 级别和设置的基本知识。点击下面的链接了解这些。

- [介绍 RAID 的级别和概念](https://linux.cn/article-6085-1.html)
- [使用 mdadm 工具创建软件 RAID 0 （条带化）](https://linux.cn/article-6087-1.html)

##### 我的服务器设置

```
操作系统    :   CentOS 6.5 FinalIP地址      :   192.168.0.230主机名     :   grow.tecmintlocal.com2 块现有磁盘   :   1 GB1 块额外磁盘   :   1 GB
```

在这里，我们已有一个 RAID ，有2块磁盘，每个大小为1GB，我们现在再增加一个磁盘到我们现有的 RAID 阵列中，其大小为1GB。

#### 扩展现有的 RAID 阵列

1、 在扩展阵列前，首先使用下面的命令列出现有的 RAID 阵列。

```
### mdadm --detail /dev/md0
```

![检查现有的 RAID 阵列](https://img.linux.net.cn/data/attachment/album/201508/31/222755j444r3ur5u6wee8f.png)

*检查现有的 RAID 阵列*

**注意**: 以上输出显示，已经有了两个磁盘在 RAID 阵列中，级别为 RAID 1。现在我们增加一个磁盘到现有的阵列里。

2、 现在让我们添加新的磁盘“sdd”，并使用`fdisk`命令来创建分区。

```
### fdisk /dev/sdd
```

请使用以下步骤为 /dev/sdd 创建一个新的分区。

- 按 `n` 创建新的分区。
- 然后按 `P` 选择主分区。
- 接下来选择分区号为1。
- 只需按两次回车键选择默认值即可。
- 然后，按 `P` 来打印创建好的分区。
- 按 `L`，列出所有可用的类型。
- 按 `t` 去修改分区。
- 键入 `fd` 设置为 Linux 的 RAID 类型，然后按回车确认。
- 然后再次使用`p`查看我们所做的更改。
- 使用`w`保存更改。

![为 sdd 创建新的分区](https://img.linux.net.cn/data/attachment/album/201508/31/222757jdbq3aoxzeeodcad.png)

*为 sdd 创建新的分区*

3、 一旦新的 sdd 分区创建完成后，你可以使用下面的命令验证它。

```
### ls -l /dev/ | grep sd
```

![确认 sdd 分区](https://img.linux.net.cn/data/attachment/album/201508/31/222800j5qwydcv5qvpqkpv.png)

*确认 sdd 分区*

4、 接下来，在添加到阵列前先检查磁盘是否有 RAID 分区。

```
### mdadm --examine /dev/sdd1
```

![在 sdd 分区中检查 RAID](https://img.linux.net.cn/data/attachment/album/201508/31/222800t57ygvagdu1cnl1y.png)

*在 sdd 分区中检查 RAID*

**注意**:以上输出显示，该盘有没有发现 super-blocks，意味着我们可以将新的磁盘添加到现有阵列。

5、 要添加新的分区 /dev/sdd1 到现有的阵列 md0，请使用以下命令。

```
### mdadm --manage /dev/md0 --add /dev/sdd1
```

![添加磁盘到 RAID 阵列](https://img.linux.net.cn/data/attachment/album/201508/31/222801x2igbt646eijgzh2.png)

*添加磁盘到 RAID 阵列*

6、 一旦新的磁盘被添加后，在我们的阵列中检查新添加的磁盘。

```
### mdadm --detail /dev/md0
```

![确认将新磁盘添加到 RAID 中](https://img.linux.net.cn/data/attachment/album/201508/31/222803kw7hhfc5r7g1833r.png)

*确认将新磁盘添加到 RAID 中*

**注意**: 在上面的输出，你可以看到磁盘已经被添加作为备用的。在这里，我们的阵列中已经有了2个磁盘，但我们期待阵列中有3个磁盘，因此我们需要扩展阵列。

7、 要扩展阵列，我们需要使用下面的命令。

```
### mdadm --grow --raid-devices=3 /dev/md0
```

![扩展 Raid 阵列](https://img.linux.net.cn/data/attachment/album/201508/31/222805p9z626ig912i211i.png)

*扩展 Raid 阵列*

现在我们可以看到第三块磁盘(sdd1)已被添加到阵列中，在第三块磁盘被添加后，它将从另外两块磁盘上同步数据。

```
### mdadm --detail /dev/md0
```

![确认 Raid 阵列](https://img.linux.net.cn/data/attachment/album/201508/31/222808e9er2ed2j2a39wa7.png)

*确认 Raid 阵列*

**注意**: 对于大容量磁盘会需要几个小时来同步数据。在这里，我们使用的是1GB的虚拟磁盘，所以它非常快在几秒钟内便会完成。

#### 从阵列中删除磁盘

8、 在数据被从其他两个磁盘同步到新磁盘`sdd1`后，现在三个磁盘中的数据已经相同了（镜像）。

正如我前面所说的，假定一个磁盘出问题了需要被删除。所以，现在假设磁盘`sdc1`出问题了，需要从现有阵列中删除。

在删除磁盘前我们要将其标记为失效，然后我们才可以将其删除。

```
### mdadm --fail /dev/md0 /dev/sdc1### mdadm --detail /dev/md0
```

![在 RAID 阵列中模拟磁盘故障](https://img.linux.net.cn/data/attachment/album/201508/31/222811wrs1rk84xkzt5r4k.png)

*在 RAID 阵列中模拟磁盘故障*

从上面的输出中，我们清楚地看到，磁盘在下面被标记为 faulty。即使它是 faulty 的，我们仍然可以看到 raid 设备有3个，1个损坏了，状态是 degraded。

现在我们要从阵列中删除 faulty 的磁盘，raid 设备将像之前一样继续有2个设备。

```
### mdadm --remove /dev/md0 /dev/sdc1
```

![在 Raid 阵列中删除磁盘](https://img.linux.net.cn/data/attachment/album/201508/31/222812skwrbkvu1yvk9pyy.png)

*在 Raid 阵列中删除磁盘*

9、 一旦故障的磁盘被删除，然后我们只能使用2个磁盘来扩展 raid 阵列了。

```
### mdadm --grow --raid-devices=2 /dev/md0### mdadm --detail /dev/md0
```

![在 RAID 阵列扩展磁盘](https://img.linux.net.cn/data/attachment/album/201508/31/222814sxz2vrlxu1pwxusu.png)

*在 RAID 阵列扩展磁盘*

从上面的输出中可以看到，我们的阵列中仅有2台设备。如果你需要再次扩展阵列，按照如上所述的同样步骤进行。如果你需要添加一个磁盘作为备用，将其标记为 spare，因此，如果磁盘出现故障时，它会自动顶上去并重建数据。

#### 结论

在这篇文章中，我们已经看到了如何扩展现有的 RAID 集合，以及如何在重新同步已有磁盘的数据后从一个阵列中删除故障磁盘。所有这些步骤都可以不用停机来完成。在数据同步期间，系统用户，文件和应用程序不会受到任何影响。

在接下来的文章我将告诉你如何管理 RAID，敬请关注更新，不要忘了写评论。











### 在 Linux 下使用 RAID（八）：当软件 RAID 故障时如何恢复和重建数据

作者： [Gabriel Cánepa](http://www.tecmint.com/recover-data-and-rebuild-failed-software-raid/) 译者： [LCTT](https://linux.cn/lctt/) [struggling](https://linux.cn/lctt/strugglingyouth) | 2015-10-22 08:03  评论: [*1*](https://linux.cn/portal.php?mod=comment&id=6448&idtype=aid) 收藏: *2*  

在阅读过 [RAID 系列](https://linux.cn/article-6085-1.html) 前面的文章后你已经对 RAID 比较熟悉了。回顾前面几个软件 RAID 的配置，我们对每一个都做了详细的解释，使用哪一个取决与你的具体情况。

![恢复并重建故障的软件 RAID - 第8部分](https://img.linux.net.cn/data/attachment/album/201510/21/220530txqez0qxqzv3iqpe.png)

*恢复并重建故障的软件 RAID - 第8部分*

在本文中，我们将讨论当一个磁盘发生故障时如何重建软件 RAID 阵列并且不会丢失数据。为方便起见，我们仅考虑RAID 1 的配置 - 但其方法和概念适用于所有情况。

##### RAID 测试方案

在进一步讨论之前，请确保你已经配置好了 RAID 1 阵列，可以按照本系列第3部分提供的方法：[在 Linux 中如何创建 RAID 1（镜像）](https://linux.cn/article-6093-1.html)。

在目前的情况下，仅有的变化是：

1. 使用不同版本 CentOS（v7），而不是前面文章中的（v6.5）。
2. 磁盘容量发生改变， /dev/sdb 和 /dev/sdc（各8GB）。

此外，如果 SELinux 设置为 enforcing 模式，你需要将相应的标签添加到挂载 RAID 设备的目录中。否则，当你试图挂载时，你会碰到这样的警告信息：

![启用 SELinux 时 RAID 挂载错误](https://img.linux.net.cn/data/attachment/album/201510/21/220530i228220gdy5zpj7v.png)

*启用 SELinux 时 RAID 挂载错误*

通过以下命令来解决:

```
### restorecon -R /mnt/raid1
```

#### 配置 RAID 监控

存储设备损坏的原因很多（尽管固态硬盘大大减少了这种情况发生的可能性），但不管是什么原因，可以肯定问题随时可能发生，你需要准备好替换发生故障的部分，并确保数据的可用性和完整性。

首先建议是。虽然你可以查看 `/proc/mdstat` 来检查 RAID 的状态，但有一个更好的和节省时间的方法，使用监控 + 扫描模式运行 mdadm，它将警报通过电子邮件发送到一个预定义的收件人。

要这样设置，在 `/etc/mdadm.conf` 添加以下行：

```
MAILADDR user@<domain or localhost>
```

我自己的设置如下：

```
MAILADDR gacanepa@localhost
```

![监控 RAID 并使用电子邮件进行报警](https://img.linux.net.cn/data/attachment/album/201510/21/220531o48bcu84uussjoow.png)

*监控 RAID 并使用电子邮件进行报警*

要让 mdadm 运行在监控 + 扫描模式中，以 root 用户添加以下 crontab 条目：

```
@reboot /sbin/mdadm --monitor --scan --oneshot
```

默认情况下，mdadm 每隔60秒会检查 RAID 阵列，如果发现问题将发出警报。你可以通过添加 `--delay` 选项到crontab 条目上面，后面跟上秒数，来修改默认行为（例如，`--delay` 1800意味着30分钟）。

最后，确保你已经安装了一个邮件用户代理（MUA），如[mutt 或 mailx](http://www.tecmint.com/send-mail-from-command-line-using-mutt-command/)。否则，你将不会收到任何警报。

在一分钟内，我们就会看到 mdadm 发送的警报。

#### 模拟和更换发生故障的 RAID 存储设备

为了给 RAID 阵列中的存储设备模拟一个故障，我们将使用 `--manage` 和 `--set-faulty` 选项，如下所示：

```
### mdadm --manage --set-faulty /dev/md0 /dev/sdc1  
```

这将导致 /dev/sdc1 被标记为 faulty，我们可以在 /proc/mdstat 看到：

![在 RAID 存储设备上模拟问题](https://img.linux.net.cn/data/attachment/album/201510/21/220532wgrcgnf4bontrgcj.png)

*在 RAID 存储设备上模拟问题*

更重要的是，让我们看看是不是收到了同样的警报邮件：

![RAID 设备故障时发送邮件警报](https://img.linux.net.cn/data/attachment/album/201510/21/220539bq20doix82juz702.png)

*RAID 设备故障时发送邮件警报*

在这种情况下，你需要从软件 RAID 阵列中删除该设备：

```
### mdadm /dev/md0 --remove /dev/sdc1
```

然后，你可以直接从机器中取出，并将其使用备用设备来取代（/dev/sdd 中类型为 fd 的分区是以前创建的）：

```
### mdadm --manage /dev/md0 --add /dev/sdd1
```

幸运的是，该系统会使用我们刚才添加的磁盘自动重建阵列。我们可以通过标记 /dev/sdb1 为 faulty 来进行测试，从阵列中取出后，并确认 tecmint.txt 文件仍然在 /mnt/raid1 是可访问的：

```
### mdadm --detail /dev/md0### mount | grep raid1### ls -l /mnt/raid1 | grep tecmint### cat /mnt/raid1/tecmint.txt
```

![确认 RAID 重建](https://img.linux.net.cn/data/attachment/album/201510/21/220544z2caprz2rshh8apm.png)

*确认 RAID 重建*

上面图片清楚的显示，添加 /dev/sdd1 到阵列中来替代 /dev/sdc1，数据的重建是系统自动完成的，不需要干预。

虽然要求不是很严格，有一个备用设备是个好主意，这样更换故障的设备就可以在瞬间完成了。要做到这一点，先让我们重新添加 /dev/sdb1 和 /dev/sdc1：

```
### mdadm --manage /dev/md0 --add /dev/sdb1### mdadm --manage /dev/md0 --add /dev/sdc1
```

![取代故障的 Raid 设备](https://img.linux.net.cn/data/attachment/album/201510/21/220550c1ttlm6xe9e8tzj2.png)

*取代故障的 Raid 设备*

#### 从冗余丢失中恢复数据

如前所述，当一个磁盘发生故障时， mdadm 将自动重建数据。但是，如果阵列中的2个磁盘都故障时会发生什么？让我们来模拟这种情况，通过标记 /dev/sdb1 和 /dev/sdd1 为 faulty：

```
### umount /mnt/raid1### mdadm --manage --set-faulty /dev/md0 /dev/sdb1### mdadm --stop /dev/md0### mdadm --manage --set-faulty /dev/md0 /dev/sdd1
```

此时尝试以同样的方式重新创建阵列就（或使用 `--assume-clean` 选项）可能会导致数据丢失，因此不到万不得已不要使用。

让我们试着从 /dev/sdb1 恢复数据，例如，在一个类似的磁盘分区（/dev/sde1 - 注意，这需要你执行前在/dev/sde 上创建一个 fd 类型的分区）上使用 `ddrescue`：

```
### ddrescue -r 2 /dev/sdb1 /dev/sde1
```

![恢复 Raid 阵列](https://img.linux.net.cn/data/attachment/album/201510/21/220553k26neoo162ewkuy1.png)

*恢复 Raid 阵列*

请注意，到现在为止，我们还没有触及 /dev/sdb 和 /dev/sdd，它们的分区是 RAID 阵列的一部分。

现在，让我们使用 /dev/sde1 和 /dev/sdf1 来重建阵列：

```
### mdadm --create /dev/md0 --level=mirror --raid-devices=2 /dev/sd[e-f]1
```

请注意，在真实的情况下，你需要使用与原来的阵列中相同的设备名称，即设备失效后替换的磁盘的名称应该是 /dev/sdb1 和 /dev/sdc1。

在本文中，我选择了使用额外的设备来重新创建全新的磁盘阵列，是为了避免与原来的故障磁盘混淆。

当被问及是否继续写入阵列时，键入 Y，然后按 Enter。阵列被启动，你也可以查看它的进展：

```
### watch -n 1 cat /proc/mdstat
```

当这个过程完成后，你就应该能够访问 RAID 的数据：

![确认 Raid 数据](https://img.linux.net.cn/data/attachment/album/201510/21/220556czeliti301lkb1ee.png)

*确认 Raid 数据*

#### 总结

在本文中，我们回顾了从 RAID 故障和冗余丢失中恢复数据。但是，你要记住，这种技术是一种存储解决方案，不能取代备份。

本文中介绍的方法适用于所有 RAID 中，其中的概念我将在本系列的最后一篇（RAID 管理）中涵盖它。

如果你对本文有任何疑问，随时给我们以评论的形式说明。我们期待倾听阁下的心声！









### 在 Linux 下使用 RAID（九）：如何使用 ‘Mdadm’ 工具管理软件 RAID

作者： [GABRIEL CÁNEPA](http://www.tecmint.com/manage-software-raid-devices-in-linux-with-mdadm/) 译者： [LCTT](https://linux.cn/lctt/) [struggling](https://linux.cn/lctt/strugglingyouth) | 2015-10-24 10:15  评论: [*3*](https://linux.cn/portal.php?mod=comment&id=6463&idtype=aid) 收藏: *7*  

无论你以前有没有使用 RAID 阵列的经验，以及是否完成了 [此 RAID 系列](https://linux.cn/article-6085-1.html) 的所有教程，一旦你在 Linux 中熟悉了 `mdadm --manage` 命令的使用，管理软件 RAID 将不是很复杂的任务。

![在 Linux 中使用 mdadm 管理 RAID 设备 - 第9部分](https://img.linux.net.cn/data/attachment/album/201510/25/201458vaugnvlr7gj5fa5v.png)

*在 Linux 中使用 mdadm 管理 RAID 设备 - 第9部分*

在本教程中，我们会再介绍此工具提供的功能，这样当你需要它，就可以派上用场。

##### RAID 测试方案

在本系列的最后一篇文章中，我们将使用一个简单的 RAID 1（镜像）阵列，它由两个 8GB 的磁盘（/dev/sdb 和 /dev/sdc）和一个备用设备（/dev/sdd）来演示，但在此使用的方法也适用于其他类型的配置。也就是说，放心去用吧，把这个页面添加到浏览器的书签，然后让我们开始吧。

#### 了解 mdadm 的选项和使用方法

幸运的是，mdadm 有一个内建的 `--help` 参数来对每个主要的选项提供说明文档。

因此，让我们开始输入：

```
### mdadm --manage --help
```

就会使我们看到 `mdadm --manage` 能够执行哪些任务：

![使用 mdadm 工具来管理 RAID](https://img.linux.net.cn/data/attachment/album/201510/23/231705xffac8m8a1wdwa9z.png)

*使用 mdadm 工具来管理 RAID*

正如我们在上面的图片看到，管理一个 RAID 阵列可以在任意时间执行以下任务：

- （重新）将设备添加到阵列中
- 把设备标记为故障
- 从阵列中删除故障设备
- 使用备用设备更换故障设备
- 先创建部分阵列
- 停止阵列
- 标记阵列为 ro（只读）或 rw（读写）

#### 使用 mdadm 工具管理 RAID 设备

需要注意的是，如果用户忽略 `--manage` 选项，mdadm 默认使用管理模式。请记住这一点，以避免出现最坏的情况。

上图中的高亮文本显示了管理 RAID 的基本语法：

```
### mdadm --manage RAID options devices
```

让我们来演示几个例子。

##### 例1：为 RAID 阵列添加设备

你通常会添加新设备来更换故障的设备，或者使用空闲的分区以便在出现故障时能及时替换：

```
### mdadm --manage /dev/md0 --add /dev/sdd1
```

![添加设备到 Raid 阵列](https://img.linux.net.cn/data/attachment/album/201510/23/231707tq4hp5elzgz5msoh.png)

*添加设备到 Raid 阵列*

##### 例2：把一个 RAID 设备标记为故障并从阵列中移除

在从逻辑阵列中删除该设备前，这是强制性的步骤，然后才能从机器中取出它 - 注意顺序（如果弄错了这些步骤，最终可能会造成实际设备的损害）：

```
### mdadm --manage /dev/md0 --fail /dev/sdb1
```

请注意在前面的例子中，知道如何添加备用设备来自动更换出现故障的磁盘。在此之后，[恢复和重建 raid 数据](https://linux.cn/article-6448-1.html) 就开始了：

![恢复和重建 raid 数据](https://img.linux.net.cn/data/attachment/album/201510/23/231708kzclq63u006rtg6q.png)

*恢复和重建 raid 数据*

一旦设备已被手动标记为故障，你就可以安全地从阵列中删除它：

```
### mdadm --manage /dev/md0 --remove /dev/sdb1
```

##### 例3：重新添加设备，来替代阵列中已经移除的设备

到现在为止，我们有一个工作的 RAID 1 阵列，它包含了2个活动的设备：/dev/sdc1 和 /dev/sdd1。现在让我们试试重新添加 /dev/sdb1 到/dev/md0：

```
### mdadm --manage /dev/md0 --re-add /dev/sdb1
```

我们会碰到一个错误:

```
### mdadm: --re-add for /dev/sdb1 to /dev/md0 is not possible
```

因为阵列中的磁盘已经达到了最大的数量。因此，我们有两个选择：a）将 /dev/sdb1 添加为备用的，如例1；或 b）从阵列中删除 /dev/sdd1 然后重新添加 /dev/sdb1。

我们选择选项 b），先停止阵列然后重新启动：

```
### mdadm --stop /dev/md0### mdadm --assemble /dev/md0 /dev/sdb1 /dev/sdc1
```

如果上面的命令不能成功添加 /dev/sdb1 到阵列中，使用例1中的命令来完成。

mdadm 能检测到新添加的设备并将其作为备用设备，当添加完成后它会开始重建数据，它也被认为是 RAID 中的活动设备：

![重建 Raid 的状态](https://img.linux.net.cn/data/attachment/album/201510/23/231708v2azltciiahr2ejj.png)

*重建 Raid 的状态*

##### 例4：使用特定磁盘更换 RAID 设备

在阵列中使用备用磁盘更换磁盘很简单：

```
### mdadm --manage /dev/md0 --replace /dev/sdb1 --with /dev/sdd1
```

![更换 Raid 设备](https://img.linux.net.cn/data/attachment/album/201510/23/231708bw2b6k9wvzr9bkrj.png)

*更换 Raid 设备*

这会导致 `--replace` 指定的设备被标记为故障，而 `--with`指定的设备添加到 RAID 中来替代它：

![检查 Raid 重建状态](https://img.linux.net.cn/data/attachment/album/201510/23/231709h3bh88f8c8dfhnnm.png)

*检查 Raid 重建状态*

##### 例5：标记 RAID 阵列为 ro 或 rw

创建阵列后，你必须在它上面创建一个文件系统并将其挂载到一个目录下才能使用它。你可能不知道，RAID 也可以被设置为 ro，使其只读；或者设置为 rw，就可以同时写入了。

要标记该设备为 ro，首先需要将其卸载：

```
### umount /mnt/raid1### mdadm --manage /dev/md0 --readonly### mount /mnt/raid1### touch /mnt/raid1/test1
```

![在 RAID 阵列上设置权限](https://img.linux.net.cn/data/attachment/album/201510/23/231709p7r4r2ehkjhkuk2k.png)

*在 RAID 阵列上设置权限*

要配置阵列允许写入操作需要使用 `--readwrite` 选项。请注意，在设置 rw 标志前，你需要先卸载设备并停止它：

```
### umount /mnt/raid1### mdadm --manage /dev/md0 --stop### mdadm --assemble /dev/md0 /dev/sdc1 /dev/sdd1### mdadm --manage /dev/md0 --readwrite### touch /mnt/raid1/test2
```

![配置 Raid 允许读写操作](https://img.linux.net.cn/data/attachment/album/201510/23/231710m88xdcxcf6o8r6ck.png)

*配置 Raid 允许读写操作*

#### 总结

在本系列中，我们已经解释了如何建立一个在企业环境中使用的软件 RAID 阵列。如果你按照这些文章所提供的例子进行配置，在 Linux 中你会充分领会到软件 RAID 的价值。

