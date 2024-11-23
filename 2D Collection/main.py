# 2D COLLECTION
fruits = ["Apple", "Orange", "Banana", "Coconut"]
vegetables = ["Celery", "Carrots", "Potatoes"]
meats = ["Chicken", "Fish","Turkey"]

groceries = [fruits, vegetables, meats]

for list in groceries:
    for item in list:
        print(item, end=" ")
    print()
    
numpad = ((1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            ("*", 0, "#"))

for row in numpad:
    for num in row:
        print(num, end=" ")
    print()    
