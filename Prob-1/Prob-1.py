# Module 8
#   Programming Assignment 11
#     Prob-1.py

# Your code below
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getYear(self):
        return self.year
       
def testCar():
    carlot = []
    for i in range(2):
        make = input("enter make: ")
        model = input("enter model: ")
        year = input("enter year: ")
        carlot.append( Car(make,model,year))

    for car in carlot:
        print(car.getMake())
        print(car.getModel())
        print(car.getYear())

    for i in range(len(carlot)):
        make = input("enter make: ")
        model = input("enter model: ")
        year = input("enter year: ")
        carlot[i].setMake(make)
        carlot[i].setModel(model)
        carlot[i].setYear(year)
    
    for car in carlot:
        print(car.getMake())
        print(car.getModel())
        print(car.getYear())

testCar()