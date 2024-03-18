"""
File: prime_checker.py
Name:Meg
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	Check if number is a prime number,and user can enter any number which greater than 1.
	The program ends when the user enter the EXIT number.
	"""
	print('Welcome to the prime checker !')
	n = int(input("n:"))
	if n == EXIT:
		print('Have a good one!')
	else:
		while True:
			m = 2
			if n == EXIT:
				break
			if n == m:  # if n = 2
				print(str(n) + ' is a prime number')
				n = int(input("n:"))
			else:
				while n >= m:  # If n>m, n % m != 0 then m+1
					if n % m != 0:
						m += 1
					elif n % m == 0:
						if n > m:  # check if n % m ==0, still n>m,n is "not" a prime
							print(str(n) + ' is not a prime number')
							m = 2  # make "m" return to "2"
							n = int(input("n:"))
						elif n == m:  # if n % m ==0, but n==m, n is a prime
							print(str(n) + ' is a prime number')
							m = 2  # make "m" return to "2"
							n = int(input("n:"))
		print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
