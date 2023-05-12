

def no_duplicate_in_list(inputted_list=None):
    duplicate_exist = False
    new_list = []
    for i in range(len(inputted_list)):
        for j in range(i + 1, len(inputted_list)):
            if inputted_list[i] == inputted_list[j]:
                duplicate_exist = True
                new_list.append(inputted_list[i])
    if duplicate_exist:
        print("duplicate exist")
    else:
        print("duplicate doesn't exist")

    print(new_list)


m = [25, 10, 15, 5, "car", "car", "bag", 30, 55, 35, 45]


n = ["nu", "mu", "tu"]

no_duplicate_in_list(m)
