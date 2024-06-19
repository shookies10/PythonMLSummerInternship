# Function to check if a substring is in a string
def check_substring():
    # Take the main string input
    main_string = input("Enter the main string: ")
    # Take the substring input
    substring = input("Enter the substring: ")
    # Check if substring is in the main string
    if substring in main_string:
        print("The substring is present in the main string.")
    else:
        print("The substring is not present in the main string.")

# Call the function
check_substring()