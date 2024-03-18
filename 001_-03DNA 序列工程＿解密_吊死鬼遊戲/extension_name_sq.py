"""
File: name_sq.py (extension)
Name: Meg
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    make the name print like a square
    """
    print('This program prints a name in a square pattern!')
    name = str(input('Name: '))
    print(name)
    side_name(name)
    bottom_name(name)


def side_name(name):
    """
    :param: user input string
    """
    for i in range(len(name)-2):
        print(name[i+1], end="")  # left side string
        for j in range(len(name)-2):  # middle space
            print(" ", end="")
        print(name[len(name)-(i+2)])  # right side string, and will change the line


def bottom_name(name):
    """
    :param: user input string
    """
    reverse_name = ""
    for i in range(len(name)):  # reverse the string
        reverse_name = name[i] + reverse_name
    print(reverse_name)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
