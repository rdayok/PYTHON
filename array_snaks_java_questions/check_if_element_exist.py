def does_element_exist(inputted_list=[], element_checked=None):
    for element in inputted_list:
        if element == element_checked:
            exist = True
            return exist
        else:
            exist = False
            return exist


lst = [25, 10, 15, 5, 30, 55, 200, 45]
print(does_element_exist(lst, 300))
