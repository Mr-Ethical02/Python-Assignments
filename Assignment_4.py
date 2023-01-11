'''
To accept N numbers from user. Compute and display maximum in list, minimum in list, sum and average of numbers.
'''

num = []
n = int(input("Enter number of items that you want to add in the list: "))
try:
    print("Enter",n,"numbers")
    
    for i in range(0,n):
        n1 = int(input())
        num.append(n1)
except:
    print("Only Integers allowed!")

sum = 0
for i in num:
    sum += i
    
num.sort()
print("Maximum in the list is:",num[0])

num.reverse()
print("Minimum in the list is:",num[0])

print("Sum of the numbers in the list is:",sum)

avg = sum/n
print("Average of the numbers in the list is: %.2f" % avg)