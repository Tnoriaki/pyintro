# coding: utf-8

#  一つの正の整数をユーザに入力させた上で
#  root**pwrが入力した整数値と等しくなるような
#  2つの整数root,pwrを表示するプログラム (ただしpwrは1〜5)　

def main():
    pwr = 0
    root = 0
    x = int(raw_input("Enter a positive integer: "))
    if x < 0:
        print "Not a positive integer"
        quit()
    while pwr < 6:
        pwr += 1
        root = 0
        while root**pwr < abs(x):
            root += 1
        if root**pwr == abs(x):
            print "answer: %d^%d = %d" % (root,pwr,x)
        
if __name__ == "__main__":
    main()
        
