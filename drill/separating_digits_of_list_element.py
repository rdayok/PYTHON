def separate_digits_of_element(my_list):
    my_new_list = []
    for element in my_list:
        for digit in str(element):
            my_new_list.append(int(digit))

    return my_new_list


mmm = [456, 333, 63, 67, 96446]

print(separate_digits_of_element(mmm))
