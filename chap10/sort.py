# coding: utf-8

# 様々なソート

## 選択ソート
## 計算量O(n^2) インプレースなので外部記憶は定数サイズ
def selSort(L):
    """Lを、>を用いて比較できる要素からなるリストとする
    Lを、昇順にソートする"""
    suffixStart = 0
    while suffixStart != len(L):
        #サフィックスの各要素を見る
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                #要素を入れ替える
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1

## マージソート
## 計算量O(nlogn) リストのコピーを利用するため空間計算量がO(len(L))
def merge(left, right, compare):
    """leftとrightをソート済みのリストとし、
    compareを要素間の順序を定義する関数とする
    (left + right)と同じ要素からなり、
    compareに従いソートされた新たなリストを返す"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    #print result
    return result
    

import operator

def mergeSort(L, compare = operator.lt):
    """Lをリストとし、
    compareをLの要素間の順序を定義する関数とする
    Lと同じ要素からなり、ソートされた新たなリストを返す"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)
        
