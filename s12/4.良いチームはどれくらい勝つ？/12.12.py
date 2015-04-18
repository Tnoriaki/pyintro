# -*- coding: utf-8 -*-

# ワールドシリーズのシミュレーション
# メジャーリーグの2チームがどちらかが4回勝つまで,繰り返し試合を行い,勝ったチームは
# ワールドチャンピオンと呼ばれる
# 多くとも7回の対戦でチームの優劣を決めることは妥当なのか？

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

def simSeries(numSeries):
    prob = 0.5
    fracWon = []
    probs = []
    while prob <= 1.0:
        seriesWon = 0.0
        for i in range(numSeries):
            if playSeries(7, prob):
                seriesWon += 1
        fracWon.append(seriesWon / numSeries)
        probs.append(prob)
        prob += 0.01
    pylab.plot(probs, fracWon, linewidth = 5)
    pylab.xlabel('Probability of Winning a Game')
    pylab.ylabel('Probability of Winning a Series')
    pylab.axhline(0.95)
    pylab.ylim(0.5, 1.1)
    pylab.title(str(numSeries) + ' Seven-Game Series ')

simSeries(400)
pylab.show()

