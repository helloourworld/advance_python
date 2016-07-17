
# coding: utf-8

# In[36]:

# trick 1 print one tree
for i in range(0,5)+range(2,8)+range(3,12)+[2,2]:
    print' '*(40-2*i-i//2)+'*'*(4*i+1+i)


# In[37]:

s = 'string'


# In[38]:

print type(s)


# In[39]:

print s[2]
s[2] = '0'


# In[40]:

sba = bytearray(s)
sba[3] = "o"
print sba
sba2 = sba
del sba
print sba2     #仍然存在


# In[ ]:



