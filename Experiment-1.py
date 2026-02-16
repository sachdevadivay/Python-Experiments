# Create a variable to store your age and print its type using type().

a = 19
print(type(a))

# Declare a string variable called x and assign it the value “Hello”.

x = "Hello"
print(x)

# Take different data types and print values using print function.



a = input("enter your age:")
b = input("enter your name:")
c = input("enter your city:")
print(a)
print(b)
print(c)

# Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign a value of 7 to y, perform addition, multiplication, division and subtraction on these two variables and Print out the result.

x = 9
y = 7
print(x+y)
print(x*y)
print(x-y)
print(x/y)

# Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem. 



import math


a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = math.sqrt(a*a + b*b)
print("The length of the hypotenuse is:", c)

# Write a program to find simple interest.



p = float(input("Enter the value of principle:"))
r = float(input("Enter the value of rate:"))
t = float(input("Enter the time:"))

SI = (p*r*t)/100
print("Simple interest:", SI)

# Write a program to find area of triangle when length of sides are given.



a = float(input("side1:"))
b = float(input("side2:"))
c = float(input("side3:"))
s = float((a+b+c)*0.5)
r = math.sqrt(s*(s-a)*(s-b)*(s-c)*1/2)
print(r)

# Write a program to convert given seconds into hours, minutes and remaining seconds.

seconds = int(input("Enter total seconds: "))


hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
remaining_seconds = seconds % 60


print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remaining_seconds)

# Write a program to swap two numbers without taking additional variable.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


a = a + b
b = a - b
a = a - b


print("After swapping:")
print("a =", a)
print("b =", b)

# Write a program to find sum of first n natural numbers.

n = int(input("enter the value of n :"))
sn = (n*(n+1))*0.5
print(sn)
