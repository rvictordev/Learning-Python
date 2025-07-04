# Temperature Conversion Program
import math

unit = input("Select a unit. Type 'f' for Fahrenheit or 'c' Celsius: ")
temp = float(input("Enter a temperature: "))

if unit == "f":
    temp = round((temp - 32) * (5/9), 1)
    print(f"The temperature Celsius is: {temp}°C")
elif unit == "c":
    temp = round(temp * (9/5) + 32, 1)
    print(f"The temperature Fahrenheit is: {temp}°F")
else:
    print(f"{unit} is an invalid unit of measurement")