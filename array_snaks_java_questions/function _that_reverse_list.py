def reverse_list(inputted_list=[]):
    reversed_list = inputted_list[::-1]
    return reversed_list


lst = [25, 10, 15, 5, 30, 55, 200, 45]
print(reverse_list(lst))
