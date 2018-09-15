#! /usr/bin/env python
#_*_ coding = utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
import pylab
data = [[1,2,3,4],[5,6,7,8]]
arr = np.array(data)
print arr.shape
print arr.dtype
num_string = np.array(['1.25','-9.6','42'],dtype = np.string_)
a = num_string.astype(float)
b = np.arange(32).reshape(8,4)
#points = np.arange(-5,5,0.01)
#xs,ys = np.meshgrid(points,points)
#print ys


#z = np.sqrt(xs**2+ys**2)
#print z
##plt.imshow(z,cmap=plt.cm.gray)
##plt.colorbar()
#plt.show()


#print points
#arr = np.random.randn(4,4)

##arr = np.where(arr>0,2,arr)
'''
a = np.random.randint(10,size=9).reshape(3,3)

b = np.array([[1,0,0],[0,1,1],[1,0,1]])
print a
print b
print np.where(b>0,0,a)
'''
nsteps = 1000
draws = np.random.randint(0,2,size=nsteps)
steps = np.where(draws>0,1,-1)
walk = steps.cumsum()

print walk.min()
print walk.max()