# CONDITIONAL EXPRESSION
num = 6
a = 6
b = 7
age = 25
temp = 30
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "Hot" if temp > 20 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
