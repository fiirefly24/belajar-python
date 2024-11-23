# LOGICAL OPERATORS
# OR
temp = 25
is_raining = True
if temp > 35 or temp < 0 or is_raining:
    print("The Outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
temp = 20
is_sunny = False

# AND
if temp >= 28 and is_sunny:
    print("It is Hot Outside")
    print("it is Sunny")
elif temp <= 0 and is_sunny:
    print("It is Cold Outside")
    print("it is Sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is Warm Outside")
    print("it is Sunny")
#NOT
elif temp <= 0 and not is_sunny:
    print("It is Cold Outside")
    print("it is Coudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is Warm Outside")
    print("it is Coudy")
