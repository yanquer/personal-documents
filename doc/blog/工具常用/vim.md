### vim

使用

```shell
vim    file            #打开文件
    file1 file2        #打开两个文件
    -O2 file1 file2    #分屏打开两个文件。有几个O几
    -o
                    #大写O表示左右排版，小写o表示上下排版
```

更多详见：    https://zhuanlan.zhihu.com/p/68111471

vim有四个模式，：

- 正常模式 (Normal-mode)
- 插入模式 (Insert-mode)
- 命令模式 (Command-mode)
- 可视模式 (Visual-mode)

> **撤销操作**

```shell
:u            #撤销
ctrl+r        #恢复撤销
```

> **格式、模式**

```shell
#格式
:set fenc                    #查看文本编码 fenc是fileencoding缩写
                            #与 :set fileencoding 一样
:set fenc='filecode'        #转换当前文本的编码为指定的编码
:set enc='filecode'            #以指定的编码显示文本，但不保存到文件中 encoding缩写
                            #这里的“编码”常见为gbk utf-8 big5 cp936
                            #fileencoding---fenc
                            #     encoding---enc

#模式
:set ff?                    #查看模式类型，一般为dos,unix
:set ff=dos                    #设置模式    例如设置unix模式    :set fileformat=unix
                            #与:set fileformat=dos一个效果 ff是缩写
                            #  fileformat---ff
                            # :%s/^M//g等同于:set ff=unix
```

> **移动编辑**

```shell
gg                #光标跳转到文件首行
G                #光标跳转文件最后一行
_                #光标移到当前行第一个非空字符位置
A                #移动到行尾
v,V                #可视化模式
行号+gg            #快速移动到指定行号
```

> **粘贴与复制**

```shell
y                #复制当前光标所在处字符
yy                #复制当前光标所在行
p                #在当前位置粘贴上一次复制的内容
```

> 删除

```shell
dd                #命令模式下dd删除当前行
#删除多行，如删除8-17行
8,17d
```

> **查找**

```shell
/'what'            #斜杠后跟查找的字符
```

> **其他**

```shell
:w                 #保存不退出
:w                 #新文件名 把文件另存为新文件
:q                 #不保存退出
:wq             #保存退出
:!                 #强制
:q!             #强制不保存退出，用于修改文件之后，不保存数据退出
:wq!             #强制保存退出，当文件的所有者或 root 用户，对文件没有写权限的时候，强制写入数据使用

:ls                #查看当前编辑器所有文件
:bn                #切换到第n个文件  主要是b控制的 序号可以先ls查看
```


#### 便捷配置

###### 语法高亮

```vim
syntax on                # 语法高亮
filetype indent on       # 开启文件类型检查，并且载入与该类型对应的缩进规则




set showmode               # 底部显示当前模式， 如命令模式、插入模式
set showcmd                # 命令模式下，底部显示当前键入的指令
set mouse=a                # 支持使用鼠标
set encoding=utf-8         # 使用 utf-8 编码
set t_Co=256               # 启用256色

# 缩进
set autoindent             # 按下回车键时，下一行缩进与上一行保持一致
set tabstop=2              # 按下tab时, vim显示的空格数
set shiftwidth             # 在文本上按下>>（增加一级缩进）、<<（取消一级缩进）或者==（取消全部缩进）时，每一级的字符数。
set expandtab              # 由于 Tab 键在不同的编辑器缩进不一致，该设置自动将 Tab 转为空格。
set softtabstop=2          # Tab 转为多少个空格

# 外观
set number                  # set nu 也可，显示行号
set relativenumber          # 显示光标所在的当前行的行号，其他行都为相对于该行的相对行号。
set cursorline              # 光标所在当前行高亮
set textwidth=80            # 设置行宽，即一行显示多少字符
set wrap                    # 自动折行，即太长的行分为几行显示
set nowrap                  # 关闭自动折行
set linebreak               # 只有遇到指定的符号（比如空格、连词号和其他标点符号），才发生折行。也就是说，不会在单词内部折行。
set wrapmargin=2            # 指定折行处与编辑窗口的右边缘之间空出的字符数。
set scrolloff=5             # 垂直滚动时，光标距离顶部/底部的位置（单位：行）
set sidescrolloff=15        # 水平滚动时，光标距离行首或行尾的位置（单位：字符）。该配置在不折行时比较有用。
set laststatus=2            # 是否显示状态栏。0 表示不显示，1 表示只在多窗口时显示，2 表示显示。
set  ruler                  # 在状态栏显示光标的当前位置（位于哪一行哪一列）。

```

参考：[Vim 配置入门 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2018/09/vimrc.html)



#### 语法

###### 变量

变量定义 let a=1

符号为 echo &a

```vim
let a = 1
echo &a
```



参考：[VIM 中文用户手册: 编写 Vim 脚本](https://yianwillis.github.io/vimcdoc/doc/usr_41.html)
