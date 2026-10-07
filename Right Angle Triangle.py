# Take input
print("Half pyramid of stars(*): ")
n = int(input("Enter the number of rows:"))
# The Outer Loop for the rows
for i in range(n):
    # The inner loop for columns
    for j in range(i+1):
        # Display result
        print("*",end="")
    print()