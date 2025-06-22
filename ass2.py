# Get input from the user
s = input("Enter a string: ")

# Initialize counters
letters = 0
digits = 0

# Loop through each character
for char in s:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
           digits += 1

# Display the result
print(f"Alphabets: {letters} & Number: {digits}")