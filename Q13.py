# Function to calculate age based on birth year
def calculate_age(birth_year):
    current_year = 2024  # Assuming the current year is 2024
    age = current_year - birth_year
    return age

# Take input from user
birth_year = int(input("Enter your birth year: "))

# Calculate age and print
age = calculate_age(birth_year)
print(f"You are {age} years old.")