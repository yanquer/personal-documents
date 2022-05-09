## root 密码忘记

查看 /etc/shadow 使用的加密机制

```
authconfig --test | grep hashing
```

- 方法一
  
  重启进入单人维护模式，系统会主动给予 root 权限的 bash 接口， 然后 passwd 修改

- 方法二
  
  以 Live CD 开机后挂载根目录去修改 /etc/shadow，将里面的 root 密码字段清空

- 方法三
  
  如果普通用户有sudo的passwd权限，那么直接 sudo passwd即可