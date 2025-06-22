# Input sentence
input_sentence = input("Enter a sentence: ")

# Split, reverse and join the words
reversed_sentence = ' '.join(input_sentence.split()[::-1])

# Display the result
print(f"Output after reverse = \"{reversed_sentence}\"")
