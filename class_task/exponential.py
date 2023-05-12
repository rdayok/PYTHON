def exponential(a):
    return a ** 3


lists = [1, 2, 3, 4, 5, 6]

ans = list(map(exponential, lists))
print(ans)
