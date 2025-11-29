# what is class in OOPS?
# A class is a blueprint for creating objects. It defines a set of attributes and methods 
# that the created objects will have.
# Class is defined using the class keyword      
class Car:
    # #  constructor method to initialize the object
    # def __init__(self, make, model, year):
    #     self.make = make
    #     self.model = model
    #     self.year = year

    # # method to display car details
    # def display_details(self):
    #     print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")
    def myfun(self):
        print("this is my first class in python")

    def dislay(self,name,age):
        print("hello ",name)
        print("your age is ",age)
# creating an object of the class
mc=Car()
mc.myfun()
mc.dislay("ananthsimha",25)


# instance method and static method in python class
# instance method is a method that is associated with the object of the class
# static method is a method that is associated with the class itself
# when we want to access the instance method we need to create the object of the class
# when we want to access the static method we can access it using the class name
# why we use static method?
# static method is used when we want to create a method that is not related to the object

# example of the intance method
class Person:
    

    def display(self):
        print("this is instance method")


    @staticmethod
    def m2(self,num):
        print(self,num)


# dis=Person()
# dis.display()
# dis.m2(100,200)

# Person.m2(300,400)
# Person.display()
#  what is constructor in python class?
# constructor is a special method that is called when an object of the class is created
# constructor is defined using the __init__ method  
#  why we use the constructor?
# constructor is used to initialize the attributes of the object

class Animal:
    def __init__(self):
        print("this is constructor example")
    

    def m1(self):
        print("this  example")


mc3=Animal()
mc3.m1()
