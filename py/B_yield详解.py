
# coding: utf-8

# ## Iterables

# **任何可以用 for in 来迭代读取的都是迭代容器，例如lists,strings,files.这些迭代器非常的便利，因为你可以想取多少便取多少，但是你得存储所有的值，其中很多值都完全没有必要每次都保持在内存中。**

# In[1]:

# ex1
mylist = [x*x for x in xrange(3)]
for each in mylist: print each
for each in mylist: print each,


# ## Generators

# Generators(生成器)也是可迭代的，但是你每次只能迭代它们一次，因为不是所有的迭代器都被一直存储在内存中的，他们临时产生这些值：

# In[2]:

# ex2
mygenerator = (x*x for x in xrange(3))
for each in mygenerator: print each
for each in mygenerator: print each,
print "I was tired out"


# 生成器几乎和迭代器是相同的，除了符号[]变为()。但是你无法用两次，因为他们只生成一次：他们生成0然后丢弃，继续统计1，接着是4，一个接着一个。

# ## Yield
# 
# Yield的用法有点像return,除了它返回的是一个生成器，例如：

# In[3]:

def createGenerator():
    mylist = xrange(3)
    for i in mylist:
        yield i*i


# In[4]:

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
for i in mygenerator:
    print(i)


# createGenerator()生成的是一个生成器。

# 为了掌握yield的精髓，你一定要理解它的要点：当你调用这个函数的时候，你写在这个函数中的代码并没有真正的运行。这个函数仅仅只是返回一个生成器对象。有点过于奇技淫巧:-)
# 
# 然后，你的代码会在每次for使用生成器的时候run起来。
# 
# 现在是解释最难的地方：
# 当你的for第一次调用函数的时候，它生成一个生成器，并且在你的函数中运行该循环，直到它生成第一个值。然后每次调用都会运行循环并且返回下一个值，till没有值返回为止。该生成器被认为是空的一旦该函数运行但是不再yield。之所以如此是因为该循环已经到达终点，或者是因为你再也不满足“if/else”的条件。

# In[5]:

class Bank(): # let's create a bank, building ATMs
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$1000"


# In[6]:

hsbc = Bank() # when everything's ok the ATM gives you as much as you want


# In[7]:

corner_street_atm = hsbc.create_atm()


# In[8]:

print(corner_street_atm.next())


# In[9]:

print(corner_street_atm.next())


# In[10]:

print([corner_street_atm.next() for cash in range(5)])


# In[11]:

print list(corner_street_atm.next() for cash in range(5))


# In[12]:

hsbc.crisis = True # crisis is coming, no more money!


# In[13]:

print corner_street_atm.next()


# In[14]:

wall_street_atm = hsbc.create_atm() # it's even true for new ATMs


# In[15]:

print(wall_street_atm.next())


# In[16]:

hsbc.crisis = False # trouble is, even post-crisis the ATM remains empty


# In[17]:

print(corner_street_atm.next())


# In[18]:

brand_new_atm = hsbc.create_atm() # build a new one to get back in business


# ## Itertools模块

# Itertools模块包含一些特别的函数去执行迭代器。有没有想过去复制一个生成器 或者链接两个生成器?等等。
# 引入itertools就好了，import itertools.
# 下面举个例子.看看四匹马到达先后顺序的例子：

# In[19]:

import itertools
horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)


# In[20]:

print(list(itertools.permutations(horses)))


# 最后是理解迭代器的内部机制：
# Iteration is a process implying iterables (implementing the __iter__() method) and iterators (implementing the __next__() method). Iterables are any objects you can get an iterator from. Iterators are objects that let you iterate on iterables.

# In[ ]:



