
import sys

while True:
	try:
		artist_age = int(input("How old are you?\n"))
		if (artist_age >= 18):
			print('you are allowed to perform')
		else:
			print('you are not allowed to perform')
		break
	except ValueError:
			print('please enter a valid number')