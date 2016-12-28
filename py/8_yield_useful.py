
# coding: utf-8

## ***yield***

# In[14]:

def h():
    print "hello"
    yield 5


# In[15]:

h()


# as you see, when h() executed, there is a generator. OK .
# 由于函数包了yield那么这个函数已经是一个Generator

# 透过next()语句看原理
# 现在，我们来揭晓yield的工作原理。我们知道，我们上面的h()被调用后并没有执行，因为它有yield表达式，因此，我们通过next()语句让它执行。next()语句将恢复Generator执行，并直到下一个yield表达式处。比如：

# In[16]:

def h():
    print ' hahah'
    yield 5
    print 'fine!'
    
c = h()
c.next()


# In[17]:

c.next()


# In[ ]:

c.next()


# 4. send(msg) 与 next()
# 
# 了解了next()如何让包含yield的函数执行后，我们再来看另外一个非常重要的函数send(msg)。其实next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值，只能传递None进去。因此，我们可以看做
# c.next() 和 c.send(None) 作用是一样的。
# 来看这个例子：

# In[ ]:

def h():
    print 'wenaaaaaaa',
    m = yield 5
    print m
    d = yield 12
    print 'we together!'


# In[ ]:

c = h()


# In[ ]:

dir(c)
c.next()# == c.send(None)


# In[ ]:

c.send('Fighting!')


# 5. send(msg) 与 next()的返回值
# send(msg) 和 next()是有返回值的，它们的返回值很特殊，返回的是下一个yield表达式的参数。比如yield 5，则返回 5 。到这里，
# 是不是明白了一些什么东西？本文第一个例子中，通过for i in alist 遍历 Generator，其实是每次都调用了alist.Next()，
# 而每次alist.Next()的返回值正是yield的参数，即我们开始认为被压进去的东东。我们再延续上面的例子：

# In[ ]:

def h():
    print 'Wen Chuan',
    m = yield 5  # Fighting!
    print m
    d = yield 12
    print 'We are together!'

c = h()
m = c.next()  #m 获取了yield 5 的参数值 5
d = c.send('Fighting!')  #d 获取了yield 12 的参数值12
print 'We will never forget the date', m, '.', d


# 6. throw() 与 close()中断 Generator
# 中断Generator是一个非常灵活的技巧，可以通过throw抛出一个GeneratorExit异常来终止Generator。
# Close()方法作用是一样的，其实内部它是调用了throw(GeneratorExit)的。我们看：

# In[ ]:

def closeGen(self):
    try:
        self.throw(GeneratorExit)
    except(GeneratorExit, StopIteration):
        pass
    else:
        raise RuntimeError("generator ignored Generator Exit")


# In[ ]:

closeGen(h)


# In[ ]:



