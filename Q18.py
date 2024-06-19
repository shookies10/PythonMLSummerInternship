from collections import Counter

# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Use Counter to count frequency of each character
    return Counter(str1) == Counter(str2)

# Take two input strings from user
input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

# Check if the strings are anagrams
if are_anagrams(input_str1, input_str2):
    print(f'"{input_str1}" and "{input_str2}" are anagrams.')
else:
    print(f'"{input_str1}" and "{input_str2}" are not anagrams.')