# coding: utf-8

#  10進数を含む文字列をコンマで分けた上でその合計を求めて表示するプログラム

def main():
    s = raw_input("Enter a string of number: ")
    answer = 0
    tmp = ""
    for x in s:
        if x == ",":
            answer += float(tmp)
            tmp = ""
        else:
            tmp += x
    answer += float(tmp)
    print "Sum = %f" % answer

if __name__ == "__main__":
    main()
