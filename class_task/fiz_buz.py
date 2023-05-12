def fiz_buz(integer):
    if integer % 3 == 0 and integer % 5 == 0:
        print("FizBuz")
    elif integer % 3 == 0:
        print("Fiz")
    elif integer % 5 == 0:
        print("Buz")


number = int(input("Enter a number: \n"))
fiz_buz(number)
