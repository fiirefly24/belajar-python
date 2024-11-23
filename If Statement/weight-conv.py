# Python weight converter

weight = float(input("Enter weight your weight: "))
unit = input("(Kg or Pounds (K/L)): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kg"
else:
    print("Invalid unit")

print(f"Your weight is {round(weight, 1)} {unit}")