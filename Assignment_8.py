'''To accept two numbers from user and compute smallest divisor and Greatest Common Divisor of these two numbers.'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
l1 = []
l2 = []
def gcd(n1,n2):
    for i in range(2,n1+1):
        if(n1%i==0):
            l1.append(i)
    for i in range(2,n2+1):
            if(n2%i==0):
                l2.append(i)
    for i in range(0,len(l1)):
        if(l2.count(l1[i])>0):
            continue
        else:
            try:
                while(l2.count(l1[i]) == 0):
                    pos = l1.index(l1[i])
                    l1.pop(pos)
            except:
                break
    l1.sort()
    print("Smallest Divisor is:",l1[0])
    print("Greatest Common Divisor is:",l1[len(l1)-1])
    
gcd(num1,num2)