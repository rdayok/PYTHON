import random


def lucky_game():
    system_number = random.randrange(1, 10)
    lucky_number = 0
    while lucky_number != system_number:
        lucky_number = int(input("Please enter your lucky number:\n"))
        if lucky_number == system_number:
            print("You just got the right number. Hey Champ")


lucky_game()
