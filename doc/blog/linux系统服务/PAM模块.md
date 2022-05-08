### PAM模块

PAM（Pluggable Authentication Modules， 嵌入式模块）

一套应用程序编程接口，提供一连串的验证机制，使用者将需求告知，PAM返回使用者验证的结果

![image-20211204173529556](%E5%B8%B8%E7%94%A8%E7%9A%84%E6%8C%87%E4%BB%A4.assets/image-20211204173529556.png)

配置文件都在  /etc/pam.d 下面

例子：

passwd执行流程

- 用户执行 passwd，输入密码、
- passwd 呼叫 PAM验证模块
- PAM 模块会找到 /etc/pam.d/ 找寻与程序（passwd） 同名的配置文件
- 依据 /etc/pam.d/passwd 内的设定，引用相关的PAM模块进行验证分析
- 将验证结果回传给passwd
- passwd根据返回结果决定下一个动作（验证失败或者通过）

配置文件结构

```sh
# /etc/pam.d/passwd
#%PAM-1.0

auth    include        system-auth
```

每一行可以区分为三个字段

- type
  
  主要分四种
  
  - auth
    
    authentication的缩写，检验使用者的身份验证，通常是需要密码检验的，所以后续接的模块是用来检验用户的身份。
  
  - account
    
    大部分是在进行授权（authorization），检验使用者是否具有正确的权限，比如，使用一个过期的密码无法登陆
  
  - session
    
    管理登陆期间（会话）环境
  
  - password
    
    密码修改，变更

- flag
  
  验证通过的标准
  
  - required
    
    此验证若成功则带有success标记，
    
    若失败带有failure标记
    
    不论是否成功都会进行后续流程（有利于log）
  
  - requisite
    
    如果是failure立刻返回给源程序失败，不会进行后续流程
  
  - sufficient
    
    与上一个相反
    
    成功则立刻返回
    
    失败则继续后续步骤
  
  - optional
    
    用于显示循讯息

- PAM 模块与参数

| type | control flag | PAM模块与模块参数 |
| ---- | ------------ | ---------- |
|      |              |            |
|      |              |            |
|      |              |            |



### Linux重置root(user)

```sh
pam_tally2 --user=root --reset    # 重置登陆计数器

passwd root    # 重置密码
```
