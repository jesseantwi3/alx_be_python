# Ask user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop: while loop for rows
while row < size:
    # Inner loop: for loop for printing stars in each row
    for column in range(size):
        print("*", end="")
    # After inner loop, move to next line
    print()
    # Move to next row
    row += 1
