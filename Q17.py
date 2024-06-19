# Function to convert string to title case
def convert_to_title_case(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Capitalize the first letter of each word and join them back
    title_case_string = ' '.join(word.capitalize() for word in words)
    
    return title_case_string

# Take input string from user
input_string = input("Enter a string: ")

# Convert input string to title case
title_case_string = convert_to_title_case(input_string)

# Print the title cased string
print("Title cased string:")
print(title_case_string)