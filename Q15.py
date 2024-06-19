import csv

# Function to read and print data from CSV file
def read_csv_file(file_name):
    try:
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            print(f"Reading data from '{file_name}':\n")
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")

# Specify the CSV file name
csv_file = "elementsQ15.csv"

# Call the function to read and print data from CSV file
read_csv_file(csv_file)