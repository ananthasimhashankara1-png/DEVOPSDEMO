#  creatrinng the tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

my_tuple2 = ("man1","Ananthsimha", "man1",25,"man1",True, 5,9,9)
print(my_tuple2.count("man1"))
print(my_tuple2)


# accessing the tuple elements
print(my_tuple2[3])
print(my_tuple2[-2])


#  slicing the tuple
my_tuple3 = ("man1","Ananthsimha", "man1",25,"man1",True, 5,9,9)
print(my_tuple2[-7:-2])

#  change the value in tuple
my_tuple4 = ("man1","Ananthsimha", "man1",25,"man1",True, 5,9,9)
# my_tuple4[2]="changed"
my_list=list(my_tuple4)
my_list[2]="changed"
my_tuple4=tuple(my_list)
print(my_tuple4)


#  serching nthe item in tuple
my_tuple5 = ("man1","Ananthsimha", "man1",25,"man1",True, 5,9,9)
if "man10" in my_tuple5:
    print("man1 is present in the tuple")
else:
    print("man1 is not present in the tuple")

#  length of the tuple
my_tuple6 = ("man1","Ananthsimha", "man1",25,"man1",True, 5,9,9)
print(len(my_tuple6))




# copying the tuple
my_tuple7 = ("man1","Ananthsimha", "man1",25,"man1",True, 5,9,9)
my_tuple8=my_tuple7 
print(my_tuple8)


# joining the tuple
my_tuple9 =my_tuple2+my_tuple4
print(my_tuple9)