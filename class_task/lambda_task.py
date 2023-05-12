lst = []
for n in range(1, 11):
    lst.append(n)

print(lst)


def square(n):
    return n ** 2


print(list(map(square, lst)))

print()