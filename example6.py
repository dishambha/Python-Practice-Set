from typing import List


#Write a python program which accepts a sequence of comma-serpated numbers 
#from the user and generates a list and tuple wih those numbers

n = input("ENTER THE SEQUENCE OF NUMBERS : ")
list= n.split(",")
tuple= tuple(list)
print('list : ', list)
print("tuple : ", tuple)