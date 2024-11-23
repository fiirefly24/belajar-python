# validate user input exercise
    # 1. username is no more than 12 characters
    # 2. username must not contain spaces
    # 3. username must not contain digits

print("Sign up!")
print("Username is no more than 12 chars, and not contain spaces and digits")    
username = input("Create your username: ")
if len(username) > 12:
    print("Username is no more than 12 characters")
elif username.find(" ") > -1:
    print("username must not contain spaces")
elif not username.isalpha():
    print("username must not contain digits")
else:
    print("Your username is validated")


# if len(username) > 12 or not username.isalpha():
#     print("Your username is more than 12 characters or it may contains spaces or digits!")
# else:
#     print("Your username is validated!")