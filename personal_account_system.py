print("Welcome!")

username = "ADMIN"
password = "PASSWORD"

def get_menu_option(prompt,*args):
    while True:
        try:
            print(prompt)
            for i, v in enumerate(args, 1):
                print(i, v)
            user_input = int(input())
            if 1 <= user_input <= len(args):
                return user_input
            else:
                print("Error: Number is not a valid option, please try again.")
        except ValueError:
            print("Error: Not a valid input, please try again.")

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

menu_one_option = get_menu_option("What would you like to do?: ", "Log in", "Sign up", "Exit")

if menu_one_option == 1:
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

elif menu_one_option == 2:
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

elif menu_one_option == 3:
    print("Goodbye! ")
    exit()

while True:
    menu_two_option = get_menu_option("What would you like to do?", "To-do List", "Notes", "Exit")

    if menu_two_option == 1:
        print("You selected 'To-Do List")
        
        while True:
            user_input = get_menu_option("What would you like to do?", "View", "Add", "Remove", "Return")

            if user_input == 1:
                if menu_one_option == 1:
                    with open("text.txt") as f:
                        print(f.read())
                if menu_one_option == 2:
                    with open("text.txt", "x") as f:
                        f.write("Hmmm... Nothing to see here, maybe you should 'Add' something here...")
                    with open("text.txt") as f:
                        print(f.read())
                        print("This should be working")
                    menu_one_option = 1
                    
                
            elif user_input == 2:
                print("Option 2")

            elif user_input == 3:
                print("Option 3")

            elif user_input == 4:
                print("Returned to Main Menu")
                break
    elif menu_two_option == 2:
        print("NOTES PART")
    elif menu_two_option == 3:
        print("Goodbye!")
        exit()