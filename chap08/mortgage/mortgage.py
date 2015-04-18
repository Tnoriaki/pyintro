# coding: utf-8

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
        
