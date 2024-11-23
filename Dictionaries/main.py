# Dictionaries
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(dir(capitals))
    # print(capitals.get("USA"))
    # if capitals.get("Russia"):
    #     print("That capital exists")
    # else:
    #     print("That capital doesnt exists")
capitals.update({"Germany": "Berlin"}) # Add key value or update the existing one
capitals.pop("China") # Remove specified key and return the corresponding value.
capitals.popitem() # Remove the latest key value
capitals.clear() # Will clear the dictionaries

keys = capitals.keys() # Return a set-like object providing a view on the dict's keys.
values = capitals.values() # Return an object providing a view on the dict's values.
items = capitals.items() # Return a set-like object providing a view on the dict's items.
print(keys)