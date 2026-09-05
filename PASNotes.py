print("Welcome!")

# 1
# This would be where the program pulls username and password from the file.
# For now, I will hard-code that info into the code.

username = "ADMIN"
password = "PASSWORD"

# 2
# This block will ask and verify if the user has an account.
# The account is hard-coded into the code (1).

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

# 3
# This block asks the user for username and password to continue.
# It also has a 3 attempt limit before exiting the program.

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

# 4
# Replaced "usermin" with "numbers, letters, and specialchar" to upgrade the password requirement system.
# "usermin" did not specifically check for numbers, letters, or special characters. 
# Inputs like "11111111" or "!!!!!!!!" should not have been passing through the system. Working example: "randomuser123!@#" and "randompass123!@#"

else:
    username = ""
    password = ""
    passwordverify = ""
    numbers = "1234567890"
    letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    specialchar = "!@#$%^&*()"

# 4.5
# Removed a lot of the username verifications because usernames do not require the same requirements as passwords do.
# Length minimum and maximum are the only requirements, being 3 characters minimum and 64 characters maximium.

    while True:
        username = input("Please enter a username (3 - 64 characters): ")
        if len(username) < 3:
            print("Error: Username must be at least 3 characters, please try again.")
        elif len(username) > 64:
            print("Error: Username must be no more than 64 characters, please try again.")
        else:
            break
        
# 5
# A complete overhaul of the password-requirement verifier.
# Replaced three near identical blocks with one function called three times.
# It takes 3 inputs (category, password, req) and checks if the password
# has at least one character from that category.
# If it finds one, it returns True right away and stops checking.
# If it never finds one, it prints the error for that category and returns False.
# The loop uses those three returned values to decide whether to break.

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

    while True:
        password = input("Enter a Password (Must include be at least 12 characters long and include 1 letter, number, and special character): ")
        if len(password) < 12:
            print("Error: Password must be at least 12 characters long, please try again.")
        else:
            num_verification = requirement_verifier(numbers, password, "number")
            letter_verification = requirement_verifier(letters, password, "letter")
            specchar_verification = requirement_verifier(specialchar, password, "special character")
            if num_verification and letter_verification and specchar_verification:
                reqmet = True
        if reqmet:
            passwordverify = input("Enter your password again: ")
            if passwordverify == password:
                print("Account successfully created!")
                break
            else:
                print("Error: Passwords must match, please try again.")
        
# 6
# These lines just print out the welcome message and the options available.

print(f"Welcome {username}!")

print("What would you like to do?")
print("(1) To-do list")
print("(2) Notes")
print("(3) Exit")

# 7
# This block loops the users input and checks if its valid input (1 - 3) and continues on. The program tells
# the user that their input is invalid if they enter anything else besides (1 - 3)

while True:
    try:
        option = int(input("What would you like to do? (1 2 3): "))
        if option == 1 or option == 2 or option == 3:
            break
        else:
            print(f"Error: Not a valid input, please try again.")
    except ValueError:
        print(f"Error: Not a valid input, please try again.")

# 8
# This block just prints out what the user selected. I haven't the necessary information related
# to file management so options 1 and 2 are just place holders. Option 3 is the only functioning 
# option as of 8/30/26. 

if option == 1:
    print("You selected To-do list")
elif option == 2:
    print("You selected Notes")
elif option == 3:
    print("You selected Exit")
    print("Goodbye!")
    exit()