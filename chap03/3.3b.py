# coding: utf-8

#  整数に対して立方根の近似解を二分法により求める

def main():
    x = int(raw_input("Enter an integer: "))
    epsilon = 0.01
    numGuess = 0
    low = min(0, x)
    high = max(0, x)
    answer = (high + low)/2.0
    while abs(answer**3 - x) >= epsilon:
        print 'low =', low, 'high =', high, 'answer =', answer
        numGuess += 1
        if answer**3 < x:
            low = answer
        else :
            high = answer
        answer = (high + low)/2.0
    print 'numGuess =', numGuess
    print answer, 'is close to cube root of', x

    
if __name__ == "__main__":
    main()
