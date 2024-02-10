# Create a tuple of N elements
n = int(input("Enter the number of elements: "))
numbers = tuple(int(input(f"Enter element {i+1}: ")) for i in range(n))

# Search for a particular number using Linear Search Technique
search_number = int(input("Enter a number to search for: "))

# Initialize a variable to store the index of the found number
index = None

# Use a for loop to iterate over the indices of the elements in the tuple
for i in range(len(numbers)):
    # Get the current number in the tuple using the index
    number = numbers[i]
    # If the current number is equal to the search number, store the index and break the loop
    if number == search_number:
        index = i
        break

# Print the result of the search
if index is not None:
    print(f"The number {search_number} was found at index {index} in the tuple.")
else:
    print(f"The number {search_number} was not found in the tuple.")