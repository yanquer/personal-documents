### SSH

设置会话过期

/etc/ssh/sshd_config

```sh
ServerAliveInterval 60        # 单次发送包检查链接时间，单位是秒，为0表示不发
ServerAliveCountMax 30        # 最大检查次数，超过后断开链接
```

- **ClientAliveInterval**: 这个其实就是SSH Server与Client的心跳超时时间，也就是说，当客户端没有指令过来，Server间隔`ClientAliveInterval`的时间（单位秒）会发一个空包到Client来维持心跳，60表示每分钟发送一次，然后客户端响应，这样就保持长连接了保证Session有效, 默认是0, 不发送;
- **ClientAliveCountMax**：当心跳包发送失败时重试的次数，比如现在我们设置成了30，如果Server向Client连续发30次心跳包都失败了，就会断开这个session连接。

另一个地方

/etc/profile

```sh
TMOUT=60    # 空闲等待时间，默认值0，表示不超时
```

### ssh的时候定义别名

**方法 1 – 使用 SSH 配置文件**

这是我创建别名的首选方法。

我们可以使用 SSH 默认配置文件来创建 SSH 别名。为此，编辑 `~/.ssh/config` 文件（如果此文件不存在，只需创建一个）：

```text
$ vi ~/.ssh/config
```

添加所有远程主机的详细信息，如下所示：

```text
Host webserver
    HostName 192.168.225.22
    User sk

Host dns
    HostName server.example.com
    User root

Host dhcp
    HostName 192.168.225.25
    User ostechnix
    Port 2233
```

**方法 2 – 使用 Bash 别名**

这是创建 SSH 别名的一种应急变通的方法，可以加快通信的速度。你可以使用 [alias 命令](https://link.zhihu.com/?target=https%3A//www.ostechnix.com/the-alias-and-unalias-commands-explained-with-examples/)使这项任务更容易。

打开 `~/.bashrc` 或者 `~/.bash_profile` 文件：

```text
alias webserver='ssh sk@server.example.com'
alias dns='ssh sk@server.example.com'
alias dhcp='ssh sk@server.example.com -p 2233'
alias ubuntu='ssh sk@server.example.com -i ~/.ssh/id_rsa_remotesystem'
```

再次确保你已使用自己的值替换主机、主机名、端口号和 IP 地址。保存文件并退出。

然后，使用命令应用更改：

```text
$ source ~/.bashrc
```

或者

```text
$ source ~/.bash_profile
```

在此方法中，你甚至不需要使用 `ssh 别名` 命令。相反，只需使用别名，如下所示。

```text
$ webserver
$ dns
$ dhcp
$ ubuntu
```

**（方法2太慢了 alias debian9=“user@host” 然后 ssh debian9 太慢了 ）**

