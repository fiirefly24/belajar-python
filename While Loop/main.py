# WHILE LOOP
name = input("Enter your name: ")
while name == "":
    print("You did not enter name")
    name = input("Enter your name: ")
print(f"Your name is {name}")

age = int(input("Enter your age: "))
while age < 18:
    print("You can't enter!")
    age = int(input("Enter your age: "))
print(f"Your age is {age}")

num = int(input("Enter a $ between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a $ between 1 - 10: "))
print(f"your number is {num}")
