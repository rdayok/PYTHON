def list_largest_element(inputted_list=[]):
    largestElement = 0
    for i in range(len(inputted_list)):
        if i == 0:
            largestElement = inputted_list[i]
        elif inputted_list[i] > largestElement:
            largestElement = inputted_list[i]

    return largestElement


lst = [25, 10, 15, 5, 30, 55, 200, 45]

num = list_largest_element(lst)
print(num)
