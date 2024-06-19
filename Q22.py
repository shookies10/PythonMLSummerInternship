# Function to find the minimum and maximum values in a list
def find_min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

# Take input from user
input_numbers = input("Enter a list of numbers separated by space: ")

# Convert input string to a list of numbers
try:
    numbers = list(map(float, input_numbers.split()))
except ValueError:
    print("Error: Please enter valid numbers separated by space.")
    exit()

# Find minimum and maximum values
min_value, max_value = find_min_max(numbers)

# Print the results
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
