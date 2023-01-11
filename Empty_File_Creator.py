import subprocess as sub
import os

print("Current Working Directory",os.getcwd())
path=input("Enter the path you want to create files on: ")
if(len(path)>0):
    os.chdir(path)
    print("Changed to",os.getcwd())
else:
    print("Proceeding with current directory")

file_name = input("Input file name: ")
ext = input("Enter file extension. Eg(.py,.txt,etc): ")
no = int(input("Enter the number of files to create: "))
if(no == 1):
    sub.run("type nul > "+file_name+ext,shell=True)
else:
    for i in range(1,no+1):
        n = str(i)
        sub.run("type nul > "+file_name+"_"+n+ext,shell=True)

print("\n List of files created:")
for x in os.listdir():
    if x.startswith(file_name) and x.endswith(ext):
        print(x)
print("\n")

print("Process Completed! Thanks for using.")