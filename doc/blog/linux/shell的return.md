### shell的return

今天写bug发现shell的return与之前java的不一样

return其实与exit基本一致    不一致的地方在于函数内return只是退出函数，exit退出脚本

返回的值只能为0-255的数字

判断时可用，而不能传递字符串之类的

操作字符串只能用全局变量了（或者echo）
