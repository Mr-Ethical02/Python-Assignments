n = int(input("Enter the number of rows to print pattern upto\n"))
'''pat = ""
for i in range(1,no+1):
    for j in range(0,i):
        pat += "* "
    pat += "\n"
    
print("Complete Pattern is:")
print(pat)'''

'''no = int(input("Enter the number of rows to print pattern upto\n"))
pat = ""
for i in range(0,no+1):
    for j in range(0,no-i):
        pat += "* "
    pat += "\n"
    
print("Complete Pattern is:")
print(pat)'''

#n = 5
k = n-1
pattern = ""
for i in range(0, n):
    for l in range(0,k):
        pattern += " "
    k= k-1
    for j in range(0,i+1):
        pattern += "* "
    pattern += "\n"
print(pattern)