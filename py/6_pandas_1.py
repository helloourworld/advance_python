
# coding: utf-8

# In[ ]:

import codecs
import requests
import numpy as np
import scipy as sp
import pandas as pd
import datetime
import json


# In[ ]:

# get test data
from IPython import get_ipython

r = requests.get("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")


# In[ ]:

# 查看当前目录下内容
get_ipython().system(u'ls -l')


# In[ ]:

# write data in file for test
with codecs.open('S1EP3_Iris.txt','w',encoding='utf-8') as f:
    f.write(r.text)


# In[ ]:

# cat the text
print r.text


# In[ ]:

with codecs.open('S1EP3_Iris.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print line,


# ## Pandas  的 意义在于：
# # 快速的识别结构化数据

# In[ ]:

import pandas as pd
irisdata = pd.read_csv('S1EP3_Iris.txt', header = None, encoding='utf-8')


# In[ ]:

irisdata


# # 快速的操作元数据

# In[ ]:

cnames = ['sepal_length', 'sepal_width','petal_length', 'petal_width', 'class']
irisdata.columns = cnames
irisdata;


# 快速过滤
# =======

# In[ ]:

irisdata[irisdata['petal_width'] == irisdata.petal_width.max()]


# ##快速切片

# In[ ]:

irisdata.iloc[::30, :2]


# ## 快速统计

# In[ ]:

print irisdata['class'].value_counts()
len(irisdata)


# In[ ]:

for x in xrange(4):
    s = irisdata.iloc[:,x]
    print '{0:<12}'.format(s.name.upper()), " Statistics: ",    '{0:>5} {1:>5} {2:>5} {3:>5}'.format(s.max(), s.min(), round(s.mean(),2), round(s.std(),2))


# ## 快速 MapReduce

# In[ ]:

slogs = lambda x: sp.log(x) * x
entpy = lambda x: sp.exp((slogs(x.sum()) - x.map(slogs).sum())/x.sum())
irisdata.groupby('class').agg(entpy)


# In[ ]:



