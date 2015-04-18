# coding: utf-8

# カプセル化と情報隠蔽

from student import UG,Grad

class Grades(object):
    """学生から成績リストへの写像"""
    def __init__(self):
        """空の成績ブックを生成する"""
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """studentをStudent型とする
        studentを成績ブックへ追加する"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getidNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """gradeをfloat型とする
        gradeをstudentの成績リストへ追加する"""
        try:
            self.grades[student.getidNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')
        
    def getGrades(self, student):
        """studentの成績リストを返す"""
        try: # studentの成績リストのコピーを返す
            return self.grades[student.getidNum()][:]
        except:
            raise ValueError('Student not in mapping')

    def getStudents(self):
        """成績ブックに収められた学生のリストを、一度に一要素ずつ返す"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s
    # def getStudents(self):
    #     """成績ブックに収められた学生のリストを返す"""
    #     if not self.isSorted:
    #         self.students.sort()
    #         self.isSorted = True
    #     return self.students[:] #学生のリストのコピーを返す
   
def gradeReport(course):
    """courseをGrade型とする"""
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report = report + '\n'\
                     + str(s) + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n'\
                     + str(s) + ' has no grades'
    return report

def main():
    ug1 = UG('Jane Doe', 2014)
    ug2 = UG('John Doe', 2015)
    ug3 = UG('David Henry', 2003)
    g1 = Grad('Billy BUckner')
    g2 = Grad('Bucky F. Dent')
    sixHundred = Grades()
    sixHundred.addStudent(ug1)
    sixHundred.addStudent(ug2)
    sixHundred.addStudent(g1)
    sixHundred.addStudent(g2)
    for s in sixHundred.getStudents():
        sixHundred.addGrade(s,75)
    sixHundred.addGrade(g1, 25)
    sixHundred.addGrade(g2, 100)
    sixHundred.addStudent(ug3)
    print gradeReport(sixHundred)
    book = Grades()
    book.addStudent(Grad('Julie'))
    book.addStudent(Grad('Charlie'))
    for s in book.getStudents():
        print s
if __name__ == '__main__':
    main()
