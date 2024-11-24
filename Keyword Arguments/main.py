# def hellow(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# # place keyword of argument    
# hellow( last="Squartepants", first="Spongebob", greeting="Hello", title="Mr.")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=62, area=898, first=881, last=2250)

print(phone_num)