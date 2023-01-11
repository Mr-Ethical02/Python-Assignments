'''
Assignment-2: To accept the number and Compute a) square root of number, b) Square of number, c) Cube of number d) check for prime, d) factorial of number e) prime factors.
'''
import math as m
num = int(input("Enter a number: "))

#square of the number
print("Square of the number is:",int(m.pow(num,2)))

#square root of the number
print("Square root of the number is:",m.sqrt(num))

#cube root of the number
print("Cube of the number is:",int(m.pow(num,3)))

#factorial of the number
print("Factorial of the number is:",int(m.factorial(num)))

#is number prime or not
c = 0
for i in range(2,num):
    if num == 2:
        print("The number is prime")
        exit()
    if(num % i == 0):
        c += 1   
if(c >= 1):
    print("The number is non prime")
else:
    print("The number is prime")

#prime factors of the number
print("Prime factors of the number are:")
for i in range(2, int(m.sqrt(num)) + 1):  
  
        if num == 1 or num == 0:
            exit()
        
        while num % i == 0:
            c = 0
            for i in range(2,i):
                if (i == 2):
                    print(i,)
                    exit()
                if(i % j == 0):
                    c += 1   
                if(c >= 1):
                    print(i,)  
            num = num / i
    
