import random
count = 1
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
while count <= 10000:
    kites = random.randint(1, 6)
    if kites == 1:
        one += 1
    elif kites == 2:
        two += 1
    elif kites == 3:
        three += 1
    elif kites == 4:
        four += 1
    elif kites == 5:
        five += 1
    elif kites == 6:
        six += 1
    count += 1

print(one, two, three, four, five, six)
