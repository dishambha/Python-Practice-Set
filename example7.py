#write a python program that takes input from the user and prints the type op the file

file_name = input("ENTER THE FILE NAME :")
f_ext = file_name.split(".")
print(f"THE EXTENSION THE THE FILE IS ", repr(f_ext[-1] ))
