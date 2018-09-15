#! /usr/bin/env python
#-*- coding: utf-8 -*-
import numpy as np
print "hello,world"
print "你好"
print np.zeros((3,3))
from sklearn.metrics.pairwise import paired_distances
#name = raw_input("what's your name? ")
#print "My name is "+name+" !"

temp = 42
print "the temperature is "+str(temp)
print "the temperature is "+`temp`
print 'greenting'[-1]
s = 'wangyong'
s1 = list(s)
print ''.join(s1)

print s1

x =  [1,4,5,3,2,6]
y = sorted(x)
x = sorted(x)
print x
print y

format = "Pi is %.3f"
from math import pi
print format % pi
d = {}
def square(x):
    'calculate the square of number x'
    return x*x

x = 10
print square(x)
print square.__doc__


import math
x = 5
y = 6
x,y = y,x
print x,y

s = [1,2,]
s2 = [3,]
s1 = s+s2
print s1

##printAll(list(quenes(4)))
import numpy
print math.__doc__
print math.__name__
a = [n for n in dir(math) if not n.startswith('_')]
#print a
print dir(numpy)
print numpy.__doc__

from heapq import *
heap = []
for i in xrange(10):
    heappush(heap,i)
print heap

import time

print time.asctime()


import sys
print sys.version

