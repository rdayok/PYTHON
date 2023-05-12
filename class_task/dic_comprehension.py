doubles = {}
for a in range(1, 11):
    doubles[a] = a ** 2

# print(doubles)

# or
double_dictionary = {a: a**2 for a in range(1, 11)}
double_list = [a**2 for a in range(11)]
double_tuple = tuple(a**2 for a in range(11))
print(double_dictionary)
print(double_list)
print(double_tuple)

