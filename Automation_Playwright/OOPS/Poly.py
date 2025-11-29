# what is the polymorphism?
# Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass.
# It enables a single interface to represent different underlying forms (data types). 
#  why we use polymorphism?
# Polymorphism is used to achieve flexibility and reusability in code. It allows methods to be used interchangeably, regardless of the specific class of the object that invokes them.
#  types of polymorphism in python  
# 1. compile time polymorphism (method overloading)
#  method overloading is not directly supported in python but we can achieve it using default arguments or variable length arguments    
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c
math_ops = MathOperations()
print("Sum of 2 numbers:", math_ops.add(10, 20))          #  using 2 arguments
print("Sum of 3 numbers:", math_ops.add(10, 20, 30))      # using 3 arguments

# 2. run time polymorphism (method overriding)
# method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already defined in its superclass
class Bird:
    def sound(self):
        print("Bird makes a sound")
class Dog:
    def sound(self):
        print("Dog barks")  # explain this
def animal_sound(animal):
    animal.sound()