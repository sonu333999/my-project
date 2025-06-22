# Function to compute LCM
def compute_lcm(x, y):
    # Get the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm

# Input numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Calculate and display LCM
lcm = compute_lcm(number1, number2)
print(f"LCM of {number1} and {number2} is: {lcm}")
