

def is_palindrome(user_input):
    swap = user_input[:: -1]
    swap = swap.lower()

    if swap == user_input.lower():
        print(user_input + ' is a palindrome')
    else:
        print(user_input + ' is not a palindrome')


userinput = input("Enter a word to know if it is a palindrome\n")
is_palindrome(userinput)
