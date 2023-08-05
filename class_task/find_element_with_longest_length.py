def find_element_with_longest_length(lst):
    longest_element = ""
    for element in lst:
        if len(element) > len(longest_element):
            longest_element = element
    return tuple([longest_element, len(longest_element)])


my_list = ["will", "mano", "emmanuel", "NoEvenReasonSayYouFitDoSmall"]
print(find_element_with_longest_length(my_list))
