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