# coding: utf-8

# try構文

def sumDigits(s):
    """sを文字列とする。sの中の数字の合計を返す"""
    Sum = 0
    for x in s:
        try:
            Sum += int(x)
        except ValueError:
            print x, 'is not an integer'
    return Sum

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = raw_input(requestMsg + ' ')
        try:
            val = valType(val)
            return val
        except ValueError:
            print val, errorMsg
            

def main():
    x = raw_input('Enter Strings: ')
    print sumDigits(x)
    print readVal(int, 'Enter an integer: ', 'is not an integer')
    

if __name__ == '__main__':
    main()
