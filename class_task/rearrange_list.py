lst = [25, 10, 15, 5, 30, 55, 35, 45]
number =0
index = 0
index2 = 1
print(lst.sort())
for i in range(len(lst)):
    print("i is", i)
    for j in range(i + 1, len(lst)):
        print("inner i is", i)
        print("j is", j)
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(lst)
