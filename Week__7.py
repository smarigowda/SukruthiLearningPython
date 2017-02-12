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

string = "1234567890"

for char in string:
	print(char)

for char in iter(string): # this is what the computer does
	print(char)
