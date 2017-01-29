# import sys

# print("Please enter an ipAddress in the format xxx.yyyy.zzzz.nnnn: ")

# ipAddress = sys.stdin.readline()

# print(ipAddress.count("."))

# colour_list = ["red", "green", "blue", "yellow", "purple"]

# colour_list.append("black")

# for state in colour_list:
# 	print("The colour is " + state)

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]

# numbers = even + odd
# numbers_in_order = sorted(numbers)

# print(numbers_in_order)

# if numbers == numbers_in_order:
# 	print("The lists are equal")
# else:
# 	print("The lists are not equal")

# if numbers_in_order == sorted(numbers):
# 	print("The lists are equal")
# else:
# 	print("The lists are not equal")

# list_1 = []
# list_2 = list()
# #both lists are empty and come out as the same

# print("list 1: {}".format(list_1))
# print("list 2: {}".format(list_2))

# if list_1 == list_2:
# 	print("Das list ist equal.")
# else:
# 	print("Das list ist nicht equal.")

# print(list("Das list ist equal"))

even = [2, 4, 6, 8]
another_even = sorted(even, reverse=True)

print(another_even == even)

another_even.sort(reverse=True)
print(even)