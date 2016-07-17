# -*- coding: utf-8 -*-

'''
黑白球各两个，取一次涂成相反的颜色，问取多少次之后，四个球颜色能一样
'''
import numpy as np
states = ('black', 'white')
observations = ('black', 'white')
start_probability = {'black': 0.1, 'white': 0.9}
transition_pprobability = {
    'black': {'black': 0, 'white': 1},
    'white': {'black': 1, 'white': 0},
}

start_ = np.matrix([0.4, 0.6])

trans_ = np.matrix([[0, 1],
                            [1, 0]])


def trans_n(n):
    end_ = start_ * trans_ ** n
    print end_

if __name__ == '__main__':
    trans_n(11)
