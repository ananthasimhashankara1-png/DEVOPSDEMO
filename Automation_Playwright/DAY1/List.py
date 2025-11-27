# creating the the list

Mylist1=[1,2,3,4,5]
mylist2=["Ananthsimha","is","a","good","man","man","man2"]
print(len(Mylist1))
mylist3=[1,"Ananthsimha",2.5,True]
print(Mylist1)
print(mylist2)
print(mylist3)
mylist5=[]
print(mylist5)
print(Mylist1[1])
print(Mylist1)
Mylist1[2]=20
print(Mylist1)
if 10 in Mylist1:
    print("10 is present in the list")
else:
    print("10 is not present in the list")

#  count in the list
mylist2=["Ananthsimha","is","a","good","man","man","man2"]
print(mylist2.count("man"))
# sorting of the list
mylist2=["Ananthsimha","is","a","good","man","man","man2"]
mylist2.sort()
print(mylist2)
# sorting of the list in desccending order
mylist2=["Ananthsimha","is","a","good","man","man","man2"]
mylist2.sort(reverse=True)
print(mylist2)

# append the list
Mylist1=[1,2,3,4,5]
Mylist1.append(10)
print(Mylist1)

# insert the list
Mylist1=[1,2,3,4,5]
Mylist1.insert(1,25)
print(Mylist1)

# remover from the list
Mylist1=[1,2,3,4,5]
Mylist1.remove(2)
print(Mylist1)

#  using the pop
Mylist1=[1,2,3,4,5]
Mylist1.pop(2)
print(Mylist1)


Mylist1=[1,2,3,4,5]
del Mylist1[0]
print(Mylist1)

# clear the list
Mylist1=[1,2,3,4,5]
Mylist1.clear()
print(Mylist1)

#  delete the list
Mylist1=[1,2,3,4,5] 
del Mylist1


#  copy the list
Mylist1=[1,2,3,4,5]
Mylist4=Mylist1.copy()
print(Mylist1)
print(Mylist4)


#  list using the for copy
Mylist1=[1,2,3,4,5]
mylist5=list(Mylist1)
print(Mylist1)  
print(mylist5)



#  join the listr using +

mylist5=[1,2,3]
mylist6=["Ananthsimha","is","a","good","man"]
mylist6=mylist5+mylist6
print(mylist6)


#  joing the list using the loop        
mylist5=[1,2,3]
mylist6=["Ananthsimha","is","a","good","man"]
for item in mylist5:
    mylist6.append(item)
print(mylist6)


#  join the list using the extend
ylist5=[1,2,3]
mylist6=["Ananthsimha","is","a","good","man"]
mylist5.extend(mylist6)
print(mylist6)  
print(mylist5)