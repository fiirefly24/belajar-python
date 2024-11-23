# Python compound interest calculator

principle = 0
rate = 0
time = 0

# It will always enter the loop because the condition is true
# unless you input > 0
while True:
    principle =float(input("enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break
while True:
    rate =int(input("enter the interest rate: "))
    if rate <= 0:
        print("Interest Rate can't be less than or equal to zero")
    else:
        break
while True:
    time =int(input("enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break

total = principle*pow((1+rate/100), time)
print(f"Balance after {time} year/s: ${total:.2f}")