# Input number
num = int(input("Enter a number: "))

# Function to compute sum of digits
def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

# Keep reducing until single digit
while num >= 10:
    num = sum_digits(num)
    print(f"Intermediate sum = {num}")

# Display final single digit sum
print(f"Final Output: {num}")
