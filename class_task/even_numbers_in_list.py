even = []
for number in range(2, 51, 2):
    even.append(number)
print(even)

even_number = list(range(2, 51, 2))
print(even_number)
print(len(even_number))
a, b, c, d, e, f, g, h, i, j, *others = even_number
print(even_number)
print(a, b, c, d, e, f, g, h, i, j, others)
print(g)
secret_numbers = [1, 2, 3, 4, 5, 6]
x, *others, z = secret_numbers
print(x, others, z)

letters = list("Hello C16")
print(letters)

for index, letter in enumerate(letters):
    print(index, letter)

let = ["a", "t", "z", "q", "m"]
print(let)
let.insert(0, "w")
print(let)
let.remove("z")
print(let)
del let[0:2]
print(let)

list_of_list = [let, letters, letter]
print(list_of_list)


jay = ["Jay", 500, 15, "07036"]
segz = ["Segun", 20, 500, "09045"]
oyi = ["Oyi", 760, 20, "09063"]
rd = ["RD", 1500, 13, "07064"]
torin = ["Torin", 5000, 600, "07043"]
kat_list = [jay, torin, segz, oyi]
print(kat_list)
# change the price for torin
kat_list[2][1] = 50
# change the name for torin
kat_list[1][0] = "Co-founder"
print(kat_list)
# add to the list kat_list
kat_list.append(rd)
print(kat_list)

numbers_even = [i for i in range(21) if i % 2 == 0]
print(numbers_even)
