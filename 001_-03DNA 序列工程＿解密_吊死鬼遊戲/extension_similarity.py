"""
File: similarity.py (extension)
Name:Meg
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Compare the DNA sequence which part is the best match.
    """
    long_sequence = str((input('Please give me a DNA sequence to search: ')).upper())
    short_sequence = str((input('What DNA sequence would you like to match?')).upper())
    ans = search(long_sequence, short_sequence)
    print('The best  match is ' + ans)


def search(long_sequence, short_sequence):
    """
    :param long_sequence:strings,user input long sequence
    :param short_sequence:strings,user input sequence to compare to long sequence
    return: part of long_sequence which is the most similar to short_sequence
    """
    high_rate = 0
    location = ''
    for i in range(len(long_sequence)-len(short_sequence)+1):
        part_long_sequence = long_sequence[i:i + len(short_sequence)]  # part of long_sequence
        number = 0  # correct number
        for j in range(len(short_sequence)):
            ch = part_long_sequence[j]
            ch_s = short_sequence[j]
            if ch == ch_s:
                number += 1
        rate = number / len(short_sequence)  # correct rate
        if rate > high_rate:  # take the highest correct rate
            high_rate = rate  # rate =number/len(short_sequence)
            location = part_long_sequence   # the highest part of long_sequence
    return location


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
