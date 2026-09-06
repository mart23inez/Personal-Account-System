# Personal-Account-System

A console based account system I am building while I learn Python. It handles
account creation, login, and a simple menu. This is a learning project. I write
every line myself and use it to practice what I pick up from the Helsinki Python
MOOC.

## What it does right now

- Asks if you already have an account, using a reusable yes/no function that
  keeps asking until it gets a valid answer
- Login against a hardcoded account, with a 3 attempt lockout
- Account creation:
  - username between 3 and 64 characters
  - password at least 15 characters, with at least one letter, one number, and
    one special character
  - password entered a second time to make sure it matches
- A menu with to-do list, notes, and exit. To-do and notes are placeholders
  until I learn lists.

## Planned

- Working to-do list and notes, once I have learned lists
- Saving accounts to a file so they last between runs
- Hashing passwords with a salt instead of storing them as plain text.
  Hashing, not encryption, since it only needs to go one way.
- Encrypting the saved notes and to-do data, which does need to go both ways
- A blocklist to reject common and weak passwords
- A case insensitive check so two people cannot take the same username

## Known limitations

Nothing is saved yet, so everything resets when the program closes.

The password rules require a mix of character types. Current NIST guidance
(SP 800-63B) actually recommends against that, and says to use a longer minimum
length plus a blocklist of known weak passwords instead. I am keeping the rules
for now because I do not have the blocklist yet, and dropping them without a
replacement would let weaker passwords through. The blocklist is on the list
above.

## Files

- `personal_account_system.py` is the program.
- `PASNotes.py` is the same code with my own notes above each block, explaining
  what it does and what I changed along the way.

## Running it

Needs Python 3. No libraries to install.

    python personal_account_system.py

## On AI use

I use Claude as a tutor while I build this. It explains concepts I have not
covered yet, points me at my own bugs instead of fixing them, and pushes back
when my reasoning is wrong. It does not write my code. Every line of Python in
this repo was written and debugged by me, and I do not keep anything I cannot
explain.