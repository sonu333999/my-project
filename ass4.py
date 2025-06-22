# Input start and stop values
start = int(input("Enter start number: "))
stop = int(input("Enter stop number: "))

# Initialize sum
odd_sum = 0

# Loop through the range
for num in range(start, stop + 1):
    if num % 2 != 0:
        odd_sum += num

# Display result
print(f"Sum of odd numbers: {odd_sum}")
