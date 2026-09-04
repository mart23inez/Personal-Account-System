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
    numbers = "1234567890"
    letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    specialchar = "!@#$%^&*()"

    while True:
            
            username = input("Please enter a username (3 - 64 characters): ")
            if len(username) < 3:
                print("Error: Username must be at least 3 characters, please try again.")
            elif len(username) > 64:
                print("Error: Username must be no more than 64 characters, please try again.")
            else:
                break

    while True:
        password = input("Please enter a password (Must be at least 12 characters, include 1 letter, and include 1 number and special character (0-9): ")
        securedUP = False
        num_verification = False
        letter_verification = False
        specialchar_verification = False
        verification = False
        num_index = 0
        let_index = 0
        specchar_index = 0
        if len(password) < 12:
            print("Error: Password must be at least 12 characters, please try again.")
        else:
            verification = True

        if verification:
            while num_index < len(numbers):
                verify = numbers[num_index]
                if verify in password:
                    num_verification = True
                    break
                else:
                    num_index += 1
            else:
                print("Error: Password must include 1 number, please try again.")

        if num_verification:
            while let_index < len(letters):
                verify = letters[let_index]
                if verify in password:
                    letter_verification = True
                    break
                else:
                    let_index += 1
            else:
                print("Error: Password must include 1 letter, please try again.")

        if letter_verification:
            while specchar_index < len(specialchar):
                verify = specialchar[specchar_index]
                if verify in password:
                    specialchar_verification = True
                    break
                else:
                    specchar_index += 1
            else:
                print("Error: Password must include 1 special character, please try again.")

            if num_verification and specialchar_verification and letter_verification:
                securedUP = True

        if securedUP:
            break

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