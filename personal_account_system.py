print("Welcome!")

username = "ADMIN"
password = "PASSWORD"

def confirm(prompt, error = "Error: Invalid input, please try again"):
    while True:
        answer = input(prompt).strip().upper()
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print(error)

def requirement_verifier(category, password, req):
    count = 0
    while count < len(category):
        verify = category[count]
        if verify in password:
            return True
        else:
            count += 1
    print(f"Error: Password must include 1 {req}, please try again.")
    return False

has_account = confirm("Do you have an account with us?: (Y/N)")

if has_account:
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
        password = input("Enter a Password (Must be at least 15 characters long and include 1 letter, number, and special character): ")
        if len(password) < 15:
            print("Error: Password must be at least 15 characters long, please try again.")
        else:
            num_verification = requirement_verifier(numbers, password, "number")
            letter_verification = requirement_verifier(letters, password, "letter")
            specchar_verification = requirement_verifier(specialchar, password, "special character")
            if num_verification and letter_verification and specchar_verification:
                passwordverify = input("Enter your password again: ")
                if passwordverify == password:
                    print("Account successfully created!")
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