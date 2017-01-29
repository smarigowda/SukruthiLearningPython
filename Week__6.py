# small number game
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))

guess = int(input()) # first attempt

if guess != answer:
	if guess < answer:
		print("Please guess higher")
	else:
		print("Please guess lower")

	guess = int(input()) # second attempt
	if guess == answer:
		print("Well done you guessed it 2nd time")
		exit(0)
	elif guess < answer:
		print("Please guess higher")
	else:
		print("Please guess lower")

	guess = int(input()) # third attempt
	if guess == answer:
		print("Well done you got it!!")
		exit(0)
	elif guess < answer:
		print("Please guess higher")
	else:
		print("Please guess lower")

	guess = int(input()) # fourth attempt
	if guess == answer:
		print("You finally got the answer!")
	else:
		print("Sorry you failed to guess correctly.")
else:
	print("You got it first time, well done!")