def sort_my_list(lst=None):
    if lst is None:
        lst = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    # print(lst)


lllst = [25, 10, 15, 5, 30, 55, 35, 45]
print("my list is formerly ", lllst)
sort_my_list(lllst)
print("my list is now sorted", lllst)
