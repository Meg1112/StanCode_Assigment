"""
File: hangman.py
Name:Meg
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    User can guess the word, but only have 7 times to guess.
    Every time only can input one alphabet.
    If guess wrong then loss one time , guess correct can keep going(no loss)
    7 times guess wrong the game over. Before 7 times guess the correct word, User Win.
    """
    guess_word = random_word()
    length = length_word(guess_word)
    print('The world looks like :' + str(length))
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')
    number = N_TURNS  # Show the remaining number.
    while True:
        guess = str((input('Your Guess: ')).upper())
        if not guess.isalpha():  # Check guess is single string or not.
            print('Illegal format.')
        elif len(guess) > 2:
            print('Illegal format.')
        else:
            result = guess_result(guess, guess_word, length)
            length = result
            if guess in guess_word:
                if length == guess_word:  # If user guess is correct, end game.
                    return print('You are correct !\nYou win!!\nThe answer is: ' + guess_word)
                else:  # If user guess one alphabet right, continue game.
                    print('You are correct !\nThe world looks like :' + result)
                    print('You have ' + str(number) + ' wrong guesses left.')
            else:
                number -= 1
                if number == 0:  # If guess number == 0 games over.
                    break
                else:  # If user guess one alphabet wrong, continue game.
                    print("There is no " + guess + "\' in the word.\nThe world looks like :" + result)
                    print('You have ' + str(number) + ' wrong guesses left.')
    print("There is no " + guess + "\' in the word.\nYou are completely hung :(")
    print("The answer is: " + guess_word)


def length_word(guess_word):
    """
    :param guess_word: str, the answer
    return: str, length of guess_word
    """
    length = ""
    for i in range(len(guess_word)):
        length += "-"
    return length


def guess_result(guess, guess_word, length):
    """
    :param guess: str, the user input string
    :param guess_word: str, the answer
    :param length: str, the string show user's guess
     return: str, new string of user's guess
    """
    ans = length
    new_ans = ''
    if guess in guess_word:
        for i in range(len(guess_word)):
            alphabet = ans[i]
            if guess != guess_word[i]:  # Check each guess_word alphabet is user's guess or not.
                new_ans += alphabet
            else:
                new_ans += guess
        return new_ans
    elif new_ans == "":  # If first guess is wrong print length.
        return ans
    else:
        return new_ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
