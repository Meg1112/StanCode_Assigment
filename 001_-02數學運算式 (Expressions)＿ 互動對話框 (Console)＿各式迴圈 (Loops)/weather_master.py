"""
File: weather_master.py
Name:Meg
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
QUIT = -1


def main():
	"""
	According input temperature ,compute the average, highest, lowest, cold days among the inputs.
	"""
	count = 0
	cold_day = 0
	print('stanCode \"Weather Master 4.0\"')
	temp = int(input('Next Temperature: (or ' + str(QUIT) + ' to quit)?'))
	count += 1
	if temp < 16:
		cold_day += 1
	if temp == QUIT:
		print('No temperatures were entered.')
	else:
		highest = temp
		lowest = temp
		total = temp
		while True:
			temp = int(input('Next Temperature: (or ' + str(QUIT) + ' to quit)?'))
			if temp == QUIT:
				break
			if temp > highest:  # compute the highest temperature
				highest = temp
			if temp < lowest:  # compute the lowest temperature
				lowest = temp
			if temp < 16:  # compute how many cold day
				cold_day += 1
			total += temp  # compute total temperature
			count += 1  # record how many temperature
		print('Highest temperature = ' + str(highest))
		print('Lowest temperature = ' + str(lowest))
		print('Average: ' + str(total / count))
		print(str(cold_day) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
