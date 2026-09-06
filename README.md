# Personal-Account-System

A console based program that handles account creation, login, and a simple menu. This is a learning project for myself as I continue to learn Python. I write every line myself and use it to practice what I pick up from the University of Helsinki Python MOOC.

## What it does

- Asks the user if they have an account. This block uses a reusable True (Yes) or False (No) function that keeps the question until it gets a valid answer. Anything other than those two options is considered invalid.
- The login is using a hardcoded account, no file handling yet (coming soon).
- It also has a 3 attempt lockout but it doesn't really work since the user can rerun the program and continue trying. This is more of a server side function than a client side one.
- Account creation process: Asks the user to input a username between 3 and 64 characters in length (can include numbers and/or special characters but are not required). Asks the user to input a password at least 15 characters in length, no limit, with at least 1 letter, number, and special character required. Asks the user to enter their password again to make sure it was inputted correctly / matches.
- A menu with 3 options: To-do list, notes, and exit. To-do list and notes are pretty much placeholders right now as I learn file handling.
- Exit works as intended.

## Planned

- A working to-do list and notes once I learn file handling and lists.
- Saving accounts so they can last between runs.
- Adding password hashing and salt implementation as opposed to saving passwords as plain text.
  - Hashing not encrypting since its a one way street.
- Encryption and decryption of to-do list and notes, goes both ways.
- Add a password blocklist to prevent weak/common passwords.
- A case insensitive check so that two users cannot have the same username.

## Known limitations

Nothing is saved. Everything resets after the program is closed. Fix coming soon.

## Files

- `personal_account_system.py` is the program.
- `PASNotes.py` is the same code plus my notes above each block, explains what the block does, and any improvements made / fixes done.

## Running it

Needs Python 3. No libraries to install.

```
python personal_account_system.py
```

## On AI use

I use Claude as a tutor while I build this. It explains concepts I have not covered yet, points me at my own bugs instead of fixing them, and pushes back when my reasoning is wrong. It does not write my code. Every line of Python in this repo was written and debugged by me, and I do not keep anything I cannot explain.