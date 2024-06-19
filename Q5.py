# Function to write user input to a text file
def write_to_file():
    # Asking the user for a string input
    user_input = input("Please enter a string: ")

    # Opening the file in write mode
    with open("QUESTION5.txt", "w") as file:
        # Writing the user input to the file
        file.write(user_input)

    print("Your input has been written to 'QUESTION5.txt'.")

# Calling the function
write_to_file()