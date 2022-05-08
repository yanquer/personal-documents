##### python定时任务（schedule）

```python
import schedule

def job(name):
    print("her name is : ", name)
    
name = "longsongpong"

schedule.every(10).minutes.do(job, name)   #每隔十分钟执行一次任务
schedule.every().hour.do(job, name)   #每隔一小时执行一次任务
schedule.every().day.at("10:30").do(job, name)   #每天的10:30执行一次任务
schedule.every(5).to(10).days.do(job, name)   #每隔5到10天执行一次任务
schedule.every().monday.do(job, name)   #每周一的这个时候执行一次任务
schedule.every().wednesday.at("13:15").do(job, name)   #每周三13:15执行一次任务

while True:
    schedule.run_pending()   #run_pending：运行所有可以运行的任务
```





此处学习是由于网络脚本定时器的编写，完成的python脚本代码如下：

```python
#!/usr/local/bin/python
import schedule
import time
import os


def backup():
    os.system("cd ~/;"
              "cd ~/sql_backup 2> /dev/null || mkdir sql_backup && cd ~/sql_backup;dir=$(date +'%Y-%m-%d');"
              "mkdir ${dir} 2>/dev/null;"
              "mysqldump -uroot -pduoyiIm trainning_server_db user > ~/sql_backup/${dir}/user.sql;"
              "mysqldump -uroot -pduoyiIm trainning_server_db co_group > ~/sql_backup/${dir}/co_group.sql;"
              "mysqldump -uroot -pduoyiIm trainning_server_db co_group_mem > ~/sql_backup/${dir}/co_group_mem.sql;"
              "mysqldump -uroot -pduoyiIm trainning_server_db tbl_user_private "
              "> ~/sql_backup/${dir}/tbl_user_private.sql;")
              
schedule.every.day().at("5:00").do(backup)
while true:
    schedule.run_pending()

```

