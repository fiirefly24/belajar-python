# If Statements    
age = int(input("How old are you? "))
if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0 :
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up!") 
    
response = input("Would you like food? (Y/N)")
if response == "Y":
    print("Here is your food!")
else:
    print("No food for you!")
        
name = input("What is your name? ")
if name == "":
    print("You didn't enter a name!")
else:
    print(f"Your name is {name}")
        
for_sale = True
if for_sale:
    print("The item is for sale!")
else:
    print("The item is not for sale!")
