"""
File: hailstone.py
Name:Meg
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Compute Hailstone Sequence.odd number *3+1 ,even number /2 ,tile number == 1
    Count how many time to reach 1
    """
    print('This program computes   ')
    n = int(input('Enter a number:'))
    count = 0
    while n != 1:
        if n % 2 == 0:
            print(str(n) + ' is even ,so I take half: ' + str(int(n / 2)))
            n = int(n/2)
            count += 1  # record count number
        elif n % 2 == 1:
            print(str(n) + ' is odd ,so I make 3n+1: ' + str(3*n+1))
            n = int(3*n+1)
            count += 1  # record count number
    print('It took ' + str(count) + ' step to reach 1')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
