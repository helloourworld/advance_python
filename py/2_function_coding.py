
# coding: utf-8

## 求和问题 命令式 函数式 对象式

# 命令式

#  x=1 y = 2 求 x和y的和
# 求 x和y的平方的和
# 求 x的m次方与n次方的和

# In[1]:

# 命令式
def sum1(x, y):
    return x + y
def sum2(x, y):
    return x ** 2 + y ** 2
def sum3(x, y, m, n):
    return x ** m + y ** n


# In[2]:

print sum1(1, 2)
print sum2(1, 2)
print sum3(1, 2, 3, 4)


# In[3]:

# 对象式
class Sum:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def sum(self, m=1, n=1):
        return self.x ** m + self.y ** n
    
    
S = Sum(1, 2)
print S.sum()
print S.sum(2, 2)
print S.sum(3, 4)


# In[4]:

# 函数式
def sum(x, y, f, g):
    return f(x) + g(y)

def f1(x):
    return x
def f2(x):
    return x**2
def f3(x):
    return x**3
def f4(x):
    return x**4



# In[5]:

sum(1, 2, f1, f1)


# In[6]:

sum(1, 2, f2, f2)


# In[7]:

sum(1, 2, f3, f4)


# In[8]:

# function_coding
def sum(x, y, f, g):
    return f(x) + g(y)

def generate_func(k):
    def func(x):
        return x**k
    return func


# In[9]:

sum(1, 2, generate_func(1), generate_func(1))


# In[10]:

sum(1, 2, generate_func(2), generate_func(2))


# In[11]:

sum(1, 2, generate_func(3), generate_func(4))


# In[12]:

def gen_func(x):
    def func(k):
        return x ** k
    return func


# In[13]:

sum(1, 2, gen_func(3), gen_func(4))


# In[14]:

def gen_func2(m, n):
    def func(x):
        return (x/m) ** n
    return func

sum(6, 6, gen_func2(3,4),gen_func(1))


# In[15]:

sum(6, 6, gen_func2(3,4), generate_func(1))


# 3.1 高阶函数 Higher-order Function
# ===

# generate_func可以动态生成函数，无需人工蛮力定义，省时省力，最大的好处是生成的函数有无限个，这是人工所不及的。

# 高阶函数就是generate_func这样的函数，要么输入中至少有一个函数，要么输出一个函数，至少满足两个条件中的一个。何谓高阶？高阶函数比普通的函数高阶。

# 为什么高阶函数更牛逼？有一个词叫"泛化",是从具体到抽象，抽象可以让我们站在更高的位置看待这芸芸众生，然后悟出人生。什么模块化、面象对象、设计模式blabla，都不是在追求抽象，追求“泛”吗？从一个函数生成无数个函数，不就是一生二二生三嘛！

# 所以高阶函数实至名归。高阶函数在数学中也叫做算子（运算符)或泛函。

# 3.2 闭包（Closure)
# =================
# 当我们使用高阶函数来生成函数的时候，可以使用以下两种方法。方法一是将要生成的函数f写在高阶函数gen_f内部； 方法二是将f写在外部。通常我们使用第一种，这就和定义局部变量差不多，在哪用就在哪定义，减少对外干扰。

# In[16]:

# method1
def gen_f():
    def f():
        pass
    return f


# In[17]:

# method2
def f():
    pass
def gen_f():
    return f


# In[18]:

# method1
def gen_f():
    array = []
    def f():
        array.append(1)
        return array
    return f
func = gen_f()
func() # [1]


# In[19]:

func() #[1, 1]


# In[20]:

func() #[1, 1, 1]


# 预料之外，情理之中，f就是闭包函数。func作为生成出来的函数，每次调用时都会往array里放一个数字1， 而array是在外部gen_f中定义的。这时就需要作出选择，是修改外部的array还是抛出一个找不到array的错误。支持闭包特性的编程语言选择的是前者。
# 
# 闭包函数和其引用变量将一同存在，所以有另一种说法认为闭包是由函数和其相关的引用环境组合而成的实体。

# 3.3 柯里化（currying）
# ======
# 如果我们习惯了生成函数的快感，也很有可能写出以下代码。方法一和方法二都实现了同样的功能。

# In[21]:

# method1
# 每次只传一个参数
def f(x):
    def g(y):
        def h(z):
            return x + y + z
        return h
    return g
f(1)(2)(3) # 6


# In[22]:

# method2 
# 一次把所有参数传进去
def f(x,y,z):
    return x + y + z
f(1, 2, 3)


# 从方法二到方法一的变化成为柯里化，即把接受多个参数的函数的函数变成每次只接受一个参数的函数，并返回余下参数的函数。有点拗口，就是通过多次调用函数来代替一次传入多个参数。

# 柯里化的优势在于可以将抽象的函数具体化，比如打印日志。

# In[24]:

from django.utils.functional import curry
def print_msg(label, msg):
    print '[%s] %s' % (label, msg)
    
# no currying
print_msg('error', 'network failed')
print_msg('info', 'init ok')

# use currying
print_err_msg = curry(print_msg)('error')
print_info_msg = curry(print_msg)('info')
print_info_msg('init ok')
print_err_msg('network failed')
# 其中curry表示将输出的函数柯里化


# 3.4 偏函数Partial Function
# ===
# python没有提供curry函数。
# python 的内置functools模块提供了类似curry的功能，名曰偏函数。

# In[ ]:

from functools import partial

def print_msg(label, msg):
    print '[%s] %s' % (label, msg)
    
# use partial
print_err_msg = partial(print_msg, 'error')
print_info_msg = partial(print_msg, 'info')

print_err_msg('network failed')
print_info_msg('init ok')


#     柯里化和偏函数类似但不同，柯里化是将多参数函数转变为一系列单参数函数的链式调用，而偏函数是事先固定好一部分参数后面就无需重复传入了。两者都可能实现函数的具体化，固定函数的一部分参数来达到特定的应用。

# 3.5 匿名函数
# ==

# In[ ]:

def sum(x, y, f, g):
    return f(x) + g(y)

sum(1, 2, lambda x: x, lambda x: x)


# In[ ]:

sum(1, 2, lambda x: x**2, lambda y: y**2)


# In[ ]:

sum(1, 2, lambda x: x**3, lambda z: z**4)


# lambda 绝色无污染 干净利索

# 3.6 map reduce filter
# ==========
# 
# map reduce filter 是Python内置的高阶函数，通过传入函数可实现某些特定的功能，通过用这些函数可以让代码更加简洁，逼格更高

# In[ ]:

array = [1, 2, 3]
### [1,2,3] 变换为 【1*1， 2*2， 3*3】 
# good
map(lambda x: x*x, array) # [1, 4, 9]


# In[ ]:

map(lambda x: x ** 2, array)


# In[ ]:

### 求[1,2,3]元素的和
# good
reduce(lambda x,y: x+y, array) # 6


# In[ ]:

reduce(lambda x,y: x*y, array)


# In[ ]:

# 求[1,2,3]中的奇数
# good
filter(lambda x: x%2, array)


# In[ ]:



