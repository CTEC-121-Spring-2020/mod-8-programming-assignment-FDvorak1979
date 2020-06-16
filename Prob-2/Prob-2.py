# Module 8
#   Programming Assignment 11
#     Prob-2.py

# Your code below
class Student:
    def __int__(self, name, SIDN, major, GPA, status):
        self.name = name
        self.SIDN = SIDN
        self.major = major
        self.GPA = GPA
        self.status = status
    def getNAme(self):
        return self.name
    def getSIDN(self):
        return self.SIDN
    def getMajor(self):
        return self.major
    def getGPA(self):
        return self.GPA
    def getStatus(self):
        return self.status
    
def testStudent():
    students = []
    for i in range(4):
        name = input("enter name: ")
        SIDN = input("enter SIDN: ")
        major = input("enter major: ")
        GPA = input("enter GPA")
        status = input("enter status eather public or private")
        students.append( Student(name, SIDN, major, GPA, status))

    for student in students:
        print(student.getName)
        print(student.getSIDN)
        print(student.getMajor)
        print(student.getGPA)
        print(student.getStatus)

    for i in range(len(carlot)):
        name = input("enter name: ")
        SIDN = input("enter SIDN: ")
        major = input("enter major: ")
        GPA = input("enter GPA")
        status = input("enter status eather public or private")
        students.append( Student(name, SIDN, major, GPA, status))
    
    for student in students:
        print(student.getName)
        print(student.getSIDN)
        print(student.getMajor)
        print(student.getGPA)
        print(student.getStatus)

'''
    student9933 = Student("Joe Bella","9933","Web Development","3.8","56","private")
    student3399 = Student("Tucker Blank","3399","Nursing","3.0","88","private")
    student1011 = Student("Gayle Ujifusa","1011","Baking","2.8","32","private")
    student9875 = Student("Edna Anker","9875","Medical Office","3.0","95","private")
'''

# I felt in order to get a good quick glance at a student that name, SIDN(Student ID Number) and GPA
# are all good infor for giving a college staff or faculty member a quick acamenic related glance
# at a student.  I did feel it was a bit lacking tho and needed a listing for total credits earned along side
# major.  Credit levels give an idea of how close a student is to completion.  I found tho that I had a problem.
# the problem was I could not do more than one world in def __int__ so I had to leave it as credits.
# I usded student followed by number to simulate how a real student would be indexed or looked up, 
# I did not think using just the first name or anything els would be realistic
# I set a simple variable for status in the def __int__ for simplicity sake and,
# I did not know how to implement the way it was used in the video

# I did the best I could using problem 2 as a template.  I still have errors that I cannot figure out even tho I followed your method and the videos.
# I think the way set is used was wrong from looking online but unsure how to use it.
# since credits were in yellow and I had an error I decided to removwe it.  I still get an odd error that I do not understand
# what I fail to comprehend is Student() takes to arguments when this is follwoing the other template.  I am at a loss
testStudent()