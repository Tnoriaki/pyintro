# coding: utf-8

from mitperson import MITPerson,Student

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year

class Grad(Student):
    pass

class TransferStudent(Student):
    def init(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool
    def getOldSchool(self):
        return self.fromSchool

def main():
    p3 = MITPerson('Billy Bob Beaver')
    p5 = Grad('Buzz Aldrin')
    p6 = UG('Billy Beaver', 1984)
    print p5, 'is a graduate student is ', type(p5) == Grad
    print p5, 'is a undergraduate student is', type(p5) == UG
    print p5, 'is a student is', p5.isStudent()
    print p6, 'is a student is', p6.isStudent()
    print p3, 'is a student is', p3.isStudent()

if __name__ == '__main__':
    main()
