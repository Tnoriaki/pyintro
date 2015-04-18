# -*- coding: utf-8 -*-

# ワールドシリーズの適切な長さを知るためのシミュレーション

import random
import pylab

def playSeries(numGames, teamProb):
    """numGames は奇数, teamProb は 0 から 1 までの浮動小数点数
    優勢なチームが優勝した時は,Trueを返す"""
    numWon = 0
    for game in range(numGames):
        if random.random() <= teamProb:
            numWon += 1
    return (numWon > numGames // 2)

def findSeriesLength(teamProb):
    numSeries = 200
    maxLen = 2500
    step = 10
    def fracWon(teamProb, numSeries, seriesLen):
        won = 0.0
        for series in range(numSeries):
            if playSeries(seriesLen, teamProb):
                won += 1
        return won / numSeries

    winFrac = []
    xVals = []
    for seriesLen in range(1, maxLen, step):
        xVals.append(seriesLen)
        winFrac.append(fracWon(teamProb, numSeries, seriesLen))
    pylab.plot(xVals, winFrac, linewidth = 5)
    pylab.xlabel('Length of Series')
    pylab.ylabel('Probability of Wining Series ')
    pylab.title(str(round(teamProb, 4)) + 'Probability of Better Team Winning a Game')
    pylab.axhline(0.95) # y = 0.95 で水平な直線を描く

YanksProb = 0.636
PhilsProb = 0.574
findSeriesLength(YanksProb / (YanksProb + PhilsProb))
pylab.show()

            
