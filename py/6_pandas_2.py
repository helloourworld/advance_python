
# coding: utf-8

## 1、 欢迎 to pandas 

# Pandas的重要数据类型
# * DataFrame（二维表)
# * Series（一维序列)
# * Index(行索引，行级元数据）

# 1.1 Series: pandas的长枪（数据表中的一列或一行，观测向量，一维数组。。。）
# ----------------------------------------------------------------------
# 数据世界中对于任意一个个体的全面观测，或者对于任意一组个体某一属性的观测，全部可以抽象炎Series的概念。
# 
# 用值构建一个Series：
# 由默认index和value组成

# In[1]:

import numpy as np
import pandas as pd
Series1 = pd.Series(np.random.randn(4))
print Series1,type(Series1)
print Series1.index
print Series1.values


# ## Series 支持过滤的原理就如同NumPy：

# In[2]:

print Series1>0


# In[3]:

print Series1[Series1>0]


# ## 当然也支持Broadcasting：

# In[4]:

print Series1 * 2
print Series1 + 5


# #以及Universal Function：

# In[5]:

print np.exp(Series1)
#NumPy Universal Function
f_np = np.frompyfunc(lambda x:np.exp(x*2+5),1,1)
print f_np(Series1)


# ##在序列上就使⽤用⾏行标，⽽而不是创建⼀一个2列的数据表，能够轻松辨别哪⾥里是数据，哪⾥里是元数据：

# In[6]:

series2 = pd.Series(Series1.values, index = ['norm_' + unicode(i) for i in xrange(4)])


# In[7]:

print series2, type(series2)


# In[8]:

print series2.index


# In[9]:

print type(series2.index)


# In[10]:

print series2.values


# 虽然⾏行是有顺序的，但是仍然能够通过⾏行级的index来访问到数据：
# （当然也不尽然像Ordered Dict，因为⾏行索引甚⾄至可以重复，不推荐重复的⾏行索引不代表不能⽤用）

# In[11]:

print series2[['norm-0', 'norm-3']]


# In[12]:

print series2[['norm_0', 'norm_3']]


# In[13]:

print 'norm_0' in series2
print 'norm-0' in series2


# 默认⾏行索引就像⾏行号⼀一样：

# In[14]:

print series2.index


# In[15]:

print Series1.index


# 从Key不重复的Ordere Dict或者从Dict来定义Series就不需要担心索引重复

# In[16]:

Series3_Dict= {"Japan":"Tokyo", "S.Korea":"Seoul", "China":"Bj"}
Series3_pdseries = pd.Series(Series3_Dict)


# In[17]:

print Series3_pdseries


# In[18]:

print Series3_pdseries.values


# In[19]:

print Series3_pdseries.index


# ## 想让序列按你的排序方式保存？就算有缺失值都毫无问题

# In[20]:

Series4_IndexList = ["Japan", "China", "Singapore", "S.Korea"]


# In[21]:

Series4_pdseries = pd.Series(Series3_Dict, index = Series4_IndexList)


# In[22]:

print Series4_pdseries


# In[23]:

print Series4_pdseries.values


# In[24]:

print Series4_pdseries.index


# In[25]:

print Series4_pdseries.isnull()


# In[26]:

print Series4_pdseries.notnull()


# #整个序列级别的元数据信息：name
# 
# #当数据序列以及index本⾝身有了名字，就可以更⽅方便的进⾏行后续的数据关联啦！

# In[27]:

print Series4_pdseries.name


# In[28]:

print Series4_pdseries.index.name


# In[29]:

Series4_pdseries.name = 'Capital series'
Series4_pdseries.index.name = "Nation"
print Series4_pdseries


# "字典"？不是的，⾏行index可以重复，尽管不推荐。

# In[30]:

Series5_IndexList = ['A', 'B', 'B', 'c']
Series5 = pd.Series(Series1.values, index = Series5_IndexList)


# In[31]:

print Series5


# In[32]:

print Series5[['B', 'C']]


### 1.2 DataFrame：pandas的战锤(数据表，⼆二维数组)

# Series的有序集合，就像R的DataFrame一样方便。
# 
# 仔细想想，绝大部分的数据形式都可以表现为DataFrame。
# 
# 从NumPy二维数组、从文件或者从数据库定义：数据虽好，勿忘列名

# In[33]:

dataNumpy = np.asarray([('Japan', 'Tokyo', 4000), ('S.Korea', 'Seoul', 1300), ('China', 'Beijing', 9100)])


# In[34]:

DF1 = pd.DataFrame(dataNumpy, columns=['nation','capital','GDP'])


# In[35]:

dataNumpy


# In[36]:

DF1


# 等长的列数据保存在一个字典里（Json): 很不幸，字典Key是无序的

# In[37]:

dataDict = {'nation': ['Japan','S.Korea','China'],'capital': ['Tokyo', 'Seoul', 'Beijing'], 'GDP': [4900, 1300, 9100]}


# In[38]:

DF2 = pd.DataFrame(dataDict)


# In[39]:

DF2


# In[40]:

DF21 = pd.DataFrame(DF2, columns=['nation','capital','GDP'])


# In[41]:

DF21


# In[42]:

DF22 = pd.DataFrame(DF2, columns = ['nation', 'capital', 'GDP'], index = [2,0,1])


# In[43]:

DF22


# 从DataFrame中取出列？两种方法（与JavaScript完全一致）

# * '.'的写法容易与其他预留类关键字产生冲突
# * '[]'的写法最安全

# In[44]:

print DF22.nation, DF22.capital


# In[45]:

print DF22['GDP']


# 从DataFrame中取出行？（至少)两种方法：

# In[46]:

print DF22[0:1] # 给出的实际是DataFrame


# In[47]:

print DF22.ix[0] # 通过对应Index给出行


# 像Numpy切片一样的终极招式： iloc

# In[48]:

print DF22.iloc[0,:]


# In[49]:

print DF22.iloc[:,0]


# 听说你从Alter Table地狱来，大熊猫笑了
# 然而动态增加列无法用"."的⽅方式完成，只能⽤用*"[ ]"*

# In[50]:

DF22['population'] = [1600, 130, 55]


# In[51]:

DF22


### 1.3 Index：pandas进行数据操纵的鬼牌（行级索引）

# 行级索引是
# --------
# * 元数据
# * 可能由真实数据产生，因此可以视作数据
# * 可以由多重索引也就是多个列组合而成
# * 可能和列名进行交换，也可以进行堆叠和展开，达到Excel透视表效果

# Index有四种，，，哦no 多种写法 一些重要的索引类型包括：
# ------
# * pd.Index（普通）
# * Int64Index(数值型索引）
# * MultiIndex（多重索引， 在数据操纵详细描述）
# * DatatimeIndex（以时间格式作为索引）
# * PeriodIndex （含周期的时间格式作为索引）

# 直接定义普通索引，长得就和普通的Series 一样
# 

# In[52]:

index_names = ['a','b','c']


# In[53]:

Series_for_Index = pd.Series(index_names)


# In[54]:

print pd.Index(index_names)


# In[55]:

print pd.Index(Series_for_Index)


# 可惜Immutable，牢记！

# In[56]:

index_names = ['a','b','c']
index0 = pd.Index(index_names)
print index0.get_values()
index0[2] = 'd'


# 扔进去一含有多元组的List,就有了*MultiIndex*
# 可惜，如果这个List Comprehension改成小括号，就不对了。

# In[57]:

multi1 = pd.Index([['Row_' + str(x+1), 'Col_'+ str(y+1)] for x in xrange(4) for y in xrange(4)])
multi1.name = ['index1', 'index2']
print multi1


# In[58]:

multi1 = pd.Index([('Row_' + str(x+1), 'Col_'+ str(y+1)) for x in xrange(4) for y in xrange(4)])
multi1.name = ['index1', 'index2']
print multi1


# 对于**Series**来说，如果拥有了多重Index,数据， 变形

# * ⼆二重MultiIndex的Series可以unstack()成DataFrame
# *   DataFrane可以stack成拥有二重MultiIndex的Series

# In[59]:

data_for_multi1 = pd.Series(xrange(0,16), index= multi1)
data_for_multi1


# In[60]:

data_for_multi1.unstack()


# In[61]:

data_for_multi1.unstack().stack()


# 我们来看一下非平衡数据的例子：
# Row_1,2,3,4 和 Col_1,2,3,4 并不是全组合的。

# In[62]:

multi2 = pd.Index([('Row_' + str(x+1), 'Col_' + str(y+1)) for x in xrange(5) for y in xrange(x)])
multi2


# In[63]:

for x in xrange(5):
    for y in xrange(x):
        print y+1
    print '**'


# In[64]:

data_for_multi2 = pd.Series(np.arange(10), index = multi2)
data_for_multi2


# In[65]:

data_for_multi2.unstack()


# In[66]:

data_for_multi2.unstack().stack()


# ## DateTime标准库如此好用，你值得拥有

# In[67]:

import datetime
dates = [datetime.datetime(2015,1,1), datetime.datetime(2015,2,8),datetime.datetime(2015,1,30)]


# In[68]:

pd.DatetimeIndex(dates)


# 如果你不仅需要时间格式统一，时间频率也要统一的话
# --------

# In[69]:

periodindex1 = pd.period_range('2015-01', '2015-04',freq = 'M')


# print periodindex1

# 月级精度和日级精度如何转换？
# ------
# 有的公司以1号代表当月 ，有的以最后一天代表 ，转化起来很麻烦

# In[70]:

print periodindex1.asfreq('D', how = 'start')
print periodindex1.asfreq('D', how = 'end')


# ## 最后的最后，我要真正把两种频率的时间精度匹配上？

# In[71]:

periodindex_mon = pd.period_range('2015-01', '2015-03',freq='M').asfreq('D',how='start')
periodindex_day = pd.period_range('2015-01-01', '2015-3-31', freq='D')


# In[72]:

print periodindex_mon
print periodindex_day


# In[73]:

# 粗粒度数据＋reindex＋ffill/bfill
full_ts = pd.Series(periodindex_mon, index=periodindex_mon).reindex(periodindex_day, method='ffill')
full_ts


# ### 关于索引，方便的操作有？
# 前面描述过了，索引有序，重复，但一定程度上又能通过key来访问，也就是说，某些集合操作都是可以⽀支持的。

# In[74]:

index1 = pd.Index(['A', 'B', 'B', 'c''c'])
index2 = pd.Index(['C', 'D', 'E', 'E', 'F'])
index3 = pd.Index(['B', 'c', 'A'])
print index1.append(index2)


# In[75]:

print index1.difference(index2)


# In[76]:

print index1.intersection(index3)


# In[77]:

print index1.union(index2) # Support unique-value Index well


# In[78]:

print index3.drop('A') # Support unique-value Index well
print index1.is_monotonic,index2.is_monotonic,index3.is_monotonic


# In[79]:

print index1.is_unique,index2.is_unique,index3.is_unique


# In[79]:



