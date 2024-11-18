# VARIABLES
    # # Strings
    # first_name = "John"
    # last_name = "Doe"

    # # Integers
    # age = 25

    # # Booleans
    # is_student = True

    # # Floats
    # height = 1.75

# TYPE CASTING
    # name = "Bro Code" #string #bool(name), the value is true and will be false if there is no value in name
    # age = 25    #int #float(age), the value will be 25.0
    # gpa = 3.2   #float #int(gpa), the value will be 3
    # is_Student = True #bool #str(is_Student), the value will be "True"

# INPUT DATA
    # name = input("What is your name? ")
    # print(name)
    # length = int(input("Enter the length of the rectangle: "))
    # width = int(input("Enter the width of the rectangle: "))
    # area = length * width
    # print(f"The area of the rectangle is {area}"

# ARITHMETIC OPERATORS
    # friends = 10
    # friends = friends + 1 #Addition
    # friends += 1 #Addition with assign the result back to the variable.
    # friends = friends - 2 #Subtraction
    # friends -= 2 #Subtraction with assign the result back to the variable.
    # friends = friends * 3 #Multiplication
    # friends *= 3 #Multiplication with assign the result back to the variable.
    # friends = friends / 2 #Division
    # friends /= 2 #Division with assign the result back to the variable.
    # friends = friends ** 2 #Exponential
    # friends **= 2 #Exponential with assign the result back to the variable.
    # remainder = friends % 3 #Modulus
    # import math
    # x = 3.14
    # y = 4
    # z = 5
    # result = round(x) #Rounding a number
    # result = abs(y) #Absolute value
    # result = pow(4, 3) #Exponentiation
    # result = max(x, y, z) #Finding the maximum
    # result = min(x, y, z) #Finding the minimum
    # math.pi #mathematical constants like pi
    # math.e #mathematical constants like e
    # result = math.sqrt(25) #Square root
    # result = math.ceil(x) #Ceiling Rounding up
    # result = math.floor(x) #Floor Rounding down
    # radius = float(input("Enter the radius of the circle: "))
    # circumference = 2 * math.pi * radius #Circumference of a circle
    # area = math.pi * pow(radius, 2) #Area of a circle
    # a = float(input("Enter the side A of the triangle: "))
    # b = float(input("Enter the side B of the triangle: "))
    # c = math.sqrt(pow(a, 2) + pow(b, 2)) #Hypotenuse of a triangle
    
# If Statements    
    # age = int(input("How old are you? "))
    # if age >= 100:
    #     print("You are too old to sign up!")
    # elif age >= 18:
    #     print("You are now signed up!")
    # elif age < 0 :
    #     print("You haven't been born yet!")
    # else:
    #     print("You must be 18+ to sign up!") 
        
    # response = input("Would you like food? (Y/N)")
    # if response == "Y":
    #     print("Here is your food!")
    # else:
    #     print("No food for you!")
        
    # name = input("What is your name? ")
    # if name == "":
    #     print("You didn't enter a name!")
    # else:
    #     print(f"Your name is {name}")
        
    # for_sale = True
    # if for_sale:
    #     print("The item is for sale!")
    # else:
    #     print("The item is not for sale!")

# LOGICAL OPERATORS
    #OR
        # temp = 25
        # is_raining = True
        # if temp > 35 or temp < 0 or is_raining:
        #     print("The Outdoor event is cancelled")
        # else:
        #     print("The outdoor event is still scheduled")
    # temp = 20
    # is_sunny = False
    #AND
        # if temp >= 28 and is_sunny:
        #     print("It is Hot Outside")
        #     print("it is Sunny")
        # elif temp <= 0 and is_sunny:
        #     print("It is Cold Outside")
        #     print("it is Sunny")
        # elif 28 > temp > 0 and is_sunny:
        #     print("It is Warm Outside")
        #     print("it is Sunny")
    #NOT
        # elif temp <= 0 and not is_sunny:
        #     print("It is Cold Outside")
        #     print("it is Coudy")
        # elif 28 > temp > 0 and not is_sunny:
        #     print("It is Warm Outside")
        #     print("it is Coudy")
# CONDITIONAL EXPRESSION
    # num = 6
    # a = 6
    # b = 7
    # age = 25
    # temp = 30
    # user_role = "admin"

    # print("Positive" if num > 0 else "Negative")
    # result = "EVEN" if num % 2 == 0 else "ODD"
    # max_num = a if a > b else b
    # min_num = a if a < b else b
    # status = "Adult" if age >= 18 else "Child"
    # weather = "Hot" if temp > 20 else "Cold"
    # access_level = "Full Access" if user_role == "admin" else "Limited Access"
# STRING METHOD
    # name = input("Enter your full name: ")
    # phone_number = input("Enter your Phone Number: ")
    # result = len(name) #The length of the strings (include spaces too)
    # result = name.find(" ") #Find the index of a substring
    # result = name.rfind(" ") #Find the index of a substring from behind, r means reverse
    # name = name.capitalize() #To capitalizes the first letter of the string name, and converts all other letters to lowercase.
    # name = name.upper() #converts all characters in the string name to uppercase letters.
    # name = name.lower() #converts all characters in the string name to lowercase letters.
    # result = name.isdigit() #To checks whether all characters in the string name are digits (0-9)
    # result = name.isalpha() #checks whether all characters in the string name are alphabetic (A-Z)
    # result = phone_number.count("-") #counts how many times the character "-" appears in the string phone_number
    # result = phone_number.replace("-","") #eplaces all occurrences of the character "-" in the string phone_number with an empty string ""
    # print(result)

# INDEXING
    # credit_number = "1234-5678-9012-3456"
    # # print(credit_number[0])
    # # print(credit_number[:4])
    # # print(credit_number[5:9])
    # # print(credit_number[5:])
    # # print(credit_number[-5])
    # # print(credit_number[::3])
    # # print("XXXX-XXXX-XXXX-"+credit_number[-4:])

# FORMAT SPECIFIERS
    # price1 = 3.14159
    # price2 = -987.65
    # price3 = 12.34
    # print(f"Price 1 is ${price1:+,.2f} ")
    # print(f"Price 2 is ${price2:+10.4f} ")
    # print(f"Price 3 is ${price3:>10} ")

# WHILE LOOP
    # name = input("Enter your name: ")
    # while name == "":
    #     print("You did not enter name")
    #     name = input("Enter your name: ")
    # print(f"Your name is {name}")
    # age = int(input("Enter your age: "))
    # while age < 18:
    #     print("You can't enter!")
    #     age = int(input("Enter your age: "))
    # print(f"Your age is {age}")
    # num = int(input("Enter a $ between 1 - 10: "))
    # while num < 1 or num > 10:
    #     print(f"{num} is not valid")
    #     num = int(input("Enter a $ between 1 - 10: "))
    # print(f"your number is {num}")

# FOR LOOPS
    # credit_card = "1234-5678-9012-3456"
    # for x in credit_card:
    #     print(x)

# NESTED LOOPS
    # rows = int(input("Enter Rows: "))
    # cols = int(input("Enter cols: "))
    # symbol = input("Enter Symbol to use")
    # for x in range(rows):
    #     for y in range(cols):
    #         print(symbol, end="")
    #     print()
    
# COLLECTION
    # list_fruits = ["Apple","Orange","Banana", "Coconut"]
    # set_fruits = {"Apple","Orange","Banana", "Coconut"}
    # tuple_fruits = ("Apple","Orange","Banana", "Coconut")

    # len(list_fruits)
    # "Pineapple" in list_fruits
    # list_fruits[0] = "Mango"
    # list_fruits.append("Pineapple")
    # list_fruits.remove("Coconut")
    # list_fruits.insert(1, "Watermelon")
    # list_fruits.sort()
    # list_fruits.reverse()
    # list_fruits.index("Orange")
    # list_fruits.count("Mango")

    # len(set_fruits)
    # "Pineapple" in set_fruits
    # set_fruits.add("Mango")
    # set_fruits.remove("Banana")
    # set_fruits.pop()
    # set_fruits.clear()
    # len(tuple_fruits)
    # tuple_fruits.index("Apple")
    # tuple_fruits.count("Banana")
    # print(list_fruits)
    
# 2D COLLECTION
    # fruits = ["Apple", "Orange", "Banana", "Coconut"]
    # vegetables = ["Celery", "Carrots", "Potatoes"]
    # meats = ["Chicken", "Fish","Turkey"]

    # groceries = [fruits, vegetables, meats]

    # for list in groceries:
    #     for item in list:
    #         print(item, end=" ")
    #     print()
        
    # numpad = ((1, 2, 3),
    #           (4, 5, 6),
    #           (7, 8, 9),
    #           ("*", 0, "#"))

    # for row in numpad:
    #     for num in row:
    #         print(num, end=" ")
    #     print()    
################  MAIN CODE   #################
