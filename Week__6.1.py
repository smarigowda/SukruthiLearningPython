# import sys

# print("Please enter an ipAddress in the format xxx.yyyy.zzzz.nnnn: ")

# ipAddress = sys.stdin.readline()

# print(ipAddress.count("."))

# colour_list = ["red", "green", "blue", "yellow", "purple"]

# colour_list.append("black")

# for state in colour_list:
# 	print("The colour is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers_in_order = sorted(numbers)

print(numbers_in_order)

if numbers == numbers_in_order:
	print("The lists are equal")
else:
	print("The lists are not equal")

if numbers_in_order == sorted(numbers):
	print("The lists are equal")
else:
	print("The lists are not equal")