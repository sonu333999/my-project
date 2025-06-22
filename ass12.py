# Input number
num = int(input("Enter a number: "))
revnum = 0

# Reverse the number using while loop
while num > 0:
    digit = num % 10
    revnum = revnum * 10 + digit
    num //= 10

# Display reversed number
print(f"Reversed number = {revnum}")
