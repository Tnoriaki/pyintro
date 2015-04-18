# -*- coding: utf-8 -*-

# エラーバー入りのプロットを作成

import random
import pylab

def stdDev(X):
    """Xを数のリストとする
    Xの標準偏差を出力する"""
    mean = float(sum(X)) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot / len(X))**0.5 #平均との差の二乗根

def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads / numFlips

def flipSim(numFlipsPerTrials, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrials))
    mean = sum(fracHeads) / len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean, sd)

def showErrorBars(minExp, maxExp, numTrials):
    """minExp と maxExp は minExp < maxExp を満たす正の整数,
    numTrials は正の整数とする
    表の割合の平均を誤差棒付きでプロットする"""
    means, sds = [], []
    xVals = []
    for exp in range(minExp, maxExp + 1):
        xVals.append(2 ** exp)
        fracHeads, mean, sd = flipSim(2 ** exp, numTrials)
        means.append(mean)
        sds.append(sd)
    pylab.errorbar(xVals, means, yerr = 2 * pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean Fraction of Heads (' + str(numTrials) + 'trials)')
    pylab.xlabel('Number of flips per trial')
    pylab.ylabel('Fraction of heads & 95% confidence')
    
random.seed(0)
#makePlots(100,1000,100000)
showErrorBars(3,10,100)
pylab.show()
