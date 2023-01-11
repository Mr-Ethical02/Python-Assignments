'''
To simulate simple calculator that performs basic tasks such as addition, subtraction, multiplication and division with special operations like computing xy and x!
'''

#Calcluator using switch..

import math as m

def Calculator(input,numbers):
    match input:
        case 1:
            sum = 0
            numbers = numbers.split(",")
            for i in numbers:
                sum += int(i)
            print("Addition is:",sum)
            
        case 2:
            numbers = numbers.split(",")
            sum = int(numbers[0])+int(numbers[0])
            for i in numbers:
                sum -= int(i)
            print("Subtraction is:",sum)
            
        case 3:
            sum = 1
            numbers = numbers.split(",")
            for i in numbers:
                sum *= int(i)
            print("Multiplication is:",sum)
            
        case 4:
            numbers = numbers.split(",")
            sum = int(numbers[0])
            for i in numbers:
                if(sum == int(i)):
                    continue
                sum = sum / int(i)
            print("Division is:",sum)
            
        case 5:
            numbers = numbers.split(",")
            if(len(numbers) > 2 or len(numbers) < 2):
                print("Cannot process your request. Problem with the parameters passed!")
            else:
                result = int(m.pow(int(numbers[0]),int(numbers[1])))
                print("X raised to y is:", result)

        case 6:
            numbers = numbers.split(",")
            if(len(numbers) > 1 or len(numbers) < 1):
                print("Cannot process your request. Problem with the parameters passed!")
            else:
                result = m.factorial(int(numbers[0]))
                print('%d! is:' % int(numbers[0]),result)
        
            
while(True):
    print('''
Welcome to PY Calcluator
Note: Please seperate the numbers using comma(,)
Choose operation you want to perform from the list below:
1.Addition
2.Subtration
3.Multiplication
4.Division
5.x raised to y
6.x!
7.Exit''')
    case_switch = int(input("Select Operation: "))
    if(case_switch == 7):
        exit()
    elif(case_switch > 7 or case_switch < 1):
        print("\nInvalid Entry!!")
    else:
        num = input("Enter numbers:\n")
        Calculator(case_switch,num)

#Calcluator using Dictionary
import math as m

def getinput(i = 0):
    if(i == 0):
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        return n1,n2
    elif(i == 1):
        n = int(input("Enter the number:"))
        return n
    
def add():
    x,y = getinput()
    print("Addition is:",x+y)
    return
    
def sub():
    x,y = getinput()
    print("Subtration is:",x-y)
    return
    
def mul():
    x,y = getinput()
    print("Multiplication is:",x*y)
    return
    
def div():
    x,y = getinput()
    print("Division is:",x//y)
    return    
    
def power():
    x,y = getinput()
    print("X raised to y is:",m.pow(x,y))
    return
    
def fact():
    x = getinput(1)
    print("X! is:",m.factorial(x))
    return    

def error():
    print("Invalid Operation Selected!!")
    
calc = {1:add,2:sub,3:mul,4:div,5:power,6:fact,7:exit}
    
while(True):
    print('''
Welcome to PY Calcluator
Note: Please seperate the numbers using comma(,)
Choose operation you want to perform from the list below:
1.Addition
2.Subtration
3.Multiplication
4.Division
5.x raised to y
6.x!
7.Exit
    ''')

    choice = int(input("Select the operation to perform: "))
    calc.get(choice,error)()