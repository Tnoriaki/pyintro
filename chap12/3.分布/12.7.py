# -*- coding: utf-8 -*-

# ヒストグラムの例

import random
import pylab

vals = [1, 200] # 値が1〜200の範囲にあることを仮定
for i in range(1000):
    num1 = random.choice(range(1,100))
    num2 = random.choice(range(1,100))
    vals.append(num1 + num2)
pylab.hist(vals, bins = 10)
pylab.show()
