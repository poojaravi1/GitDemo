#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object

#class Calculator:
    #num = 100

    #def __int__(self, a, b):
        #self.firstNumber = a
        #self.secondNumber = b
        #print("I am called automatically when object is created")


    #def getData(self):
        #print("I am now executing as a method in class")

    #def summation(self):
        #return self.firstNumber + self.secondNumber

class Calculator:
    num = 100  #class variables
    #default constructor

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber



#obj = Calculator(4,5) #syntax to create objects in Python
#obj.getData() #calling getData method within a class using objects
#print(obj.num)  #calling and printing the value stored in variable using objects
#print(obj.summation())

#obj = Calculator(2, 3)
#obj.getData()
#print(obj.summation())

obj = Calculator(2, 3)
print(obj.Summation())
