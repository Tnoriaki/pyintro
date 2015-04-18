# coding: utf-8

#  正の整数に対してニュートンラフソン法により平方根の近似解を求めるプログラム
#  x*2-aがepsilon以内になるようにxを求める

def main():
    k = int(raw_input("Enter a positive integer: "))
    numGuess = 0
    epsilon = 0.01
    guess = k/2.0
    while abs(guess*guess - k) >= epsilon:
        guess = guess - ((guess**2 - k) / (2*guess))
        #next_guess = guess - f(guess)/f'(guess)
        numGuess += 1
    print 'numGuess =', numGuess
    print 'Square root of', k, 'is about',guess
        
if __name__ == '__main__':
    main()
