#coding: utf-8

# ハッシュ表
 
class intDict(object):
    """整数をキーとする辞書"""
    
    def __init__(self, numBuckets):
        """空の辞書を生成する"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
    
    def addEntry(self, dictKey, dictVal):
        """dictKeyをint型とし、エントリを追加する"""
        hashBucket = self.buckets[dictKey % self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] == (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))
        
    def getValue(self, dictKey):
        """dictKeyをint型とする
        キーをdictKeyに関連付けられたエントリを返す"""
        hashBucket = self.buckets[dictKey % self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None

    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'
        
import random

D = intDict(29)
for i in range(20):
    #0から10**5までの整数をランダムに選ぶ
    key = random.randint(0, 10**5)
    D.addEntry(key, i)

print 'The value of the intDict is:'
print D
print '\n', 'The buckets are:'
for hashBucket in D.buckets: #抽象化の壁
    print '  ',hashBucket
    
