# coding: utf-8

#  正の整数に対して平方根の近似解を二分法により求める

def main():
    x = int(raw_input("Enter a positive integer: "))
    epsilon = 0.01
    numGuess = 0
    low = 0.0
    high = max(1.0 , x)
    answer = (high + low)/2.0
    while abs(answer**2 - x) >= epsilon:
        print 'low =', low, 'high =', high, 'answer =', answer
        numGuess += 1
        if answer**2 < x:
            low = answer
        else :
            high = answer
        answer = (high + low) / 2.0
    print 'numGuess =', numGuess
    print answer, 'is close to square root of', x
    
if __name__ == "__main__":
    main()
