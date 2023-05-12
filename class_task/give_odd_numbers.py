lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def odd_numbers(a):
    if a % 2 != 0:
        return a


ans = list(filter(odd_numbers, lst))

print(ans)


def odd_num(lsttt):
    odd = []
    for n in lsttt:
        if n % 2 != 0:
            odd.append(n)
    return odd


print(odd_num(lst))

man = {a: a % 2 != 0 for a in range(1, 11)}
print(f"this is {man}")
