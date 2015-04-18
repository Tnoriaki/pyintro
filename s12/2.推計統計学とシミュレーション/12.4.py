# -*- coding: utf-8 -*-

#標準偏差

import random

def stdDev(X):
    """Xを数のリストとする
    Xの標準偏差を出力する"""
    mean = float(sum(X)) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot / len(X))**0.5 #平均との差の二乗根
