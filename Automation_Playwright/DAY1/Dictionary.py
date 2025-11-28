# strotre data inthe key value
my_dict={"name":"ananthsimha","age":25,"city":"bangalore"}
print(my_dict)

# accessing the data from the dictionary
print(my_dict.get("name"))
print(my_dict.get("age"))


# adding the new key value pair to the dictionary
my_dict["salary"]=50000
print(my_dict)

#  create the dictionary using constructor
my_dict2=dict(name="man1",age=30,city="chennai")
print(my_dict2)

#  updating the value in the dictionary
my_dict2["age"]=39 
print(my_dict2)



# key can have multiple values
my_dic3={"name":"ford","model":"mustang","year":1964,"colors":["red","blue","green"]}
print(my_dic3)


# accessing the values from the dictionary 
print(my_dic3   ["colors"])

#  accessiong the dictory using the get the method
print(my_dic3.get("name"))

# i wnat to extract the key from the dictionary
print(my_dic3.keys())
print(my_dic3.values() )

#  using the itmems method to get both key and values and it return as tuple
print(my_dic3.items())

# checking the key is present in the dictionary or not
if "models" in my_dic3:
    print("model is present in the dictionary")
else:
    print("model is not present in the dictionary")

#  checking the length of the dictionary
print(len(my_dic3))

# update the dictionary using update method
my_dic3.update({"yesr":2025,
                "p[rice":600000})

print(my_dic3)

my_dic3.update({"yesr":2024,
                "p[rice":700000})

print(my_dic3)

# the difference between add and update add can only add new key value pair but update can change the existing key value pair also 
# add a new key using assignment
my_dic3["milage"] = "25kmpl"
print(my_dic3)

# removing the key value pair from the dictionary pop will remove the specific key value pair but popitem will remove the last inserted key value pair
my_dic3.pop("yesr")
print(my_dic3)
my_dic3.popitem()
print(my_dic3)
#  delate entire key value pair
my_dic3.clear()
print(my_dic3)
#  deleting the dictionary del keyword will delete the entire dictionary
# del my_dic3

# copying the dictionary
my_dict4={"name":"ananthsimha","age":25,"city":"bangalore1"}
my_dict5=my_dict4.copy()    
print(my_dict5)


my_dict6=my_dict4
#  it will not create the new object it will create the reference of the existing object
print(my_dict6)

my_dict7=dict(my_dict4)
print(my_dict7)


#  i wwant to print all the key from the dictionary one by one using for loop
my_dict8={"name":"ananthsimha","age":25,"city":"bangalore2"}

for keys in my_dict2:
    print(keys)

for key in my_dict8.keys():
    print(key) 

#  i wwant to print all the values from the dictionary one by one using for loop
for values in my_dict8.values():
    print(values)

#   i wwant to print all the values from the dictionary one by one using for loop
for values in my_dict8:
    print(my_dict8[values])


# i wwant to print all the item from the dictionary one by one using for loop
for keys,items in my_dict2.items():
    print(keys,items)