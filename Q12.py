# Function to calculate sum of digits of a number
def sum_of_digits(number):
   
    digit_sum = 0
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number //= 10
    # Return the sum of digits
    return digit_sum

# Take input from user
num = int(input("Enter a number: "))

# Calculate sum of digits and print
result = sum_of_digits(num)
print(f"The sum of digits of {num} is: {result}")