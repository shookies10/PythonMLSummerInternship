import string

# Function to remove punctuation from a string
def remove_punctuation(input_string):
    # Create translation table with punctuation characters mapped to None
    translator = str.maketrans('', '', string.punctuation)
    # Remove punctuation using translate method
    return input_string.translate(translator)

# Take input string from user
input_string = input("Enter a string with punctuation: ")

# Remove punctuation and print the result
result_string = remove_punctuation(input_string)
print("String without punctuation:", result_string)