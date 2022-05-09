## es遇到的问题2



#### 1、数据data

默认情况下es的data都是存在于path.data所指定的目录的，path.data默认为文件的data目录，

所以data存在着上一次或者上几次的运行配置

故有些时候需要清空data来重新运行



#### 2、关于cluster.initial_master_nodes

使用的7.13的版本，有一些配置过时了

|             过时配置             |        配置（新）        |
| :------------------------------: | :----------------------: |
| discovery.zen.ping.unicast.hosts |   discovery.seed_hosts   |
|   discovery.zen.hosts_provider   | discovery.seed_providers |
|   discovery.zen.nomasterblock    |  cluster.nomasterblock   |

discovery.seed_hosts
提供集群中符合主机要求的节点的列表. 每个值的格式为host:port或host ，其中port默认为设置transport.profiles.default.port。
discovery.seed_providers
以文件的方式提供主机列表，可以动态修改，而不用重启节点（容器化环境适用）
cluster.initial_master_nodes
设置全新群集中符合主机要求的节点的初始集合. 默认情况下，该列表为空，这意味着该节点希望加入已经被引导的集群
discovery.findpeersinterval
选定主节点发现时间间隔,默认1S



<u>**注意：自己测试中发现具有选举权的master节点一定要设置cluster.initial_master_nodes，值为当前所有可以参与选举的节点，否则会出现“master not discovered yet”的错误；**</u>

非master节点可以不设置，设置了反而会出现真正的master节点无法实时发现的问题，猜测原因可能是因为，单独的node节点因为设置了，所以与master节点不会主动发生通信



官网文档如下：

**`cluster.initial_master_nodes`**

([Static](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/settings.html#static-cluster-setting)) Sets the initial set of master-eligible nodes in a brand-new cluster. By default this list is empty, meaning that this node expects to join a cluster that has already been bootstrapped. See [`cluster.initial_master_nodes`](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/important-settings.html#initial_master_nodes).

在全新的集群中设置初始主节点集。 默认情况下，这个列表是空的，这意味着这个节点希望加入一个已经被引导的集群。



具备成为master节点的应该设置initial_master_nodes为一个master集群列表，而其他的node不用设置，可以自己引导（测试发现如果都设置，第一次启动集群时，master节点必须最后启动才可以完全发现所有的node）



更新，有毒吧，全设置了initial_master_nodes，删除了data数据又重新测试了一下，居然master可以不用最后启动了也可以全部发现了。那就是昨天本机网络有问题？





#### 3、关于master节点

设置了node-master：true的节点，表示有资格成为Master的节点。

选举Master选举Master需要所有的Master候选节点共同工作，即使某些节点发生了故障，这个工作也必须能够正常进行，es需要通过仲裁的方式选取出还能正常工作的节点，再组成集群，避免形成“脑裂”，这里“脑裂”是指，可能出现不止一个Master节点，比如节点间的通信断开后，各个Master候选节点都有可能认为其他节点都宕机，提升自己为Master，造成集群状态不一致的情况。由此衍生出参与选主时，需要配置能通信的候选节点数量。discovery.zen.minimummasternodes，缺省配置是1.一个基本的原则是这里需要设置成 N/2 1, N是集群中节点的数量。

由上面的分析我们可以知道，是否发生选举，在于节点彼此间的通信感知，由此可知节点间的网络通信同样重要，就像是API接口调用，有调用就会有超时，所以在网络环境差的情况下，超时配置显得尤为重要。discovery.zen.ping.timeout用来指定两个节点间的通信超时时间，默认是3S。根据网络情况，调整这个参数，尽量避免由于网络延迟，带来的不必要的选举。



#### 4、分片与副本

**分片**就是将数据分成几份，使用head-master可以很直观的看出，

例如设置分片：5

就会在主页出现0,1,2,3,4五个分片

**副本**就是数据的备份，

例如分片为5，副本为1：就会出现0,0,1,1,2,2,3,3,4,4一共十个分片，有一份是副本



官方：

一个索引可以存储超出单个结点硬件限制的大量数据。比如，一个具有10亿文档的索引占据1TB的磁盘空间，而任一节点都没有这样大的磁盘空间；或者单个节点处理搜索请求，响应太慢。

为了解决这个问题，Elasticsearch提供了将索引划分成多份的能力，这些份就叫做分片。当你创建一个索引的时候，你可以指定你想要的分片的数量。每个分片本身也是一个功能完善并且独立的“索引”，这个“索引”可以被放置到集群中的任何节点上。 
分片之所以重要，主要有两方面的原因：

- 允许你水平分割/扩展你的内容容量
- 允许你在分片（潜在地，位于多个节点上）之上进行分布式的、并行的操作，进而提高性能/吞吐量

至于一个分片怎样分布，它的文档怎样聚合回搜索请求，是完全由Elasticsearch管理的，对于作为用户的你来说，这些都是透明的。

在一个网络/云的环境里，失败随时都可能发生，在某个分片/节点不知怎么的就处于离线状态，或者由于任何原因消失了。这种情况下，有一个故障转移机制是非常有用并且是强烈推荐的。为此目的，Elasticsearch允许你创建分片的一份或多份拷贝，这些拷贝叫做复制分片，或者直接叫复制。复制之所以重要，主要有两方面的原因：

- 在分片/节点失败的情况下，提供了高可用性。因为这个原因，注意到复制分片从不与原/主要（original/primary）分片置于同一节点上是非常重要的。
- 扩展你的搜索量/吞吐量，因为搜索可以在所有的复制上并行运行

总之，每个索引可以被分成多个分片。一个索引也可以被复制0次（意思是没有复制）或多次。一旦复制了，每个索引就有了主分片（作为复制源的原来的分片）和复制分片（主分片的拷贝）之别。分片和复制的数量可以在索引创建的时候指定。在索引创建之后，你可以在任何时候动态地改变复制数量，但是不能改变分片的数量。

默认情况下，Elasticsearch中的每个索引被分片5个主分片和1个复制，这意味着，如果你的集群中至少有两个节点，你的索引将会有5个主分片和另外5个复制分片（1个完全拷贝），这样的话每个索引总共就有10个分片。一个索引的多个分片可以存放在集群中的一台主机上，也可以存放在多台主机上，这取决于你的集群机器数量。主分片和复制分片的具体位置是由ES内在的策略所决定的。





#### 5、哭了，NS用的是python2.7，es导的es7.13的模块，而模块es7.13调用了urllib3的方法，最后urllib3只支持python3



是为什么发现这个问题的呢？

因为外网机下载好es的python的模块之后安装到内网机，windows安装时报错缺少两个模块

certifi，urllib

然后去下载安装，成功，

接着自己写了个测试使用，成功



然后接入数据库数据，

debian安装es7，比win上多安装一个模块，因为装urllib3的时候提示报错，查询后是setuptools版本过低，遂去找了适合python2的最新模块包，

报错找不到RecursionError，然后在http_urllib3.py里也确实没有发现RecursionError是在哪里定义的，然后去搜了urllib3这个模块，发现只支持python3



所以如果现在要改的话

要么把服务器python2.7升级，但是这样要改很多包

要么就把es7的模块给换了，本地集群的服务的得重新来，合着白装了这几个。。。



现在尝试，就未定义RecursionError这个错来修复，尝试注释之类的



嗯，注释了这个except，没报这个错了，

新的错误：虚拟机连接不上宿主机