#  whatt is global variable in python with example
#  global variable is a variable that is defined outside of a function and can be accessed from anywhere in the code
#  example of global variable
# when we want to access the variable inside the function we need to use the global keyword
var1=24
def my_variiable():
   
    var1 = 0.15255
    print("inside the function:", var1)
my_variiable()


#  example of local variable
def my_variable2():
    var2="this is a local variable"
    print("inside the function:",var2)

print(var1)

