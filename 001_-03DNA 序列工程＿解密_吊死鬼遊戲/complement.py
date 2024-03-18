"""
File: complement.py
Name:Meg
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    Output  the complement DNA sequence
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna :str .replace A to T ;C to G
    return:new DNA sequence
    """
    if dna == '':
        return'DNA strand is missing.'
    else:
        ans = ""
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A':
                ans = ans + "T"
            if ch == 'T':
                ans = ans + "A"
            if ch == 'C':
                ans = ans + "G"
            if ch == 'G':
                ans = ans + "C"
        return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
