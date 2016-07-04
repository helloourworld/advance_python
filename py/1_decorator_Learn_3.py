# -*- coding: utf-8 -*-
# __user__: davidyjun
'''
接例1_decorator_Learn_2.py
 单个 Decorator，带参数
　　会报价并且带折扣的salesgirl：
'''


def salegirl(discount):
    def expense(func):
        def serve(*args):
            print("Salesgirl: Hello, what do you want?, \
%s") % (func.__name__)
            result = func(*args)
            if result:
                print "Salesgirl: This shirt is 50$. As an old user, we promised to discount at %d%%" % (discount)
            else:
                print "Salesgirl: Well, how about tryiing another style?"
            return result
        return serve
    return expense


@salegirl(20)
def try_this_shirt(size):
    if size < 35:
        print "I: %d inches is to small to me" % (size)
        return False
    elif size > 38:
        print "I: %d inches is to large to me" % (size)
        return False
    else:
        print "I: %d inches is just enough" % (size)
        return True


print '+' * 20
result = try_this_shirt(32)
print '-' * 20
print "Mum: do you want to buy this?", result
print '+' * 20
result = try_this_shirt(36)
print '-' * 20
print "Mum: do you want to buy this?", result
print '+' * 20
result = try_this_shirt(39)
print '-' * 20
print "Mum: do you want to buy this?", result
