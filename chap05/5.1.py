# coding: utf-8

# タプルを用いて公約数を求めるプログラム
# 順序型と多重代入の利用

def findDivisors (n1, n2):
    """n1とn2を正のint型とする。
    n1とn2のすべての公約数からなるタプルを返す"""

    divisors = ()
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            divisors = divisors + (i,)
    return divisors

def findExtremeDivisors(n1, n2):
    """n1とn2を正のint型とする。
    n1とn2の 最小の公約数 > 1 と 最大公約数 からなるタプルを返す"""

    divisors = ()
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if minVal == None or i < minVal:
                minVal = i
            if maxVal == None or i > maxVal:
                maxVal = i
    return (minVal, maxVal)

def main():
    divisors = findDivisors(100, 200)
    print divisors
    total = 0
    for d in divisors:
        total += d
    print total
    minDivisor, maxDivisor = findExtremeDivisors(100,200)
    print minDivisor
    print maxDivisor

if __name__ == '__main__':
    main()
         
