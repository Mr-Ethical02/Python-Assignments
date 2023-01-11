'''
Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.
'''

def sumsquare(l):
    sumsq = []
    osum = 0
    esum = 0
    for i in l:
        if(i % 2 == 0):
            esum = esum + (i*i)
        elif(i % 2 == 1):
            osum = osum + (i*i)
    sumsq.append(osum)
    sumsq.append(esum)
    return sumsq

l_list = [1,2,4,7,8,12,9,11]
olist = sumsquare(l_list)

print("Sum of squares of odd numbers is:",olist[0])
print("Sum of squares of even numbers is:",olist[1])