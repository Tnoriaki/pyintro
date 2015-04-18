#coding: utf-8

#pythonにおけるソーティング
#ティムソート←安定ソート

L = [3,5,2]
D = {'a':12, 'c':5, 'b':'dog'}
print sorted(L)
print L
L.sort()
print L
print sorted(D)
#D.sort()
#dict.sortというメソッドは存在しない
L = [[1,2,3], (3,2,1,0), 'abc']
print sorted(L, key = len, reverse = True)
#keyはcompareの役割、reverseはリストを昇順と降順どちらにソートするか
