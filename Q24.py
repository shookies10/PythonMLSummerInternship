# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

# Main function to handle user input and perform calculations
def main():
    print("Simple Calculator")
    
    try:
        # Take input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        
        # Perform the appropriate calculation based on the operator
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            result = "Error: Invalid operator. Please enter one of +, -, *, /."
        
        print(f"The result is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the main function
if __name__ == "__main__":
    main()
