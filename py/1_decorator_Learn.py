
# coding: utf-8

# Decoator
# ======
# 
# http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html

# >1 最简单的函数，准备附加额外功能：

# In[1]:


'''示例1: 最简单的函数,表示调用了两次'''
 
def myfunc():
    print("'myfunc' called.")
 
myfunc()
myfunc()


# >2使用装饰函数在函数执行前和执行后分别附加额外功能

# In[2]:


'''示例2: 替换函数(装饰)
装饰函数的参数是被装饰的函数对象，返回原函数对象
装饰的实质语句: myfunc = deco(myfunc)'''
 
def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func
 
def myfunc():
    print(" This is myfunc() called.")
 
myf = deco(myfunc)
print("****")
myf()
print("******")
myf()


# >3使用语法糖@来装饰函数

# In[3]:


'''示例3: 使用语法糖@来装饰函数，相当于“myfunc = deco(myfunc)”
但发现新函数只在第一次被调用，且原函数多调用了一次'''
 
def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func
 
@deco
def myfunc():
    print(" myfunc() called.")
print("***") 
myfunc()
print("***")
myfunc()


# >4使用内嵌包装函数来确保每次新函数都被调用

# In[4]:


'''示例4: 使用内嵌包装函数来确保每次新函数都被调用，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''
 
def deco(func):
    print 'Start:'
    def _deco():
        print("before myfunc() called.",'%s' % (func.__name__))
        func()
        print("  after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco
 
@deco
def myfunc():
    print(" myfunc() called.")
    return 'ok'
 
print("***") 
myfunc()
print("***")
myfunc()


# >5对带参数的函数进行装饰

# In[5]:


'''示例5: 对带参数的函数进行装饰，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''
 
def deco(func):
    def _deco(a, b):
        print("before myfunc() called.", func.__name__)
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret
    return _deco
 
@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b
 
myfunc(1, 2)
myfunc(3, 4)


# >6对参数数量不确定的函数进行装饰

# In[6]:


'''示例6: 对参数数量不确定的函数进行装饰，
参数用(*args, **kwargs)，自动适应变参和命名参数'''
 
def deco(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco
 
@deco
def myfunc1(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a+b
 
@deco
def myfunc2(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a+b+c
print '***'
myfunc1(1, 2)
print '****'
myfunc1(3, 4)
print '*****'
myfunc2(1, 2, 3)
print '******'
myfunc2(3, 4, 5)


# >7让装饰器带参数

# In[7]:


'''示例7: 在示例4的基础上，让装饰器带参数，
和上一示例相比在外层多了一层包装。
装饰函数名实际上应更有意义些'''
 
def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("  after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco
 
@deco("mymodule")
def myfunc():
    print(" myfunc is called.")
 
@deco("module2")
def myfunc2():
    print(" myfunc2 is called.")
print '*****'
myfunc()
print '***'
myfunc2()


# >8让装饰器带 类 参数
# 

# In[8]:


'''示例8: 装饰器带类参数'''
 
class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")
         
    @staticmethod
    def acquire():
        print("locker.acquire() called.（这是静态方法）")
         
    @staticmethod
    def release():
        print("  locker.release() called.（不需要对象实例）")
 
def deco(cls):
    '''cls 必须实现acquire和release静态方法'''
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco
 
@deco(locker)
def myfunc():
    print(" myfunc() called.")
print '1\n',
myfunc()
print '2'
myfunc()


# >9装饰器带类参数，并分拆公共类到其他py文件中，同时演示了对一个函数应用多个装饰器

# In[9]:


'''mylocker.py: 公共类 for 示例9.py'''

class mylocker:
    def __init__(self):
        print("mylocker.__init__() called.")
        
    @staticmethod
    def acquire():
        print("mylocker.acquire() called.")
        
    @staticmethod
    def unlock():
        print("  mylocker.unlock() called.")

class lockerex(mylocker):
    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")
        
    @staticmethod
    def unlock():
        print("  lockerex.unlock() called.")

def lockhelper(cls):
    '''cls 必须实现acquire和release静态方法'''
    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()
        return __deco
    return _deco


# In[10]:


'''示例9: 装饰器带类参数，并分拆公共类到其他py文件中
同时演示了对一个函数应用多个装饰器'''

# from mylocker import *

class example:
    @lockhelper(mylocker)
    def myfunc(self):
        print(" myfunc() called.")

    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def myfunc2(self, a, b):
        print(" myfunc2() called.")
        return a + b

if __name__=="__main__":
    a = example()
    a.myfunc()
    print(a.myfunc())
    print(a.myfunc2(1, 2))
    print(a.myfunc2(3, 4))


# In[10]:



