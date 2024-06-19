# Generator function to yield Fibonacci numbers
def generate_fibonacci(n):
    fib1, fib2 = 0, 1
    count = 0
    while count < n:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2
        count += 1

# Take input from user
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate Fibonacci sequence and print
fibonacci_numbers = list(generate_fibonacci(n))
print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")