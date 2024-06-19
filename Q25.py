def copy_file(source_file, destination_file):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as src:
            # Read the contents of the source file
            contents = src.read()
        
        # Open the destination file in write mode
        with open(destination_file, 'w') as dest:
            # Write the contents to the destination file
            dest.write(contents)
        
        print(f"Contents of {source_file} have been copied to {destination_file}.")
    except FileNotFoundError:
        print(f"Error: {source_file} not found.")
    except IOError as e:
        print(f"Error: {e}")

# Main function to get file names from the user
def main():
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")
    copy_file(source_file, destination_file)

# Run the main function
if __name__ == "__main__":
    main()
