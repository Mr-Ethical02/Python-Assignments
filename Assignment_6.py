'''
To accept an object mass in kilograms and velocity in meters per second and display its momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is its velocity.
'''
m = float(input("Enter mass of object in Kilograms: "))
v = float(input("Enter velocity of object in m/s"))
p = m*v

print("Momentum of the object is: %.2f" % p)