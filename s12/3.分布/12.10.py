# -*- coding: utf-8 -*-

# *正規分布*
# 正規分布はrandom.gauss(mu,sigma)を実行することで、簡単に生成できる
# 平均mu,標準偏差sigmaを持つ正規分布から無作為に浮動小数点数を選んで返す
# *一様分布*
# 一様分布はrandom.uniform(min,max)を実行することで、簡単に生成できる
# minとmaxの間の浮動小数点数を無作為に選んで返す
# *ベンフォード分布*
# Sを10進数を多く含む集合とする
# 1桁目がdである可能性が P(d) = log10(1 + 1 / d) に等しい時
# Sはベンフォードの法則に等しい
# フィボナッチ数はこの法則に完全に従っている

# *指数分布*
# 指数分布はrandom.expovariateを実行することで、簡単に生成できる

# 分子の指数関数的消滅

import random
import pylab

def clear(n, p, steps):
    """n と steps は正の整数, p は浮動小数点数
    n: 分子の初期個数
    p: 分子が消失する確率
    steps: シミュレーションする長さ"""
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n * ((1 - p) ** t))
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.title('Clearance of Drug')
    pylab.figure()
    pylab.semilogy()
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.title('Clearance of Drug')

clear(1000, 0.01, 1000)
pylab.show()
                            
