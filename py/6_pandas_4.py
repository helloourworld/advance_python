
# coding: utf-8

## 3. 深入Pandas数据操纵

# ## 数据集整合
# ### 3.1.1 横向拼接： 直接DataFrame

# In[1]:

import pandas as pd
import json
import numpy as np


# In[2]:

pd.DataFrame([np.random.rand(2),np.random.rand(2),np.random.rand(2)],columns =['C1', 'C2'])


# ### 3.1.2 横向拼接： Concatenate

# In[3]:

json_data = [{'name': 'Wang', 'sal': 50000, 'Job': 'VP'},             {'name': 'Shen', 'Job': 'Mnger', 'report': 'VP'},
             {'name': 'Li', 'sal': 5000, 'report': 'IT'}]


# In[4]:

data_employee = pd.read_json(json.dumps(json_data))


# In[5]:

data_employee_ri = data_employee.reindex(columns=['name','Job','sal','report'])


# In[6]:

pd.concat([data_employee_ri,data_employee_ri,data_employee_ri])


# ### 3.1.3 纵向拼接： Merge

# 根据数据关联，使用关键字
# 
# * 可以指定一列或多列
# * 可以使用left_on和right_on

# In[7]:

pd.merge(data_employee_ri,data_employee_ri,on = 'name')


# In[8]:

pd.merge(data_employee_ri,data_employee_ri, on=['name','Job'])


# 根据index关联，可以直接使用left_index和right_index

# In[9]:

data_employee_ri.index.name = 'index1'
pd.merge(data_employee_ri,data_employee_ri,left_index='index1',right_index='index1')


# ** Tips:增加HOW关键字，并指定
#     
# * how = 'inner'
# * how = 'left'
# * how = 'right'
# * how = 'outer'
# 
# 结合How，可以看到merge基本再现SQL应有的功能，并保持代码整洁

# # 3.2自定义函数映射

# In[10]:

dataNumpy32 = np.asarray([('Japan', 'Tokyo',4000),('S.Korea','Seoul',1900),('China','Beijing',9100)])
DF32 = pd.DataFrame(dataNumpy32,columns=['nation','capital','GDP'])
DF32


# ** map:** 以相同规则将一列数据作为一个映射，也就是进行相同函数的处理

# In[11]:

def GDP_Factorize(v):
    fv = np.float64(v)
    if fv > 6000.0:
        return 'H'
    elif fv < 2000.0:
        return 'L'
    else:
        return 'M'


# In[12]:

DF32['GDP_Level'] = DF32['GDP'].map(GDP_Factorize)


# In[13]:

DF32['NATION'] = DF32['nation'].map(str.upper)


# In[14]:

DF32


# ## 3.3 排序
# 
# * sort: 按一列或多列值进行行级排序
# * sort_index: 根据index里的取值进行排序，而且可以根据axis决定是重排行还是重排列

# In[15]:

dataNumpy33 = np.asarray


# In[16]:

dataNumPy33 = np.asarray([('Japan','Tokyo',4000),('S.Korea','Seoul',1300),('China','Beijing',9100)])
DF33 = pd.DataFrame(dataNumPy33,columns=['nation','capital','GDP'])
DF33


# In[17]:

DF33.sort('GDP')


# In[18]:

DF33.sort(['capital', 'nation'], ascending = False)


# In[19]:

DF33.sort('GDP',ascending=False)


# In[20]:

DF33.sort_index(axis = 1,ascending=True)


# 一个好用的功能: Rank

# In[21]:

DF33.rank()


# In[22]:

DF33.rank(ascending=False)


# 注意 ** tied data(相同值)的处理**
# 
# * method = 'average'
# * method = 'min'
# * method = 'max'
# * method = 'first'

# ## 3.4 缺失数据处理
# 

# In[23]:

# >>>


# In[23]:



