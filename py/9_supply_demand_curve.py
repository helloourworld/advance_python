
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[2]:

import scipy as sp


# In[3]:

def make_supply(A,B,C):
    def supply_func(q):
        return A * q/(C - B * q)
    return supply_func
    
def make_demand(K,L):
    def demand_func(q):
        return K/(1 + L * q)
    return demand_func


        


# In[4]:

A,B,C = 23.3, 9.2, 82.4


# In[5]:


K,L = 1.2, 0.54


# In[6]:


supply = make_supply(A,B,C)
demand = make_demand(K, L)


# In[7]:

q = linspace(0.01, 5, 200)
plot(q, supply(q), lw = 2)
plot(q, demand(q), lw = 4)
title('Supply and demand curves')
xlabel('Quantity (thousands of units)')
ylabel('Price($)')
legend(['Supply', 'Demand'], loc = 'upper left')


# In[7]:



