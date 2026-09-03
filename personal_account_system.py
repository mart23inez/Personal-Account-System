print("Welcome!")

username = "ADMIN"
password = "PASSWORD"

while True:
    AccVerification = input("Do you have an account with us?: (Y/N)").strip().upper()
    hasAccount = False
    if AccVerification == "Y":
        hasAccount = True
        break
    elif AccVerification == "N":
        hasAccount = False
        break
    else:
        print("Error: Invalid input, please try again.")


if hasAccount:
    attempts = 0
    while attempts < 3:
        inputusername = input("Please enter your username: ")
        inputpassword = input("Please enter your password: ")
        if inputusername == username and inputpassword == password:
            print("Login successful!")
            break
        else:
            print("Error: Incorrect username or password, please try again.")
            attempts += 1
            if attempts >= 3:
                print("Error: Too many attempts. Goodbye!")
                exit()
else:

    username = ""
    password = ""
    passwordverify = ""
    usermin = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#$%^&*()"

    while True:

        username = input("Please enter a username (Must be between 8 - 16 characters and include at least 1 number or special character 0-9): ")
        securedUP = False
        index = 0
        verification = False

        if len(username) < 8:
            print("Error: Username must be at least 8 characters, please try again.")
        elif len(username) > 16:
            print("Error: Username must be 16 characters or fewer, please try again.")
        else:
            verification = True

        if verification:
            while index < len(usermin):
                verify = usermin[index]
                if verify in username:
                    securedUP = True
                    break
                else:
                    index += 1
            else:
                print("Error: Username must include 1 number or special character, please try again.")
        if securedUP:
            break

    while True:

        password = input("Please enter a password (Must be between 8 - 16 characters and include at least 1 number or special character 0-9): ")
        securedUP = False
        index = 0
        verification = False

        if len(password) < 8:
            print("Error: Password must be at least 8 characters, please try again.")
        elif len(password) > 16:
            print("Error: Password must be 16 characters or fewer, please try again.")
        else:
            verification = True

        if verification:
            while index < len(usermin):
                verify = usermin[index]
                if verify in password:
                    securedUP = True
                    break
                else:
                    index += 1
            else:
                print("Error: Password must include 1 number or special character, please try again.")
        if securedUP:
            passwordverify = input("Please enter the password again: ")
            if passwordverify == password:
                print("Account successfully created.")
                break
            else:
                print("Error: Passwords must match, please try again.")

print(f"Welcome {username}!")

print("What would you like to do?")
print("(1) To-do list")
print("(2) Notes")
print("(3) Exit")

while True:
    try:
        option = int(input("What would you like to do? (1 2 3): "))
        if option == 1 or option == 2 or option == 3:
            break
        else:
            print(f"Error: Not a valid input, please try again.")
    except ValueError:
        print(f"Error: Not a valid input, please try again.")

if option == 1:
    print("You selected To-do list")
elif option == 2:
    print("You selected Notes")
elif option == 3:
    print("You selected Exit")
    print("Goodbye!")
    exit()