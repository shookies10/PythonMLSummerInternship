# Function to calculate sum of numbers in a list
def calculate_sum(numbers):
    total_sum = sum(numbers)
    return total_sum

# Take input from user
input_numbers = input("Enter a list of numbers separated by space: ")

# Convert input string to list of numbers
try:
    numbers = list(map(float, input_numbers.split()))
except ValueError:
    print("Error: Please enter valid numbers separated by space.")
    exit()

# Calculate sum of numbers and print
sum_of_numbers = calculate_sum(numbers)
print(f"The sum of numbers is: {sum_of_numbers}")