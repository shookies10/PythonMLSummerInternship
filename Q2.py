# Function to check whether a number is even or odd
def EvenOrOdd():
    # Taking input from the user
    number = int(input("Enter a number: "))

    # Checking if the number is even or odd
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

# Calling the function
EvenOrOdd()