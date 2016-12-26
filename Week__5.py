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

for i in range(11):
	print("i is now {}".format(i))

i = 0
while i < 10:
	print("i is now {}".format(i))
	i += 1