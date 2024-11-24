## Without argument
# def happy_birthday():
#     print("Happy Birthday!")
# happy_birthday()

## Without argument
# def happy_birthday(name, age):
#     print(f"Happy Birthday {name}!")
#     print(f"You are {age} years old!")
# happy_birthday("Kucing", 20)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
# display_invoice("Fikri", 50, "02/12")

## return = statement used to end a function and send a result back to the caller
# def add(x, y):
#     z = x + y
#     return z # Need to return otherwise the value is None    
# print(add(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("bro", "code")
print(full_name)
