"""
File: caesar.py
Name:Meg
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    User can input Secret number and ciphered string.It's will output deciphered string.
    """
    n = int(input('Secret number: '))
    new = new_alpha(n)
    strings = str((input("What's the ciphered string? ")).upper())
    ans = world(strings, new)
    print("The deciphered string is :" + ans)


def new_alpha(n):
    """
    According Secret number create new alphabet.
    """
    new = ''
    new += ALPHABET[26-n:]
    new += ALPHABET[:26-n]
    return new


def world(strings, new):
    """
    According new alphabet and input strings,deciphered correct string.
    """
    ans = ""
    for i in range(len(strings)):
        t = new.find(strings[i])  # Find input string location in new alphabet
        if t != -1:
            ans += ALPHABET[t]  # Find location in old alphabet
        else:
            ans += strings[i]  # If input string is not in alphabet then output the original string.
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
