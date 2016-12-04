#age = 12

#print("My age is " + str(age) + " years")

#print("My age is {0} years".format(age))

#print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "January", "March", "May", "July", "August", "October", "December"))

# print("""January: {2}
# February: {0}
# March: {1}
# April: {2}
# May: {1}
# June: {2}
# July: {1}
# August: {2}
# September: {1}
# October: {2}
# November: {1}
# December: {2}""".format(28, 30, 31))
#
# print("My age is %d years" % age)
# print("My age is %d %s, %d %s" % (age, "years", 2, "months"))

#for i in range(1, 12):
 #   print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2,  i ** 3))


# print("Pi is approximately %12.50f" % (22.0 / 7.0))


#for i in range(1, 12):
    #print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2,  i ** 3))

# print("Pi is approximately {0:12.50f}".format(22 / 7))

# for i in range(1, 12):
#      print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))


# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
#     # print("Please put an X in the box")
#
# else:
#     print("please come back in {0} years".format(18 - age))


# print("Please guess a number between 1 and 100: ")
# guess = int(input())
#
# if guess < 76:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 76:
#         print("Well done you guessed it")
#     else:
#         print("Sorry you have not guessed correctly")
# elif guess > 76:
#     print("Please guess lower")
#     guess = int(input())
#
#     if guess == 76:
#         print("Well done you guessed it")
#     else:
#         print("Sorry you have not guessed correctly")
# else:
#     print("You got it first time")
#
# age = int(input("How old are you? "))
#
# if (age < 16) or (age > 65):
#        print("Enjoy your free time")
# else:
#     print("Have a good day a work")
#


# x ="false"
# if x:
#     print("x is true")
#


# x = input("Please enter some text ")
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything")

print(not False)
print(not True)
#
age = int(input("How old are you?"))
if not(age < 18):
    print("You are an Adult")
    print("You are old enough to vote")
else:
    print("Please come back in {0} years when you are an adult".format(18 - age))