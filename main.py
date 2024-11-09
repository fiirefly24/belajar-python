# Strings
first_name = "John"
last_name = "Doe"

# Integers
age = 25

# Booleans
is_student = True

# Floats
height = 1.75

# Lists
languages = ["Python", "Java", "C++"]

# Dictionaries
person = {"name": "John", "age": 25, "city": "New York"}

# Tuples
coordinates = (1, 2, 3)

# Sets
numbers = {1, 2, 3, 4, 5}

# Functions
def greet(name):
    print("Hello, " + name + "!")
    
    
# Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
        
################  MAIN CODE   #################
store_name = "My Store"
time_open = 9
time_closed = 6
isOpen = True
type_of_item = ["beverages", "groceries", "produce"]
beverages = [{"name": "Water", "price": 1.99}, {"name": "Coke", "price": 2.99}]
groceries = [{"name": "Milk", "price": 4.99}, {"name": "Eggs", "price": 3.99}]
produce = [{"name": "Potatoes", "price": 2.99}, {"name": "Carrots", "price": 1.99}]
itemsCart = []

def add(the_item, type_of_item):
    priceItem = next((item["price"] for item in type_of_item if item["name"] == the_item), None)
    found = False
    for item in itemsCart:
        if item["name"] == the_item:
            found = True
            item["qty"] += 1
            item["price"] += item["price"] / item["qty"]
            break
    if not found:
        itemsCart.append({"name": the_item, "qty": 1, "price": priceItem})
    print(f"You Add to {the_item} cart + {priceItem}")

def cancel():
    itemsCart.clear()
    
def buy():
    total = 0
    for item in itemsCart:
        total += item["price"]
    print(f"Total: {total}")
    
def listType():
    for i, item in enumerate(type_of_item, start=1):
        print(f"{i} . {item}")

def menu():
    listType()
    typeItem = input("Enter the number of the item you want to buy: ")

    while typeItem.isdigit() and not 1 <= int(typeItem) <= len(type_of_item) :
        print(f"Invalid input. Please enter a number between 1 and  {len(type_of_item)}")
        typeItem = input("Enter the number of the item you want to buy: ")

    listItem(typeItem)
        
def listItem(typeItem):
        match int(typeItem):
            case 1:
                for i, item in enumerate(beverages, start=1):
                    print(f"{i} . {item['name']} Price: {item['price']}$")
                    
                theItem = input("Enter the number of the item you want to buy: ")
                while theItem.isdigit() and not 1 <= int(theItem) <= len(beverages) :
                    print(f"Invalid input. Please enter a number between 1 and  {len(type_of_item)}")
                    theItem = input("Enter the number of the item you want to buy: ")
                
                match int(theItem):
                    case 1:
                        add('Water', beverages)
                    case 2:
                        add('Coke', beverages)
                
            case 2:
                for i, item in enumerate(groceries, start=1):
                    print(f"{i} . {item['name']} Price: {item['price']}$")
                    
                theItem = input("Enter the number of the item you want to buy: ")
                while theItem.isdigit() and not 1 <= int(theItem) <= len(beverages) :
                    print(f"Invalid input. Please enter a number between 1 and  {len(type_of_item)}")
                    theItem = input("Enter the number of the item you want to buy: ")
                
                match int(theItem):
                    case 1:
                        add('Milk', groceries)
                    case 2:
                        add('Eggs', groceries)
            case 3:
                for i, item in enumerate(produce, start=1):
                    print(f"{i} . {item['name']} Price: {item['price']}$")
                
                theItem = input("Enter the number of the item you want to buy: ")
                match int(theItem):
                    case 1:
                        add('Potatoes', produce)
                    case 2:
                        add('Carrots', produce)

def listItemCart():
    priceItem = 0
    for item in itemsCart:
        print(f"{item['name']} Qty: {item['qty']} Price: {item['price']}$")
        priceItem += item["price"]
    print(f"Total: {priceItem}")

print("Hey you wanna buy something today?")
print("Yeah, I think i want to buy some items at grocery store")
print("Lets go to the grocery store " + store_name)    
if isOpen:
    print("Okay lets go")
else:
    print(f"The store is closed. The Store are open from " + {time_open} + "am to " + {time_closed} + "pm")

print("Welcome to our store")
print("What do you want to buy?")

menu()
addElse = input("Do you want to buy something else? ")

while addElse.lower() == "yes":
    menu()
    addElse = input("Do you want to buy something else? ")
listItemCart()



