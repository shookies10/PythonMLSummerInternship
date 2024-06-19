from collections import Counter

# Function to count frequency of each character in a string
def count_character_frequency(input_string):
    # Using Counter to count frequency of each character
    frequency = Counter(input_string)
    return frequency

# Take input string from user
input_string = input("Enter a string: ")

# Calculate frequency of each character in the input string
char_frequency = count_character_frequency(input_string)

# Print frequency of each character
print("Character frequencies:")
for char, freq in char_frequency.items():
    print(f"{char}: {freq}")