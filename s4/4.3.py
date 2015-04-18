# coding: utf-8

#繰り返しと再帰による階乗を実装したプログラム

def factI(n):
    u"""n > 0を満たす整数と仮定
    n!を返す"""

    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

def factR(n):
    u"""n > 0を満たす整数と仮定
    n!を返す"""

    if n == 1:
        return n
    else :
        return n*factR(n-1)

def main():
    n = int(raw_input("Enter a positive integer: "))
    print factI(n)
    print factR(n)

if __name__ == '__main__':
    main()
