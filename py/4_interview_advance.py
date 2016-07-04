
# coding: utf-8

# Interview
# ==============

# 1 Mutable & Unmutable
# -------------
# strings,tuples, and numbers 是不可更改对象， 而list, dict是可更改对象

# In[26]:

def try_to_change_list_contents(the_list):
    print 'got', the_list
    the_list.append('four')
    print 'changed to', the_list


# In[27]:

outer_list = ['one', 'two', 'three']
print 'before: outer_list =', outer_list
try_to_change_list_contents(outer_list)
print 'after: outer_list =', outer_list


# Now try to change the referene that was passed in as a parameter:

# In[28]:

def try_to_change_list_reference(the_list):
    print 'got', the_list
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print 'set to', the_list

outer_list = ['we', 'like', 'proper', 'english']
print 'before: outer_list = ', outer_list
try_to_change_list_reference(outer_list)
print 'after: outer_list = ', outer_list


# Since the the_list parameter was passed by value, assigning a new list to it had no effect that the code outside the method could see. #The the_list was a copy of the outer_list reference#, and we had the_list point to a new list, but there was no way to change where outer_list pointed.

# String - an immutable table
# -----------------------

# It's immutable, so there's nothing we can do to change the contents of the string
# Now, let's try to change the reference

# In[29]:

def try_to_change_string_reference(the_string):
    print 'got', the_string
    the_string = 'In a kingdom ty the sea'
    print 'set to', the_string
    
outer_string = 'It was many and many a year ago'
print 'before: ,outer_string = ', outer_string
try_to_change_string_reference(outer_string)
print 'after: ,outer_string = ', outer_string


# Again, since the the_string parameter was ##passed ty value, assigning a new string to it had no effect that the code outside the method could see.

# In[30]:


def return_a_whole_new_string(the_string):
    # new_string = something_to_do_with_the_old_string(the_string)
    new_string = len(the_string)
    return new_string

# then U could call it like
my_string = 'I love you'
my_string = return_a_whole_new_string(my_string)
print my_string


# If you really wanted to avoid using a return value, you could create a class to hold your value and pass it into the funcion or use an existing class, like a list:
# 

# In[31]:

def use_a_wrapper_to_simulate_pass_by_reference(stuff_to_change):
    # new_string = something_to_do_with_the_old_string(stuff_to_change[0])
    new_string = stuff_to_change[0]
    stuff_to_change[0] = new_string
    
# then U can call it like
my_string = 'Davidyjun'
wrapper = [my_string]
use_a_wrapper_to_simulate_pass_by_reference(wrapper)
# do_something_with(wrapper[0])
print len(wrapper[0])


# ————————————————————————————————————————————————————

# 2 metaclass python中的元类

# 不常用

# ————————————————————————————————————————

# 3 @staticmethond 和 @classmethod

# In[ ]:



