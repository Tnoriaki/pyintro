#coding: utf-8

import pylab

pylab.figure(1) #figure1を作成
pylab.plot([1,2,3,4], [1,2,3,4]) #figure1に作図
pylab.figure(2) #figure2を作成
pylab.plot([1,4,2,3], [5,6,7,8]) #figure2に作図
pylab.savefig('Figure-Addie') #figure2を保存
pylab.figure(1) #go back to working on figure 1
pylab.plot([5,6,10,3]) #figure1に再度作図
pylab.savefig('Figure-Jane') #figure1を保存
