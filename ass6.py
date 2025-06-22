# Input number
num = int(input("Enter a number: "))

# Initialize sum of divisors
sum_divisors = 0

# Find divisors and calculate sum
for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

# Check if perfect number
if sum_divisors == num:
    print("Yes, it is a Perfect Number")
else:
    print("No, it is not a Perfect Number")
