def user_name_generator(email):
    user_name = ""
    for letter in email:
        if letter == '@':
            return user_name
        user_name = user_name + letter[::1]


mail = input("Enter your email:\n")
print(user_name_generator(mail))
