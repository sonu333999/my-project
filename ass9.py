# Input list
input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

# Initialize empty frequency dictionary
freq = {}

# Count frequencies
for item in input_list:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

# Display frequency count
print(f"Frequency count: {freq}")
