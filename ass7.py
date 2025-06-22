# Input strings
string1 = input("Enter first string: ").replace(" ", "").lower()
string2 = input("Enter second string: ").replace(" ", "").lower()

# Check if sorted characters are same
if sorted(string1) == sorted(string2):
    print("True")
else:
    print("False")
