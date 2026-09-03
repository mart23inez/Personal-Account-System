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
# This block creates the users account if "hasAccount = False" in (1)
# Username and Password must be 8 - 16 characters in length and
# include at least 1 number or special character 0-9.

else:
    username = ""
    password = ""
    passwordverify = ""
    usermin = "1234567890!@#$%^&*()"
    
# 4.5
# Realized that my previous "while loop" did not work with this block since it basically clashed with the 3rd username requirement.
# Previous "while loop": while len(username) < 8 or len(username) > 16:
# Figured out an alternative way that is not elegant nor clean but works. Had some trouble putting it together when I originally coded it.
# Basically, I have a boolean variable set to "False" before running the loop "while index < 20:". I had to make that my
# loop condition (20 being the natural break) because if a user enters a username 8 characters long with the 8th character being ")", "while index < len(username):"
# would not make it to ")", being the 20th index, and cause the program to skip straight to the password block. 
# FINAL UPDATE ON 4.5: Did not like how the second code improvement caused the program to output 2 error messages,
# ("Error: Username must be more than 8 characters, please try again.") and ("Error: Username must include 1 number or special character, please try again.")
# so I added a path that can only be unlocked if the 1st or 2nd requirement are met which then unlocks the 3rd requirement and continues that check producing
# only 1 error message at a time. Lines 78 - 91 do that plus the "verification" function.

    while True:
        username = input("Please enter a username (Must be between 8 - 16 characters and include at least 1 number or special character 0-9): ")
        securedUP = False
        index = 0
        verification = False
        if len(username) < 8:
            print("Error: Username must be at least 8 characters, please try again.")
        elif len(username) > 16:
            print("Error: Username must be 16 characters or fewer, please try again.")
#       elif not any(char in usermin for char in username): <---- Haven't learned the "any" function yet. TBD
        else:
            verification = True
        if verification:
            while index < 20:
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
        
# 5
# This block creates the password and applies the 3 requirements plus a 4th requirement of having the user
# enter the password again to make sure it matches with the first. 
# Same problem applies here, the original "while loop" did not work with the 3rd password requirement.
# Previous "while loop": while len(password) < 8 or len(password) > 16:
# The "FINAL UPDATE" of 4.5 applies in the password block as well.

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
            while index < 20:
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

# 6
# These lines (133 - 138) just print out the welcome message and the options available.

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