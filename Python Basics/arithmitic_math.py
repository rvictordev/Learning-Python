# Basic Arithmetic Operations
# Addition, Subtraction, Multiplication, Divison, Exponentation, Modulos

# friends = 10

# friends = friends + 1
# friends += 1 # Augmented assignment operators
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 2
# friends = friends / 3
# friends /= 2
# friends = friends ** 2
# friends **= 2

# remainder = friends % 4
# print(remainder)

# Built-in Math related functions

# x = 3.14
# y = 4
# z = 5

# result = round(x) # -> round to the nearest whole number
# result = abs(y) # -> distance away from 0 as a whole number
# result = pow(4,3) # pow is an mathematical built-in function for exponentials
# result = max(x,y,z) # return the highest number value
# result = min(x,y,z) # return the lowest number value

# print(result)

# import math

# x = 9.1

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)

# print(result)

import math

# Math Exercise 1: Calculate the Circumference of a circle
# radius = float(input("Enter a radius: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference of the circle is: {round(circumference, 2)}cm")

# Math Exercise 2: Calculate the Area of a circle
# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * math.pow(radius, 2)

# print(f"The Area of the circle is: {round(area,2)}cm²")

# Math Exercise 3: Find the Hypotenuse of a Right Triangle
a = float(input("Enter the A side:"))
b = float(input("Enter the B side:"))

hypotenuse = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"The hypotenuse of a triangle is: {round(hypotenuse,2)}cm")
