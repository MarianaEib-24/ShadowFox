#Question 1
pi = 22/7
print(type(pi)) #output: class 'float'

#Question 2
for = 4 #This returns a syntax error because 'for' is a keyword in python and is used in creating loops,thus cannot be used as a variable name

#Question 3
"""let
principal amount be P
interest rate be R
time in years be T """
P = 500
R = 5
T = 3
simple_interest = (P*R*T) / 100
print (simple_interest) #output: 75.0

#Section 2:Numbers
def format_text(a,b):
    result = format(format_text(a,b))
    return result
format_text(145,"o")

#2
radius = 84
π = 3.14
π = int(π)
Circle_Area = π * (radius**2)
water_in_pond = Circle_Area // 1.4
water_in_pond = int(water_in_pond)
print ("The area of the pond is",Circle_Area,"square metres")
print(f"The total amount of water is",water_in_pond)

#3
distance = 490
minutes = 7
minutes_to_seconds = minutes * 60
speed = distance / minutes_to_seconds
print("Your speed is {} metres per second".format(speed) )



