# Input number
num = int(input("Enter a number: "))

# Initialize factorial
factorial = 1

# Compute factorial using for loop
for i in range(1, num + 1):
    factorial *= i

# Display result
print(f"Factorial of {num} is {factorial}")
