size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    col = 0
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after printing one row
    row += 1
