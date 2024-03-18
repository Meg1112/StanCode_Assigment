"""
File: rocket.py
Name:Meg
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    Make a rocket and user can input size to create different size rocket
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):  # make left side space
            print(' ', end='')
        for j in range(i+1):  # make left side slash"/"
            print('/', end='')
        for j in range(i + 1):  # make right side slash"\"
            print('\\', end='')
        print(' ')


def belt():
    print('+', end='')
    for i in range(SIZE*2):
        print('=', end='')
    print('+')


def upper():
    for i in range(SIZE):
        print("|", end='')
        for j in range(SIZE-i-1):  # make upper left side "."
            print('.', end='')
        for j in range(i+1):
            print('/\\', end='')
        for j in range(SIZE-i-1):  # make upper right side "."
            print('.', end='')
        print("|")


def lower():
    for i in range(SIZE):
        print("|", end='')
        for j in range(i):  # make lower left side "."
            print('.', end='')
        for j in range(SIZE-i):
            print('\\/', end='')
        for j in range(i):  # make lower right side "."
            print('.', end='')
        print("|")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
