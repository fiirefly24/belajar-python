# STRING METHOD
name = input("Enter your full name: ")
phone_number = input("Enter your Phone Number: ")
result = len(name) #The length of the strings (include spaces too)
result = name.find(" ") #Find the index of a substring
result = name.rfind(" ") #Find the index of a substring from behind, r means reverse
name = name.capitalize() #To capitalizes the first letter of the string name, and converts all other letters to lowercase.
name = name.upper() #converts all characters in the string name to uppercase letters.
name = name.lower() #converts all characters in the string name to lowercase letters.
result = name.isdigit() #To checks whether all characters in the string name are digits (0-9)
result = name.isalpha() #checks whether all characters in the string name are alphabetic (A-Z)
result = phone_number.count("-") #counts how many times the character "-" appears in the string phone_number
result = phone_number.replace("-","") #eplaces all occurrences of the character "-" in the string phone_number with an empty string ""
print(result)
