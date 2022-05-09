## crontab定时器

cron表达式中问号(?)的使用

【摘要】
cron表达式详解其中问号(?)只能用在DayofMonth和DayofWeek两个域，由于指定日期(DayofMonth)和指定星期(DayofWeek)存在冲突，所以当指定了日期(DayofMonth)后（包括每天*），星期(DayofWeek)必须使用问号(?)，同理，指定星期(DayofWeek)后，日期(DayofMonth)必须使用问号(?)。

其中问号(?)只能用在DayofMonth和DayofWeek两个域，由于指定日期(DayofMonth)和指定星期(DayofWeek)存在冲突，所以当指定了日期(DayofMonth)后（包括每天*），星期(DayofWeek)必须使用问号(?)，同理，指定星期(DayofWeek)后，日期(DayofMonth)必须使用问号(?)。

原文链接：https://blog.csdn.net/qq_45587822/article/details/119760955

