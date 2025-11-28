#  what is functions ans methods in python
#  function is a block of code which is used to perform a specific task
#  method is also a block of code which is used to perform a specific task but method is associated with the objects
#  function is defined using def keyword            
def my_function():
    print("hello world")        
my_function()  # function call



#  function with parameters
def my_function2(name, age):
    print("hello ", name)
    print("your age is ", age)  
my_function2("ananthsimha", 25)


#  function with return type
def my_function3(num1, num2):
    return num1 + num2  
result = my_function3(10, 20)


print("the sum is: ", result)


#  method is associated with the objects
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # append is a method of list object
print(my_list)
my_string = "hello world"
my_string_upper = my_string.upper()  # upper is a method of string object
print(my_string_upper)
#  difference between function and method   
#  function is defined using def keyword but method is defined inside the class
#  function is called using function name but method is called using object name


# function with no prarameters and no return values
def my_fun():
    print("This is a function with no parameters and no return values")

my_fun()
my_fun()
my_fun()


#  function with parameter no return values
def my_fun2(name):
    print("hello",name) 


my_fun2("ananthasimha2")   #passing the value during the function call
my_fun2("ganesh")



# function with parameters and return values
def my_fun3(num1,num2):
    num3=num2+num1
    return num3
sum=my_fun3(10,20 )
print("the sum is: ",sum)


# funnction reurns none
def my_func4():
    print("this function returns none")
    return

print(my_func4())

def my_func5():
    i=100


print(my_func5())
#  function arguments
# types of function arguments





# 3. default arguments

#  what is default arguments with example
# default arguments are the arguments which are assigned a default value during the function definition
# if the value is not passed during the function call then the default value is used
def greet(name, msg="Good morning!"):
    print("Hello", name + ', ' + msg)   

greet("lakshmi") 
  # using default message
greet("akshmi","How do you do?")



# 4. aritrary or variable lenth  length arguments and only tuple will accepts
    # explain this with example variable length arguments


def sum_function(a,b):
    return a+b

result=sum_function(10,20)
print("the sum is: ",result)


def sum2(*numbers):
    total=0
    for num in numbers:
        total =total+num
    return total


total=sum2(10,20,130,40,50)
print("the total sum is: ",total)


#  positinal and keyword arguments
# what is positional and keyword arguments with example give the answer
#  its a way to pass arguments to a function in python
#  positional arguments are passed to the function in the order they are defined in the function
#  keyword arguments are passed to the function using the name of the parameter
def person_info(name, age, city):
    print("name: ", name)
    print("age: ", age)
    print("city: ", city)

person_info("ananthsimha", 25, "bangalore")   # positional arguments

person_info(age=28 , name="man123",city="chennai")   # keyword arguments



#  function with return multiple values

def arithmetic_operations(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    return sum, difference, product, quotient

result = arithmetic_operations(20, 10)
print("the sum is: ", result[0])
print("the difference is: ", result[1]) 

print("the product is: ", result[2])
print("the quotient is: ", result[3])
#  unpacking the multiple return values
sum, difference, product, quotient = arithmetic_operations(30, 15)
print("the sum is: ", sum)
print("the difference is: ", difference)    
print("the product is: ", product)
print("the quotient is: ", quotient)

