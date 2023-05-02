integer = int(input("Enter and integer: \n"))
if integer >= 0:
    if integer % 2 == 0:
        print(f"The integer {integer} inputted is an even number")
    else:
        print(f"The integer {integer} inputted is an odd number")
else:
    print("You entered a negative number")
