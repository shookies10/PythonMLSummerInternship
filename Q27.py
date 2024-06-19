# Function to convert a string into a list of its characters
def string_to_char_list(string):
    return list(string)

# Main function to handle user input and perform the conversion
def main():
    string = input("Enter a string: ")
    char_list = string_to_char_list(string)
    print(f"The list of characters is: {char_list}")

# Run the main function
if __name__ == "__main__":
    main()
