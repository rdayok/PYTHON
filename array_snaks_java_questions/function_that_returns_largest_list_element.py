def get_largest_element(inputted_list=None):
    largest_element = inputted_list[0]
    for i in range(len(inputted_list)):
        if inputted_list[i] > largest_element:
            largest_element = inputted_list[i]

    return largest_element


lst = [25, 10, 15, 5, 30, 55, 200, 45]

num = get_largest_element(lst)
print(num)
