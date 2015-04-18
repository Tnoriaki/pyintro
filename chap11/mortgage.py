#coding: utf-8

import pylab

def findPayment(loan, r, m):
    """loatとrをfloat型とし、mをint型とする
    月割りの金利をrとして、借入額loanの住宅ローンを
    mヶ月で返済する場合の、毎月の返済額を返す"""
    return loan*((r*(1+r)**m)/((1+r)**m-1))

class Mortgage(object):
    """異なる種類の住宅ローンを構築するための抽象クラス"""
    def __init__(self, loan, annRate, months):
        """新たに住宅ローンを生成する"""
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None #住宅ローンの種類(サブクラスで用いる)

    def makePayment(self):
        """返済を行う"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)

    def getTotalPaid(self):
        """これまでに支払った総額を返す"""
        return sum(self.paid)
    
    def __str__(self):
        return self.legend

    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)

    def plotBalance(self, style):
        pylab.plot(self.owed, style, label = self.legend)

    def plotTotPd(self, style):
        """これまでに支払った総額のプロットをする"""
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, style, label = self.legend)

    def plotNet(self, style):
        """住宅ローンの総費用の近似値を時系列的にプロットする。
        具体的には、総支払額からローンの返済によって得た純資産額を減じたものをプロットする"""
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        #支払いによって得る総資産額とは、ローンの総額からローン残高を減じたもの
        equityAcquired = pylab.array([self.loan]*len(self.owed))
        equityAcquired = equityAcquired - pylab.array(self.owed)
        net = pylab.array(totPd) - equityAcquired
        pylab.plot(net, style, label = self.legend)
        
