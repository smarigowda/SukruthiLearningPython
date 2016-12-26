# greeting = " Good "
# greeting += "morning"
# print (greeting)
# #
# greeting *= 5
# print(greeting)

# input_prompt = "Please enter your IP address. An Ip address consists os 4 numbers " \
# 				"separated from each other by a full stop. "
# ipAddress = input(input_prompt)
# if ipAddress[-1] != '.':
#  ipAddress += '.'

# segment = 1
# segment_length = 0
# character = ""

# for character in ipAddress:
# 	if character == '.':
# 		print("segment {} contains {} characters".format(segment, segment_length))
# 		segment += 1
# 		segment_length = 0
# 	else:
# 		segment_length += 1

# for i in range(11):
# 	print("i is now {}".format(i))

# i = 0
# while i < 10:
# 	print("i is now {}".format(i))
# 	i += 1

# available_exits = ["east", "north east", "south"]

# chosen_exit = ""
# while chosen_exit not in available_exits:
# 	chosen_exit = input("Please choose a direction")
# 	if chosen_exit == "quit":
# 		print("Game over")
# 		break

# print("aren't you glad you got out of there")


import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())
if guess != answer:
	if guess < answer:
		print("Please guess higher")
	else: # guess must be higher than number
		print("Please guess lower")
	guess = int(input())
	if guess == answer:
		print("Well done you guessed it")
	else:
		print("Sorry you have not guessed correctly")
else:
	print("You got it first time, well done!")

