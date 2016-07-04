
# coding: utf-8

# In[1]:

Lord_of_ring = ['Ainur','Dragons','Dwarves','Elves','Ents','Hobbits','Men','Orcs']

for idx,element in enumerate(Lord_of_ring):
    Lord_of_ring[idx] ="{0}:{1}".format(idx,element)

print Lord_of_ring


# In[2]:

print type(Lord_of_ring)


# In[3]:

Lord_of_ring_dict = {idx: element for idx,element in enumerate(Lord_of_ring)}


# In[4]:

print Lord_of_ring_dict


# In[5]:

test =['Ainur','Dragons','Dwarves','Elves','Ents','Hobbits','Men','Orcs']

def _trans(idx,element):
    return '{0}:{1}'.format(idx,element)
print [_trans(idx,element) for idx,element in enumerate(test)]

print ['{0}:{1}'.format(idx,element) for idx,element in enumerate(test) ]


# In[6]:

import collections

print isinstance("H", collections.Iterable)
print isinstance(test, collections.Iterable)


# In[7]:

language={"Scala":"Martin Odersky",          "Clojure":"Richy Hickey",          "C":"Dennis Ritchie",          "Standard ML":"Robin Milner"}

['{0:<15} created by {1:<15}'.format(la,ua) for la,ua in language.iteritems()]


# In[8]:

# 多重解析
print [(x+1,y+1) for x in xrange(4) for y in xrange(4)]
print [(x+1,y+1) for x in xrange(4) for y in xrange(4) if y<x]
print [(x+1,y+1) for x in xrange(4) for y in xrange(x)]


# In[9]:

# 使用小括号做Comprehension返回生成器对象，占用O(1)内存空间
num = range(1,20)
simple_generator = (x ** 2 for x in num if x > 0)
print simple_generator


# In[10]:

for e in simple_generator:
    print e,


# In[11]:

# 使用小括号解析并不会返回一个不可变元组而是生成器，是一个需要强记的规则；然而大括号解析式就普通了许多。
x = range(10)

print { i for i in x if i%2==0 }
print { idx:i**2 for idx,i in enumerate(x) if i%2==0 }


# In[12]:

#花样传参：zip与星号操作


# In[13]:

# zip: 拉链函数
# *: 经常和zip在一起，用于传递参数。
# **: 用于传递关键字型参数


# In[14]:

# enumerate: 返回生成器，生成器每次给出下标和Iterable的内容
# sorted: 返回列表，可以进行排序
# zip: 把多个长度相同的列表当成数据列组成的数据表，返回一个包含着元组的列表，每个元组是数据表中的一行


# In[15]:

war3_char = ['Orc','Humans','Undead','Night Elves']
dota_hero = ['Blade Master','Archmage','Death King','Demon Hunter']
Your_choice=zip(war3_char,dota_hero)
print Your_choice


# In[16]:

# 取回原来的列表：
choice1,choice2,choice3,choice4 = Your_choice
print zip(choice1,choice2,choice3,choice4)


# In[17]:

# 用*把Your_choice的内容而不是它本身作为参数传递
print zip(*Your_choice)
# * 告诉Python即将传入的参数Your_choice不是单独一个序列，而是把Your_choice中的每一项作为参数


# In[18]:

Base_Damage={'Blade Master':48,'Death King':65,'Tauren Chieftain':51}


# In[19]:

max_Damage = max(zip(Base_Damage.itervalues(), Base_Damage.iterkeys()))
print max_Damage


# In[20]:

min_Damage = min(zip(Base_Damage.iterkeys(), Base_Damage.itervalues()))
print min_Damage


# In[21]:


# 花样传参

def triplesum(a,b,c):
    return a * 100 + b * 10 + c

print triplesum(1,2,3)


# In[22]:

# 带默认值的参数叫keyword arguments(kargs):

def triplesum_default(a=0,b=0,c=1):
    return a * 100 + b * 10 + c

print triplesum_default(*[1,2,3])
print triplesum_default(*[1,3])
print triplesum_default(**{'b':2,'c':3,'a':1})
print triplesum_default(**{'c':3,'a':1})


# In[23]:

#深浅拷贝：关系到变量的正确修改与复制
#变量的属性：
#身份：就像身份证（或者内存地址）那样，id()
#属性：表示变量的类型，type()或者isInstance()确认
#值：这个地址存的数据，通过与名字绑定的方法来读取


# In[24]:

import math
print math.log(10, 100)


# In[25]:

print math.log(100,math.e)


# In[26]:

def ind(a, e):
    return (a-e) * math.log((a*0.01/(e*0.01)),e)

act = [19, 21,29]
exp = [18, 30, 30]

ainde = map(ind, act, exp)
print ainde


# In[26]:



