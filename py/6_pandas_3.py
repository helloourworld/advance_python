
# coding: utf-8

## 2. 大熊猫世界来去自如：Pandas的I/O

# 老生常谈，从基础来看，仍然关心pandas对于与外部数据是如何交互的。

# ## 2.1 结构化数据输出输入
# 
# * read_csv与to_csv是一对输出输入工具，read_csv直接返回pandas.DataFrame，而to_csv只要执行即可写文件。
#     * read_table: 功能类似
#     * read_fwf: 操作fixed width file
# * read_excel 与 to_excel 方便地与excel交互
# 
# * header表示数据中是否存在列名，如果在第0行就写就写0，并且开始读数据时跳过相应的行数，不存在可以写none
# * names表示要用给定的列名来作为最终的列名
# * encoding 表示数据集的字符编码，通常而言一份数据为了方便的进行文件传输都以utf-8作为标准

# In[1]:

import pandas as pd
import numpy as np
import json


# In[2]:

irisdata = pd.read_csv('S1EP3_Iris.txt', header =None, encoding='utf-8')


# In[3]:

cnames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']


# In[4]:

irisdata.columns = cnames


# In[5]:

irisdata.head(5)


# # 希望了解全部参数的请移步API：
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html#pandas.read_csv
# 
# (http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html#pandas.read_csv)
# 
# > 这里介绍一些常用的参数：
# 
# ### 读取处理：
# 
# * skiprows：跳过⼀一定的⾏行数
# * nrows：仅读取⼀一定的⾏行数
# * skipfooter：尾部有固定的行数永不读取
# * skip_blank_lines：空行跳过
# 
# ### 内容处理：
# 
# * sep/delimiter：分隔符很重要，常见的有逗号，空格和Tab('\t')
# * na_values：指定应该被当作na_values的数值
# * thousands：处理数值类型时，每千位分隔符并不统⼀一 (1.234.567,89或者1,234,567.89都可能)，此时要把字符串转化为数字需要指明千位分隔符
# 
# ### 收尾处理：
# 
# * index_col：将真实的某列（列的数目，甚至列名）当作index
# * squeeze：仅读到一列时，不再保存为pandas.DataFrame⽽而是pandas.Series

# 以下为读取推荐书籍数据，采用pandas.read_csv来读取

# In[6]:

book_rating = pd.read_csv('BX-Dump/BX-Book-Ratings.csv', header=None, nrows = 1000 ,sep = ';')


# In[7]:

book_rating


# In[8]:

book_rating.colnames = ['user','book','rating']


# In[9]:

# na_values
users = pd.read_csv('BX-Dump/BX-Users.csv', header=None, nrows = 1000 ,sep = ';', na_values ='\N',names=['userid','location','age'])


# In[10]:

users


# In[11]:

# usecols 只读取subset内容
# 数据集6451数据问题：&amp; 在解析时出错 （&）
# solution for &amp;
# import fileinput  
# for line in fileinput.input("BX-Dump/BX-Books.csv", inplace=1):  
    # print line.replace('\&amp\;', '&'),  
# title中出现'"',在解析时出错
# solution for \" 转换为\'
# import fileinput  
# for line in fileinput.input("BX-Dump/BX-Books.csv", inplace=1):  
    # print line.replace('\\\"', '\''),  
# error_bad_lines=False
"""
error_bad_lines : boolean, default True
Lines with too many fields (e.g. a csv line with too many commas) will by default cause an exception to be raised, and no DataFrame will be returned. If False, then these “bad lines” will dropped from the DataFrame that is returned. (Only valid with C parser)
warn_bad_lines : boolean, default True
If error_bad_lines is False, and warn_bad_lines is True, a warning for each “bad line” will be output. (Only valid with C parser).
"""
books = pd.read_csv('BX-Dump/BX-Books.csv', quotechar='"',header=None ,sep = ';', na_values ='\N',names=['isbn','title','author'],usecols=[0,1,2],error_bad_lines=False)


# In[12]:

books


### 2.1 Excel

# 对于存储着极为规整数据的Excel而言，其实没必要一定用Excel来存，尽管Pandas也十分友好地提供I/O接口。

# In[13]:

irisdata.to_excel('S1EP3_Iris.xls',index = None,encoding='utf-8')


# In[14]:

irisdata_from_excel = pd.read_excel('S1EP3_Iris.xls',header=0, encoding='utf-8')
irisdata_from_excel


# ** 唯一重要的参数： sheetname=k ,标志着一个excel的第K个sheet页将会被取出 。（From 0）**

### 2.2 半结构化数据

# JSON: 网络传输出常用的一种数据格式
#     
# 仔细看一下， 实际上这就是我们平时收集到异源数据的风格是一致的：
# 
# * 列名不能完全匹配
# * key可能并不唯一
# * 元数据被保存在数据里

# In[15]:

json_data = [{'name': 'Wang', 'sal': 50000, 'job': 'VP'},             {'name': 'Shen', 'Job': 'Mnger', 'report': 'VP'},
             {'name': 'Li', 'sal': 5000, 'report': 'IT'}]


# In[16]:

data_employee = pd.read_json(json.dumps(json_data))


# In[17]:

data_employee
data_employee_ri = data_employee.reindex(columns=['name','job','sal','report'])


# In[18]:

data_employee


# In[19]:

data_employee_ri


# In[19]:



