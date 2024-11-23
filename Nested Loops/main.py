# NESTED LOOPS
rows = int(input("Enter Rows: "))
cols = int(input("Enter cols: "))
symbol = input("Enter Symbol to use")
for x in range(rows):
    for y in range(cols):
        print(symbol, end="")
    print()
