# coding: utf-8

# 色と線種の詳しい指定方法
# http://matplotlib.soourceforge.net/api/pyplot_api.html
# http://matplotlib.soourceforge.net/users/customizing.html

import pylab

principal = 10000 #初期投資額
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
#pylab.plot(values) #線
#pylab.plot(values, 'ro') #赤い点群
pylab.plot(values, linewidth = 30) #太い線
pylab.title('5% Growth, Compounded Annually')
#pylab.title('5% Growth, Compounded Annually',fontsize = 'xx-large') #フォントのサイズ変更
pylab.xlabel('Years of Compounding')
#pylab.xlabel('Years of Compounding', fontsize = 'x-small') #フォントのサイズ変更
pylab.ylabel('Value of Principal ($)')
pylab.show()

#初期値

#線の太さの設定
pylab.rcParams['lines.linewidth'] = 4
#題名に使われる文字の大きさの設定
pylab.rcParams['axes.titlesize'] = 20
#軸の名前に使われる文字の大きさの設定
pylab.rcParams['axes.labelsize'] = 20
#軸の数字の大きさの設定
pylab.rcParams['xtick.labelsize'] = 16
#軸の数字の大きさの設定
pylab.rcParams['ytick.labelsize'] = 16
#軸のメモリ幅の設定
pylab.rcParams['xtick.major.size'] = 7
#軸のメモリ幅の設定
pylab.rcParams['ytick.major.size'] = 7
#マーカーの大きさの設定
pylab.rcParams['lines.markersize'] = 10
