"""
Assignment 1
-------------------------------------

This program shows the following: list of an integers, calculated the sum,
calculated the average, and finally find the largest number.
@Author: sulaimon
@Date: Jan 8 2024 
"""

# Create the list
my_list = [5, 0, -10, 4, 9, -5, 13, 26, -17, 18]

# Print each number in the list
for number in my_list:
    print(number)
    

# Initialize a variable to store the sum
total_sum = 0

# Iterate through each number in the list and add it to the sum
for number in my_list:
    total_sum += number

# Display the result
print("The sum of the list is:", total_sum)


# Initialize variables to store the sum and count of elements
total_sum = 0
element_count = 0

# Iterate through each number in the list, add it to the sum, and 
# increment the count
for number in my_list:
    total_sum += number
    element_count += 1

# Check if the list is not empty to avoid division by zero
if element_count != 0:
    # Calculate the average
    average = total_sum / element_count
    # Display the result
    print("The average of the list is:", average)
else:
    print("The list is empty. Cannot calculate the average.")

# Initialize a variable to store the maximum value
# Initialize with negative infinity to ensure any value in the list is greater
max_number = float('-inf')  

# Iterate through each number in the list and update the maximum if needed
for number in my_list:
    if number > max_number:
        max_number = number

# Display the result
print("The largest number in the list is:", max_number)