# -*- coding: utf-8 -*-

# コイン投げのシミュレーション

import pylab
import random

def stdDev(X):
    """Xを数のリストとする
    Xの標準偏差を出力する"""
    mean = float(sum(X)) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot / len(X))**0.5 #平均との差の二乗根

def CV(X):
    """Xを数のリストとする
    Xの変動係数を出力する"""
    mean = sum(X) / float(len(X))
    try:
        return stdDev(X) / mean
    except ZeroDivisionError:
        return float('nan')
        
def makePlot(xVals, yVals, title,  xLabel, yLabel, style, logX = False, logY = False):
    """xValに対するyValsの値を、題名と軸名入りでプロットする"""
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
        if logY:
            pylab.semilogy()
    
def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.random() < 0.5:
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)

def flipPlot1(minExp, maxExp, numTrials):
    """minExp と maxExp は minExp < maxExp を満たす正の整数
    numTrials は正の整数とする
    2**minExp から 2**maxExp 回のコイン投げを numTrials 回行った結果の要約をプロットする"""
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    ratiosCVs, diffsCVs = [], []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios =  []
        diffs = []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads / float(numTails))
            diffs.append(abs(numHeads - numTails))
        ratiosMeans.append(sum(ratios) / float(numTrials))
        diffsMeans.append(sum(diffs) / float(numTrials))
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        ratiosCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))
    numTrialsString = ' (' + str(numTrials) + ' Trials)'
    title = 'Mean Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosMeans, title,
             'Number of flips', 'Mean Heads/Tails', 'bo', logX = True)
    title = 'SD Heads/Tails' + numTrialsString
    makePlot(xAxis, ratiosSDs, title,
             'Number of Flips', 'Standard Deviation', 'bo', logX = True, logY = True)

    title = 'Mean abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsMeans, title,
         'Number of Flips ', 'Mean abs(#Heads = #Tails)', 'bo', logX = True, logY = True)
    title = 'SD abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsSDs, title,
         'Number of Flips', 'Standard Deviation', 'bo', logX = True, logY = True)
    title = 'Coeff. of Var. abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsCVs, title, 'Number of Flips',
             'Coeff. of Var. ', 'bo', logX = True)
    title = 'Coeff. of Var. Heads/Tails Ratio' + numTrialsString
    makePlot(xAxis, ratiosCVs, title, 'Number of Flips',
             'Coeff. of Var. ', 'bo', logX = True, logY = True)

flipPlot1(4,20,20)    
pylab.show()
