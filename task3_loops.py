# Task 3: Python program to print all positive numbers in a range

# Example 1
list1 = [12, -7, 5, 64, -14]
print("Input: list1 =", list1)
print("Output:", end=" ")

# Using a for loop to iterate through the list
for num in list1:
    # Check if the number is positive
    if num > 0:
        print(num, end=", ")
print("\b\b ") # Removes the trailing comma

# Example 2
list2 = [12, 14, -95, 3]
print("\nInput: list2 =", list2)

# Using list comprehension for the specific list output format [12, 14, 3]
output2 = [num for num in list2 if num > 0]
print("Output:", output2)
