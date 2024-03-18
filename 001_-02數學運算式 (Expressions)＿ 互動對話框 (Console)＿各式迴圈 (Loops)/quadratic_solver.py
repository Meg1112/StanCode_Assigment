"""
File: quadratic_solver.py
Name:Meg
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Call Quadratic Solver function
	"""
	for i in range(3):
		print('stanCode Quadratic Solver!')
		a = float(input('Enter a: '))
		b = float(input('Enter b: '))
		c = float(input('Enter C: '))
		discriminant = b * b - 4 * a * c
		if discriminant < 0:  # check if discriminant<0
			print('No real roots')
		elif discriminant > 0:  # check if discriminant>0
			y = math.sqrt(discriminant)
			x1 = (-b + y) / 2 * a
			x2 = (-b - y) / 2 * a
			print('Two roots : ' + str(x1)+',' + str(x2))
		else:  # discriminant==0
			y = math.sqrt(discriminant)
			x1 = (-b + y) / 2 * a
			print('One roots : ' + str(x1))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
