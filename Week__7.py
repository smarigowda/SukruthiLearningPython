# list_1 = []
# list_2 = list()
# list_3 = ["non empty list"]

# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
# if list_1 == list_2:
# 	print("The lists are equal") # empty lists are equal

# if list_1 == list_3:
# 	print("list 1 and 3 are equal")
# else:
# 	print("list 1 and 3 are not equal")

# print(list("The lists are equal"))

# menu = []
# menu.append(["egg","spam","carrots"])
# menu.append(["egg", "potatoes","carrots"])
# menu.append(["egg","spam",])
# menu.append(["egg","carrots", "spam"])
# menu.append(["egg","carrots","potatoes","spam"])
# menu.append(["spam","carrots","potatoes","spam"])
# menu.append(["spam","egg","spam","spam","carrots","spam"])
# menu.append(["spam","egg","potatoes","spam"])

# print(menu)

# #
# #
# for meal in menu:
# 	if not "spam" in meal:
# 		print(meal)
# 		for ingredient in meal:
# 			print(ingredient)

# string = "1234567890"

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# string = "1234567890"

# for char in string:
# 	print(char)

# for char in iter(string): # this is what the computer does
# 	print(char)


# for i in range(0, 1):
# 	print i

# my_list = ["1,2,3,4,5,6,7"] # this is a single element
# my_iterator = iter(my_list)

# for i in range(0, len(my_list)):
# 	next_item = next(my_iterator)
# 	print(next_item)

# my_list = list(range(10))
# print(my_list)
# #
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
# #
# print(even)
# print(odd)

# ##################################

# my_string ="abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('e'))
# print(my_string[4])

# ###################################

# small_decimals = range(0, 10)
# print(small_decimals)

# print(small_decimals.index(3))

# ##################################

# odd = range(1, 10000, 2)
# print(odd)

# print(odd[985]) # It gives the 985th odd number

sevens = range(7, 1000000, 7)
x = int(input("Please enter a positive number less than 1 million,if divisible by 7 an answer is given: "))
if x in sevens:
	print("{} is divisible by seven". format(x))


