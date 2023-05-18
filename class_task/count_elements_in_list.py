lst = ["male", "female", "female", "male", "male", "male", "female"]
males = 0
females = 0

for element in lst:
    if element == "male":
        males += 1
    else:
        females += 1

first_tuple = tuple(["males", males])
second_tuple = tuple(["females", females])
lssst = [first_tuple, second_tuple]
print(list(lssst))


