# Get two integers from the user
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

# Calculate the sum
    sum = num1 + num2

# Display the result
    print(sum)
except ValueError:
    print("please enter a valid interger")
