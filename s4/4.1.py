# coding: utf-8

# 2つの文字列を引数とし、このどちらか一方の文字列が他方の文字列内に含まれる場合、TRUEを返し、それ以外の場合、Falceを返す関数(isIn関数)を書いたプログラム

def isIN(a,b):
    tmp = ''
    tmp_i = 0
    ##大きい文字列をstr1、小さい文字列をstr2に格納
    if len(a) > len(b):
        str1 = a
        str2 = b
    else:
        str1 = b
        str2 = a
    ##探索してtmpに一致した文字列を格納する
    for x in str1:
        if x == str2[tmp_i]:
            tmp_i += 1
            tmp += x
            if tmp == str2:
                break
        else :
            tmp_i = 0
            tmp = ''
    return tmp == str2

def main():
    a = raw_input("Enter a string: ")
    b = raw_input("Enter a string: ")
    if isIN(a,b):
        print "True"
    else :
        print "False"

if __name__ == "__main__":
    main()
    
            

