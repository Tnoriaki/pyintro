# -*- coding: utf-8 -*-

# 最終地点のプロット

from Location import *
from Field import *
from Drunk import *
from styleIterator import *
import pylab

def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    origin = Location(0,0)
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, origin)
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('b+', 'r^', 'mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for I in locs:
            xVals.append(I.getX())
            yVals.append(I.getY())
        meanX = sum(xVals) / float(len(xVals))
        meanY = sum(yVals) / float(len(yVals))
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle, 
                   label = dClass.__name__ + ' Mean loc. = <'
                   + str(meanX) + ', ' + str(meanY) + '>')
        pylab.title('Location at End of Walks (' + str(numSteps) + ' steps)')
        pylab.xlabel('Steps East/West of Origin')
        pylab.ylabel('Steps North/South of Origin')
        pylab.legend(loc = 'lower left', numpoints = 1)

plotLocs((UsualDrunk, ColdDrunk, EWDrunk), 100, 200)        
pylab.show()
