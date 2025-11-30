# # creating the file
# file=open("D:/New folder/SRE/DEVOPSDEMO/myfile.txt",'w')
# file.write("welcome to the python demo \n added the new linw data")
# file.close()

# file=open(r"D:\New folder\SRE\DEVOPSDEMO\myfile2.txt","w")
# file.write("this is my second file \n new line is added")
# file.close()
           


# file=open(r"D:\New folder\SRE\DEVOPSDEMO\myfile3e.txt","a")
# file.write("256986 \n addin the new file to append12345 \n will add ethe data doe the file it will append ")
# file.close()

# #  reading the data from the the text file
# # read( readline, readlines)

# file=open(r"D:\New folder\SRE\DEVOPSDEMO\myfile3e.txt","r")
# read1=file.readlines()
# print(read1)


# # renaming the file
import os
# os.rename(r"D:\New folder\SRE\DEVOPSDEMO\myfile.txt",r"D:\New folder\SRE\DEVOPSDEMO\myfile3.txt")

# delete the file
# if exit or
file=r"D:\New folder\SRE\DEVOPSDEMO\myfile.txt"
if os.path.exists(file):
    os.remove(file)
else:
    print("file is not found")