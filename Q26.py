# Function to check if a string starts with a given prefix
def starts_with(string, prefix):
    return string.startswith(prefix)

# Function to check if a string ends with a given suffix
def ends_with(string, suffix):
    return string.endswith(suffix)

# Main function to handle user input and perform the checks
def main():
    string = input("Enter the string: ")
    prefix = input("Enter the prefix to check: ")
    suffix = input("Enter the suffix to check: ")

    # Check if the string starts with the given prefix
    if starts_with(string, prefix):
        print(f"The string starts with '{prefix}'.")
    else:
        print(f"The string does not start with '{prefix}'.")

    # Check if the string ends with the given suffix
    if ends_with(string, suffix):
        print(f"The string ends with '{suffix}'.")
    else:
        print(f"The string does not end with '{suffix}'.")

# Run the main function
if __name__ == "__main__":
    main()

