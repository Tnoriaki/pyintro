# coding: utf-8

# 学生と教員の情報管理のためのクラスの利用
# 抽象データ型とクラス

import datetime

class Person(object):
    def __init__(self, name):
        """「人間」を生成する"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank + 1:]
        except:
            self.lastName = name
        self.birthday = None
    
    def getName(self):
        """selfの名前（フルネーム）を返す"""
        return self.name

    def getLastName(self):
        """selfの姓を返す"""
        return self.lastName
    
    def setBirthday(self, birthdate):
        """birthdateをdatetime.date型とする
        selfの生年月日をbirthdateと設定する"""
        self.birthday = birthdate

    def getAge(self):
        """selfの現在の年齢を日単位で返す"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    def __lt__(self, other):
        """selfの名前がotherの名前と比べて辞書順で前ならばTrueを、
        そうでなければFalseを返す"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """selfの名前(フルネーム)を返す"""
        return self.name
        
def main():
    me = Person('Michael Guttag')
    him = Person('Barack Hussein Obama')
    her = Person('Madonna')
    print him.getLastName()
    him.setBirthday(datetime.date(1961,8,4))
    her.setBirthday(datetime.date(1958,8,16))
    print him.getName(), 'is', him.getAge(), 'days old'
    pList = [me, him, her]
    for p in pList:
        print p
    pList.sort()
    for p in pList:
        print p
    
if __name__ == '__main__':
    main()
