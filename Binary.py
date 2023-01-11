def decToBinary(n):
     
    # array to store
    # binary number
    binaryNum = [0] * n
 
    # counter for binary array
    i = 0;
    while (n > 0):
 
        # storing remainder
        # in binary array
        binaryNum[i] = n % 2
        n = int(n / 2)
        i += 1
 
    # printing binary array
    # in reverse order
    
    # printing extra 0's for creating 4 bit sets
    if(i % 4 != 0):
        x = 4 - (i % 4)
        for k in range(0,x):
            print(0, end = "")
    # printing rest binary value
    for j in range(i-1, -1, -1):
        print(binaryNum[j], end = "")
        

# Driver Code
n = int(input("Enter a number to convert:\n"))
decToBinary(n)