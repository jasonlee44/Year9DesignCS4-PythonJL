username = {}

while True:
    print(" ")
    print("""
    ----Menu----
    1. Login
    2. Signup
    3. Quit
    ------------
    """)
    x = int(input("Please choose an operation: "))

    if x == 2:
        usernameInput = input("Please choose a username: ")
        if usernameInput in username:
            print("This username already exists")
        else:
            passwordInput = input("Please choose a password: ")
            passwordConfirm = input("Please confirm password: ")
            if passwordInput != passwordConfirm:
                print("Passwords do not match")
            else:
                username[usernameInput] = passwordConfirm
                print("Please login")



    if x == 1:
        usernameInput = input("What is your username? ")
        if (usernameInput in username) == False:
            print("Username does not exist")
        else:
            passwordInput = input("What is your password: ")
            if username[usernameInput] != passwordInput:
                print("Wrong passsword!")
            else:
                print("Login Successful")

    if x == 3:
        print("Program Exited")
        break








