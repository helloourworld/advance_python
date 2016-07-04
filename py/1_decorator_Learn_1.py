# -*- coding: utf-8 -*-
'''
设想一个情景，你平时去买衣服的时候，跟售货员是怎么对话的呢？售货员会先向你问好，然后你会试穿某件你喜爱的衣服。
'''


def salesgirl(method):
    def serve(*args):
        print "Salesgirl:Hello, what do you want?", method.__name__
        method(*args)
    return serve


@salesgirl
def try_this_skirt(color):
    if color in ['black', 'white']:
        print "I: %s is not suit to me" % (color)
    else:
        print "I: %s is suit to me" % (color)


@salesgirl
def try_this_shirt(size):
    if size < 35:
        print "I: %d inches is to small to me" % (size)
    else:
        print "I:%d inches is just enough" % (size)

try_this_shirt(20)
try_this_shirt(45)
try_this_skirt('blue')
try_this_skirt('white')
