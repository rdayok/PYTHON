my_number_list = []
my_even_number_list = []
# A list of numbers 1 to 20
for number in range(1, 21):
    my_number_list.append(number)
print(my_number_list)

# A new list for the even numbers
for number in range(1, 21, 2):
    my_even_number_list.append(number)
print(my_even_number_list)

# Change the fifth number in the list of even numbers to zero
my_even_number_list[4] = 0
print(my_even_number_list)

# Make the fifth to the tenth number in the even list to be zero
for index in range(4, 10):
    my_even_number_list[index] = 0
print(my_even_number_list)

# Display only the first 7 numbers in the list
print(my_even_number_list[:7])

# Change every number in the even list to zero
for index in range(10):
    my_even_number_list[index] = 0
print(my_even_number_list)

# Clear the list
my_even_number_list[:] = []
print(my_even_number_list)

