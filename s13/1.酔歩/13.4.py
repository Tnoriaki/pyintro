# -*- coding: utf-8 -*-

# 酔歩

from Location import Location
from Field import Field
from Drunk import Drunk, UsualDrunk
import random

def stdDev(X):
    mean = float(sum(X)) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return (tot / len(X)) ** 0.5

def CV(X):
    mean = sum(X) / float(len(X))
    try:
        return stdDev(X) / mean
    except ZeroDivisionError:
        return float('nan')
        
def walk(f, d, numSteps):
    """f: Field クラスのオブジェクト
       d: Drunk クラスのオブジェクト
       dをnumSteps回移動し,酔歩の初期位置と最終位置との差を出力する"""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    """numSteps : 0 以上の整数
       numTrials : 正の整数
       dClass : Drunk のサブクラス
       numSteps 回移動する酔歩を, numTrials 回シミュレートする.
       各実験の初期位置と最終位置との差をリストにして出力する."""
    Homer = dClass()
    origin = Location(0.0, 0.0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(walk(f, Homer, numSteps))
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    """walkLengths : 0 以上の整数のシークエンス
       numTrials : 正の整数
       dClass : Drunk のサブクラス
       walkLengths の各要素を酔歩の移動回数として, numTrials 回の酔歩をシミュレートする simWalks を実行し, 結果を出力する."""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print dClass.__name__ , 'random walk of', numSteps, 'steps'
        print 'Mean =', sum(distances) / len(distances),'CV =', CV(distances)
        print ' Max =', max(distances), 'Min =', min(distances)
        
drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
