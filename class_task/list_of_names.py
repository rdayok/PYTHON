lst = []
# count = 0
print("Enter names with letters not less than 1 or greater than 10")
for name in range(10):
    name = input('Enter a name:\n')
    if 10 >= len(name) > 1 and name != "":
        lst.append(name)
    else:
        while 10 < len(name) or len(name) < 2 or name == "":
            print("enter a valid name")
            name = input('Enter a name:\n')
            if 10 >= len(name) > 1 and name != "":
                lst.append(name)


print(lst)
