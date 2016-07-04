
# coding: utf-8

# In[16]:

import datetime
td = datetime.date(2015,05,26)
print td


# In[17]:

get_ipython().magic(u'connect_info')


# In[18]:

def normalize(name):
    return name.capitalize()


# In[19]:

get_ipython().magic(u'qtconsole')


# In[20]:

L1 = ['DAVID', "YULIJUN", 'yulijun']


# In[21]:

L2 = list(map(normalize, L1))
print(L2)


# In[22]:

a = None
b = 'ss'
print 1 and a or b


# In[23]:

a = None
b = 'null'
s = 1 and a or b


# In[24]:

print s.strip()


# In[25]:

series = range(1,5)
import math
print sum((0.1 * each)** 2 for each in series)


# In[26]:

print (0.1**2 + 0.2** 2 + 0.3**2 + 0.4**2)


# In[27]:

import numpy as np
n = 2
prin = 1000
r = 0.09
fv = prin * (1 + r) ** (n )
print fv


# In[28]:

import numpy as np
o_0 = 78
o_1 = 4


# In[29]:

l_0=5
l_1 = 33


# In[30]:

o_0+o_1


# In[31]:

l_0+l_1


# In[32]:

o_0 + l_1


# In[33]:

111/120.0


# In[34]:

9.0/120


# In[35]:

recall = l_1*.01/((l_1+l_0)*.01)
print '%0.5f'%recall


# In[36]:

precision = l_1*0.01/((l_1+o_1)*.01)
print '%.5f'%precision


# In[37]:

print np.average((precision, recall))


# In[38]:

get_ipython().system(u'dir')


# In[39]:

import os
os.listdir('.')


# In[40]:

print os.curdir


# ![](a.jpg)

# In[40]:



