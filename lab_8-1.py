def sum_up_to_n():
    # Prompt the user to input an integer
    user_input = int(input("Enter an integer: "))

    # Initialize a variable to store the sum
    total_sum = 0

    # Use a for loop and the range function to find the sum
    for x in range(1, user_input + 1):
        total_sum += x

    # Return the final total
    return total_sum

# Call the function and store its output as a variable
result = sum_up_to_n()

# Print the variable to see the final sum
print("The sum of numbers up to the input is:", result)
