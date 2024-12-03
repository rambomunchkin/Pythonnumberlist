# Create a list of 15 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Loop through each number in the list
for number in numbers:
    # Check if the number is even or odd
    if number % 2 == 0:
        # If even, print the message stating that the number is even
        print(str(number) + " is even")
    else:
        # If odd, print the message stating that the number is odd
        print(str(number) + " is odd")
