
# coding: utf-8

# In[1]:

for i in xrange(5):
    if i > 3:
        break
    else:
        print i,
else:
    print "Expectedly Finished"


# In[6]:

your_salary = 35000
your_location = "Beijing"
if your_salary > 100000:
    print "(￣￣︶)> []"
elif your_salary >= 25000:
    print "<(￣︶￣)/*"
else:
    print "(￣﹏￣) (￣ˇ￣)"


# In[7]:

x,y = 111,17
if x < y:
    smaller = x
else:
    smaller = y
print smaller


# In[8]:

smaller = x if x < y else y
print smaller


# In[9]:

x , y  = 3 , 5
smaller =  x < y and x or y
print smaller

x , y  = 5 , 3
smaller =  x < y and x or y
print smaller


# In[10]:

x , y  = 0 , 5 
smaller =  x < y and x or y
print smaller


# In[12]:

x , y  = 0.12 , 5 
smaller =  x and x < y  or y
print smaller


# In[13]:

print range(10)
print range(1,5,1)
print range(5,1,-1)
for i in xrange(10):
    print i ** 2,


# In[14]:

s = 'string'


# In[15]:

for each in s:
    print each


# In[18]:

for each in s:
    print each,


# In[25]:

a = 'Be Enumerated'
b = len(a)
for eachnum in range(b):
    print a[eachnum], "{0}".format(float(eachnum))


# In[26]:

for eachnum,item in enumerate(a):
    print eachnum,item


# In[28]:

count = 0
while count <= 3:
    print "looping {0}".format(count)
    count += 1
    print count
else:
    print "Finite Loop, {0}".format(count)

count = 0
while True:
    print "looping {0}".format(count)
    count += 1
    print count
    if count > 3:
        break
else:
    print "Broken Loop"


# In[29]:

for i in xrange(3):
    print i
else:
    print "Finished"
print '='*20
for i in xrange(3):
    if i > 1:
        break
    print i
else:
    print "Finished"


# In[30]:

a = [1, 0, 2, 4]
for element in a:
    if element == 0:
        continue
    print 1. / element


# In[31]:

z = 1 + 1j
while True:
    if abs(z) > 100:
        break
    z = z ** 2 + 1
    print z


# In[32]:

print (-11 -16j) ** 2


# In[33]:

print (-135 + 352j) ** 2


# In[34]:

print (-105679 - 95040j) ** 2


# In[35]:

L = ['red', 'blue', 'green', 'black', 'white']


# In[36]:

print isinstance(L, list)
print L[0], L[-1]
print L[2:4]
print L[:3], L[::2]


# In[37]:

M = ['red','blue','green','black','white',42,True]  # 列表中可以包含不同类型的元素
M[2:4] = ['Ruby','sapphire']
N = M
M[-1] = False                                     # 可以通过切片修改
print N                                           # 可变类型的特点，不直接操作N，N内容被改变


# In[38]:

print M


# In[39]:

LM = ['red','blue','green','black','white']
LM.append('pink')                          # 列表尾部添加一个元素
popped = LM.pop()                           # 删除并返回列表最后一个元素
#试试LM.pop(0)
LM.extend(['pink','purple','purple'])       # 讲extend后的序列添加到列表中，extend后的内容应该是可迭代的
LM.remove('purple')                       # 删除指定值的一个元素
print LM
print popped


# In[40]:

print LM[::-1]


# In[41]:

print LM.reverse


# In[42]:

LL = LM.reverse
print LL


# In[43]:

print LM


# In[44]:

print LM * 2


# In[45]:

print LM + LM


# In[46]:

LL_Law = M.sort
print LL_Law


# In[47]:

sorted(M)


# In[48]:

LL_law = ['red', 'blue', 'Ruby', 'sapphire', 'white', 42, False]
my_precious = "silmarils"
print my_precious in LL_law
if "Ruby" in LL_law:
    print "Ok"


# In[49]:

string = 'Mukatsuku'
ls_str = list(string)
print ls_str


# In[ ]:




# In[50]:

war3 = ('Orc','Humans','Undead','Night Elves')
heros = 'Blade Master','Farseer','Tauren Chieftain','Shadow Hunter'


# In[51]:

war3copy = war3
print war3copy
del war3copy
print war3copy


# In[52]:

t = (42,False,[True],-203+1j)
t[2][0] = False


# In[53]:

print t


# In[54]:

print list(t)


# In[55]:

war3 = ('Orcs','Humans','Undead','Night Elves')
Lord_of_ring = ('Ainur','Dragons','Dwarves','Elves','Ents','Hobbits','Humans','Orcs')
test_set = set(war3)
train = set(Lord_of_ring)
ya_test_set = {'Orcs','Humans','Undead','Night Elves'}


# In[56]:

print 'Orcs' in test_set


# In[57]:

print 'Orcs' in train


# In[59]:

print 'Orcs' in ya_test_set


# In[60]:

test_set.add('Xmen')


# In[61]:

print test_set


# In[62]:

test_set.update(['No.16', 'No.17', 'No.18'])
print test_set


# In[63]:

for item in ['Xmen', 'No.16', 'No.17', 'No.18']:
    test_set.remove(item)
print test_set


# In[64]:

ftest = frozenset(test_set)
print ftest
ftest.add('Xmen')


# In[65]:

print test_set==train   #判断是否相等
print test_set<train    #判断是否是子集
print test_set>train    #判断是否是超集
print test_set&train    #求交集
print test_set|train    #求并集
print train-test_set    #求差集
print test_set^train    #求异或

print test_set^train == ((train-test_set) | (test_set-train))
rint test_spet^train == (train | test_set) - (train & test_set)


# In[66]:

print test_set^train


# In[67]:

language={"Scala":"Martin Odersky","Clojure":"Richy Hickey","C":"Dennis Ritchie","Standard ML":"Robin Milner"}


# In[68]:

print language.keys() #key


# In[69]:

print language.values() #value


# In[70]:

print language.items() #item


# In[71]:

print language.iterkeys()  #取得上述内容的iterable


# In[72]:

print language.itervalues()


# In[73]:

print language.iteritems()


# In[74]:

# 迭代器
for key in language:
    print 'key={0}, value={1}'.format(key,language[key])


# In[75]:

language.get("Haskell","They hardly understand IT")


# In[ ]:



