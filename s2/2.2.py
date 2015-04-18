# coding: utf-8  
#日本語を含んだコードの場合上の記述が必要

#  三つの正の変数x,y,zを調べその中で最も大きい奇数を表示するプログラム
import sys

##  三つの正の変数から奇数のリスト作る関数
def odd_list(x,y,z):
    answer = []
    if x%2 == 1:
        answer.append(x)
    if y%2 == 1:
        answer.append(y)
    if z%2 == 1:
        answer.append(z)
    return answer
    
##  正の整数からなるリストの最大値を求める関数
def mymax(row):
    answer = 0
    for x in row:
        if x > answer:
            answer = x
    return answer

##  main関数
def main():
    argvs = sys.argv
    argc = len(argvs)
    if argc != 4:
        print 'Input 3 number!!'
        quit()
    x = int (argvs[1])
    y = int (argvs[2])
    z = int (argvs[3])    
    odd_v = odd_list(x,y,z)
    if odd_v == []:
        print 'No odd!!'
        quit()
    else : 
        print 'answer = %d' %  mymax(odd_v)

if __name__ == '__main__':
    main()
