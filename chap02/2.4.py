# coding: utf-8

#  ユーザに10個の正の整数の入力を促した上でその中で最も大きな奇数の値を表示するプログラム

##  ユーザが入力した10個の正の整数をある配列に整数型で格納する関数
def input10():
    print "Input 10 numbers"
    i = 10
    answer = []
    while (i != 0):
        x = int(raw_input("No %d : "% (11 - i)))
        i -= 1
        answer.append(x)
    return answer

##  引数として渡された配列から奇数のみ取り出しある配列に格納する関数
def odd_list(v):
    answer = []
    for x in v:
        if x%2 == 1:
            answer.append(x)
    if answer == []:
        print "No odd!!!"
        quit()
    return answer

##  引数として渡された配列から最大値を求める関数
def mymax(v):
    answer = 0
    for x in v:
        if x > answer:
            answer = x
    return answer
    
##  main関数
def main():
    a = input10()
    a = odd_list(a)
    print mymax(a)

    
if __name__ == "__main__":
    main()

        
    
