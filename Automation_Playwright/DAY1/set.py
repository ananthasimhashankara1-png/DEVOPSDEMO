# set can store all type of the data
#  set in python is similar to list or dictionary but with unique values only
# set not support indexing and slicing
#  set is not take both duplicate values and order of the values
#  set is mutable we can change the values in set
my_set={1,2,3,4,5}
print(my_set)
my_set2={"apple","banana","cherry"}
print(my_set2)

#  creating the empty set
my_set3=set()
print(type(my_set3))


#  addin the sew item to set
my_set3.add("apple")
print(my_set3)
my_set.add("banana")
print(my_set)

my_set3.update(["banana","cherry","orange","grape"])
print(my_set3)

# access the data from the set using for loop
for item in my_set3:
    print(item)

if "banana" in my_set3:
    print("banana is present in the set")   
else:
    print("banana is not present in the set")

print("banana" in my_set3   )

print(len(my_set3))
print(my_set3)

my_set3.remove("banana")
print(my_set3)

print(len(my_set3))
print(my_set3)

del my_set3
print(my_set3)