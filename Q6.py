# Function to read and print the content of a text file
def read_and_print_file():
    # The name of the file to be read
    file_name = "QUESTION5.txt"

    try:
        # Opening the file in read mode
        with open(file_name, "r") as file:
            # Reading the content of the file
            content = file.read()
        
        # Printing the content to the console
        print("The content of the file is:\n")
        print(content)
    
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

# Calling the function
read_and_print_file()

