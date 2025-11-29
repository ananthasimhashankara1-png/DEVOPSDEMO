#  what is inheritence in OOPS?
# Inheritence is a mechanism that allows a class to inherit attributes and methods from another class   
#  why we use inheritence?
#  inheritence is used to achieve reusability and to establish a relationship between classes
#  types of inheritence in python       
# 1. single inheritence
# 2. multiple inheritence   
# 3. multilevel inheritence
# 4. hierarchical inheritence
# 5. hybrid inheritence


# example of single inheritence
class parent:
    def parent_method(self):
        print("this is parent method")

class child(parent):
    def child_method(self):
        print("this is child method")

class parent2:
    i=20
    j=30
    def paent2_metod(self):
        numn1=self.i+self.j
        print("the sum is ",numn1)  
        print("this is parent2 method")

class child2(parent2):
    a,b=40,50

    def child2_method(self):
        sub=self.b-self.a
        print("the sub is ",sub)
        print("this is child2 method")


objibfo=child()
objibfo.parent_method()
objibfo.child_method()

objinfo2=child2()
objinfo2.paent2_metod()
objinfo2.child2_method()


# whta is overriddibng in inheritence?
#  when a child class has a method with the same name as a method in the parent class,
#  the method in the child class overrides the method in the parent class

class parent3:
    def display(self):
        print("this is parent3 display method")
class child3(parent3):
    def display(self):
        # print("this is child3 display method")
        super().display() #this is used to call the parent class method invoke the parent class method
objec=child3()
objec.display()