rows = int(input("enter the amount of rows: "))
for row in range(1, rows+1 ):
    for space in range(1, (rows-row)+1):
        print(" ", end="")
    for symbol in range(1, row+1):
        print("*", end="")
    print()