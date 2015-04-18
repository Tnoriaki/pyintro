# coding: utf-8

# フィボナッチ回帰とこれをテストする関数を定義したプログラム

def fib(n):
    u"""n > 0 を満たす整数と仮定
    n番目のフィボナッチ数を返す"""

    if n == 0 or n == 1:
        return 1
    else :
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        if i > 1:
            print 'fib of', i, '=', fib(i), ': fib of', i-1, "+ fib of", i-2
        else:
            print 'fib of', i, '=', fib(i)
        
def main():
    #n = int(raw_input("Enter a positive integer: "))
    testFib(5)

if __name__ == '__main__':
    main()


        
