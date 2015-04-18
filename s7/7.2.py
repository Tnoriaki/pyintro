# coding: utf-8

# フロー制御機構としての例外
# try構文とraise文


def findAnEven(l):
    """lをint型の要素を持つリストとする
       lに最初に現れる偶数を返す
       lが偶数を含まなければValueErrorを引き起こす"""
    try:
        for x in l:
            if int(x) % 2 == 0:
                return x
    except:
        raise ValueError('l is not involved even')
    
def getRatios(vect1, vect2):
    """vect1とvect2を同じ長さのリストとする
       vect1[i]/vect2[i]を意味する値からなるリストを返す"""
    ratios = []
    for index in range(len (vect1)):
        try:
            ratios.append(vect1[index]/float(vect2[index]))
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios

def getGrades(fname):
    try:
        gradesFile = open(fname, 'r') #読み込み用のファイルを開く
    except IOError:
        raise ValueError('getGrades could not open ' + fname)
    grades = []
    for line in gradesFile:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')
        return grades
        

def main():
    #findAnEven test
    try:
        print findAnEven([1.0, 2.0, 6.0])
        print findAnEven([1.0, 3.0])
        print findAnEven('acbdefg')
    except ValueError, msg:
        print msg

    #getRatios test
    try:
        print getRatios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 0.0, 3.0])
        print getRatios([], [])
        print getRatios([1.0, 2.0], [3.0])
    except ValueError, msg:
        print msg
    
    #getGrades test
    try:
        grades = getGrades('quiz1grades.txt')
        grades.sort()
        median = grades[len(grades)//2]
        print 'Median grade is', median
    except ValueError, errorMsg:
        print 'Woops.', errorMsg

  
if __name__ == '__main__':
    main()
