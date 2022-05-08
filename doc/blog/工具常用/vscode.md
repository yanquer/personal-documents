### vscode

```
ctrl + p                #按文件名搜索
ctrl + shift + f        #全局搜索指定文件夹内容
ctrl + f                #全局搜索当前打开文件内容
ctrl + shift + p        #全局打开文件
```

关于setting.json

```json
{
    // Git 可执行文件路径
    "git.path": "D:/Program Files/Git/bin/git.exe"

    ,"editor.tabSize": 4
    ,"editor.insertSpaces": false
    ,"editor.useTabStops": true

    // 默认行尾字符。使用 \n 表示 LF，\r\n 表示 CRLF。
    ,"files.eol": "\n"
    // 控制编辑器在空白字符上显示特殊符号的方式。可选值为 "none"(无)、"boundary"(边界) 或 "all"(所有)。选择 "boundary" 选项，则不会在单词之间的单个空格上显示特殊符号。
    ,"editor.renderWhitespace": "all"

    // 去除shellcheck local的报错 In POSIX sh, 'local' is undefined
    // local is supported in many shells, including bash, ksh, dash, and BusyBox ash. However, strictly speaking, it's not POSIX.
    ,"shellcheck.exclude": ["SC3043"]
}
```

### vscode插件离线安装

离线安装

在vscode插件库（https://marketplace.visualstudio.com/vscode）搜索自己需要的插件，点击右侧 Download Extension



然后将下载的文件，复制到vscode安装目录下的bin文件夹中



在bin文件夹下打开cmd，运行如下命令

```shell
code --install-extension octref.vuter-0.23.0.vsix 	#需要安装的插件文件名
```

4.出现如下提示，则安装成功。



-----------------------------------------------------------------------------------

vscode中可直接从visx安装插件



原文链接：https://blog.csdn.net/qq_26118603/article/details/115062440

