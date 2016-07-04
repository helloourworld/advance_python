# -*- coding: utf-8 -*-
# __user__: davidyjun
'''
接例1_decorator_Learn_1.py
现在我们的salesgirl还不算合格，她只会给客人打招呼，但是客人要是买衣服了，
也不会给他报价；客人不买的话，也应该推荐其他款式！
'''


def salegirl(func):
    def serve(*args):
        print("Salesgirl: Hello, what do you want?, \
%s") % (func.__name__)
        result = func(*args)
        if result:
            print "Salesgirl: This shirt is 50$."
        else:
            print "Salesgirl: Well, how about tryiing another style?"
        return result
    return serve


@salegirl
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
result = try_this_shirt(39)
print '-' * 20
print "Mum: do you want to buy this?", result
