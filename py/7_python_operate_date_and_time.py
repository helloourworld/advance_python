
# coding: utf-8

##  不管何时何地，只要我们编程时遇到了跟时间有关的问题，都要想到 datetime 和 time 标准库模块，今天我们就用它内部的方法，详解python操作日期和时间的方法。 

# In[2]:

'''
1.将字符串的时间转换为时间戳
'''
a = "2013-10-10 23:40:00"
#将其转换为时间数组
import time
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
#转换为时间戳:
timeStamp = int(time.mktime(timeArray))
timeStamp == 1381419600


# In[3]:

# 2.格式更改
'''
如a = "2013-10-10 23:40:00",想改为 a = "2013/10/10 23:40:00"
方法:先转换为时间数组,然后转换为其他格式
'''
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)


# In[4]:

otherStyleTime


# In[5]:

# 3.时间戳转换为指定格式日期
# 方法一:利用localtime()转换为时间数组,然后格式化为需要的格式,如：
timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
otherStyleTime == "2013-10-10 23:40:00"


# In[6]:

# 方法二
import datetime
timeStamp = 1381419600
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
otherStyleTime == "2013-10-10 23:40:00"


# 4.获取当前时间并转换为指定日期格式

# In[7]:

import time
#获得当前时间时间戳
now = int(time.time())  # 这是时间戳
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
otherStyleTime


# In[8]:

import datetime
#获得当前时间
now = datetime.datetime.now()  # 这是时间数组格式
#转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
otherStyleTime


# *5.获得三天前的时间的方法*

# In[9]:

import time
import datetime
#先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3))
#转换为时间戳:
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
#转换为其他字符串格式:
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
# 注:timedelta()的参数有:days,hours,seconds,microseconds


# 6.给定时间戳,计算该时间的几天前时间

# In[10]:

timeStamp = 1381419600
#先转换为datetime
import datetime
import time
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
threeDayAgo = dateArray - datetime.timedelta(days = 3)


# python 计算昨天和明天的日期

# In[11]:

import datetime
today = datetime.date.today()
today


# In[12]:

yesterday = today - datetime.timedelta(days = 1)


# In[13]:

yesterday


# In[14]:

tomorrow = today + datetime.timedelta(days = 2)
tomorrow


                print " 昨天: %s, 今天:%s, 后天: %s" %(yesterday, today, tomorrow)
                
                8、python里使用time模块来获取当前的时间 日期
                
# In[15]:

import time
print time.strftime("%H:%M：%S")


# In[16]:

## 12 hour format　＃＃
print time.strftime("%I:%M :%S")


# In[17]:

## date ##
print time.strftime("%Y-%m-%d")


# 10、使用datetime模块来获取当前的日期和时间

# In[18]:

import datetime
i = datetime.datetime.now()
i


# In[19]:

print "当前的日期和时间是 %s"%i


# In[20]:

print "ISO格式的时间和日期是%s" %i.isoformat()


# In[21]:

print "当前的年份是%s" % i.year


# In[22]:

i.month,i.day


# In[23]:

print "dd/mm/yyyy格式是%s/%s/%s" % (i.day,i.month,i.year)


# In[24]:

print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)


# 附：日期和时间的格式化参数
# %a 星期几的简写
# %A 星期几的全称
# %b 月分的简写
# %B 月份的全称
# %c 标准的日期的时间串
# %C 年份的后两位数字
# %d 十进制表示的每月的第几天
# %D 月/天/年
# %e 在两字符域中，十进制表示的每月的第几天
# %F 年-月-日
# %g 年份的后两位数字，使用基于周的年
# %G 年分，使用基于周的年
# %h 简写的月份名
# %H 24小时制的小时
# %I 12小时制的小时
# %j 十进制表示的每年的第几天
# %m 十进制表示的月份
# %M 十时制表示的分钟数
# %n 新行符
# %p 本地的AM或PM的等价显示
# %r 12小时的时间
# %R 显示小时和分钟：hh:mm
# %S 十进制的秒数
# %t 水平制表符
# %T 显示时分秒：hh:mm:ss
# %u 每周的第几天，星期一为第一天 （值从0到6，星期一为0）
# %U 第年的第几周，把星期日做为第一天（值从0到53）
# %V 每年的第几周，使用基于周的年
# %w 十进制表示的星期几（值从0到6，星期天为0）
# %W 每年的第几周，把星期一做为第一天（值从0到53）
# %x 标准的日期串
# %X 标准的时间串
# %y 不带世纪的十进制年份（值从0到99）
# %Y 带世纪部分的十制年份
# %z，%Z 时区名称，如果不能得到时区名称则返回空字符。
# %% 百分号
