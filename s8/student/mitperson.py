# coding: utf-8

# 継承

from person import Person

class MITPerson(Person):
    nextidNum = 0 #個人識別番号

    def __init__ (self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextidNum
        MITPerson.nextidNum += 1
        
    def getidNum(self):
        return self.idNum

    def isStudent(self):
        return isinstance(self, Student)
    
    def __lt__(self,other):
        return self.idNum < other.idNum

class Student(MITPerson):
        pass

def main():
    p1 = MITPerson('Mark Guttag')
    print str(p1) + '\'s id number is' + str(p1.getidNum())
    p2 = MITPerson('Billy Bob Beaver')
    p3 = MITPerson('Billy BOb Beaver')
    p4 = Person('Billy Bob Beaver')
    print 'p1 < p2 =', p1 < p2
    print 'p3 < p2 =', p3 < p2
    print 'p4 < p1 =', p4 < p1
    #print 'p1 < p4 =', p1 < f4 ←Person型にはidNumの属性が存在しないのでAttributeErrorという例外が発生する
    
if __name__ == '__main__':
    main()
