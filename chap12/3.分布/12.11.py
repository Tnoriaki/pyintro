# -*- coding: utf-8 -*-

# *幾何分布*
# 幾何分布は指数分布を離散化したものである
# それは最初の成功までの必要な独立試行の回数を表す

import random
import pylab

def successfulStarts(eventProb, numTrials):
    """eventProb : 一回の試行で成功する確率を表す浮動小数点数
       numTrials : 正の整数
       各実験において,成功するまでに必要な試行の回数を出力する"""
    triesBeforeSuccess = []
    for t in range(numTrials):
        consecFailures = 0
        while random.random() > eventProb:
            consecFailures += 1
        triesBeforeSuccess.append(consecFailures)
    return triesBeforeSuccess

random.seed(0)
probOfSuccess = 0.5
numTrials = 5000
distribution = successfulStarts(probOfSuccess, numTrials)
pylab.hist(distribution, bins = 14)
pylab.xlabel('Tries Before Success ')
pylab.ylabel('Number of Occurrences Out of ' + str(numTrials))
pylab.title('Probability of Starting Each Try' + str(probOfSuccess))
pylab.show()
