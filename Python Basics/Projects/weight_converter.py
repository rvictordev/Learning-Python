# Weight Converter
print("Weight Converter. Kilograms to Pounds or Pounds to Kilograms")
weight = float(input("What is your weight: "))
unit = input("Type a unit. 'k' for Kilograms 'l' for Pounds: ")
convert_num = 2.205

if unit == "k":
    weight = weight * convert_num
    unit = "l"
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "l":
    weight = weight / convert_num
    unit = "kgs"
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is an invalid unit")
