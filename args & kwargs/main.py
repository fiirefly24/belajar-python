def add(*args): # using *args makes the type of the value is a tuple
    total = 0
    for arg in args:
        total += arg
    return total
print(add(2,4,5,6,7))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Spongebob", "Eugene", "Squarepandt")

def print_address(**kwargs): # using **kwargs makes the type of the value is a dictionary
#    for value in kwargs.values(): # take the values
#    for key in kwargs.keys(): # take the keys
    for key, value in kwargs.items(): # take the keys and values
        print(f"{key}: {value}", end=" ")

print_address(street="123 Fake Street",
              apt="100", 
              city="Detroit", 
              state="MI", 
              zip="5464")