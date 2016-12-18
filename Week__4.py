# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''

# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
# #
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))

# for state in [" not pinin'", " no more", " a stiff", " bereft of life"]:
#     print("This parrot is"+ state)

# for i in range(0, 100, 5):
#     print("i is {} ".format(i))

# for i in range(1,13):
#     for j in range(1,13):
#         print("{1} times {0} is {2}". format(i, j, i*j))
#         print("=============")

# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         break

#     print("Buy " + item)

# meal = ["egg", "bacon", "tomato", "rice"]

# for item in meal:
#     if item == 'bacon':
#         nasty_food_item = item
#         break
# #
# if nasty_food_item:
# # #instead of underscore can put nastyFoodItem
#     print("Can i have anything without bacon in it?")


number = "9,223,272,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))










