# Function to count occurrences of a specific element in a list
def count_occurrences(lst, element):
    return lst.count(element)

# Take input list from user
input_list = input("Enter a list of elements separated by space: ").split()

# Take the specific element to count from user
specific_element = input("Enter the element to count: ")

# Count occurrences of the specific element in the list
occurrences = count_occurrences(input_list, specific_element)

# Print the result
print(f"The element '{specific_element}' occurs {occurrences} times in the list.")