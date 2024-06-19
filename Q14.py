def read_and_print_lines():
    lines = []
    while True:
        # Read input line from user
        line = input("Enter a line (or press Enter to finish): ")
        # Check if line is empty
        if line == "":
            break
        # Add line to list
        lines.append(line)
    
    # Print all lines entered by the user
    if lines:
        print("\nThe lines entered are:")
        for line in lines:
            print(line)
    else:
        print("No lines were entered.")

# Call the function to execute the program
read_and_print_lines()