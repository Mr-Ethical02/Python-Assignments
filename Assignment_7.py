'''
To check whether input number is Armstrong number or not. An Armstrong number is an integer with three digits such that the sum of the cubes of its digits is equal to the number itself. Ex. 371.
'''
num = int(input("Enter a number to check if it is armstrong or not: "))
tmp = num
sum = 0
while(num != 0):
    rem = num % 10
    sum += (rem**3)
    num //= 10
    
if(sum == tmp):
    print(tmp,"is a Armstrong Number")
else:
    print(tmp,"is not a Armstrong Number")