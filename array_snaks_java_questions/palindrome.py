

def check_if_palindrome(input):
    swap = userinput[:: -1]
    lowerswap = swap.lower()
    finalword = lowerswap.title()

    if finalword == userinput:
        print(finalword + ' is a palindrome')
    if finalword != userinput:
        print(userinput + ' is not a palindrome')


userinput = input("Enter a word to know if it is a palindrome\n")
check_if_palindrome(userinput)

