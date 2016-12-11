name = input("Please enter your name")
age = int(input("How old are you?"))
if 18 <= age < 31:
    print("Welcome to the holiday")
else:
    print("You are illegible for the holiday")

for i in range(1,20):
    print("i is now {}".format(i))

number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')

number = "9,223,372,036,854,775"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))