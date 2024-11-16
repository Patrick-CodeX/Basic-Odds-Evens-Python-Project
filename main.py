
i = 0
# So the i = 0 this is going to be used later for the while loop.


# These are just lists being stored the values of numbers for later.
list = []

Odds = []

Even = []

while i < 5:
# This while loop is used, because we're asking the person for 5 numbers, so instead
# Of just repeating the input with different variables we'll just change it with x and then put it in a list.
    x = input("Please input a number. ")
# The x is asking for a number.
    list.append(x)
# It will then append the number into a list called "list".
# Append is just a function to add the value of the variable to the list.
    i += 1
# Then we add 1 to i. The "+= 1" is just saying add 1 to i. So now this for loop is going to continue until
# i has the value 5, because 5 is not bigger than 5.
for x in list:
# This for loop is saying x go through each number in the list, so the x will go through the first number
# Then x will maintain the value of the first number through the rest of the code.
    if int(x) % 2 == 0:
        # The int() just temporarily changes the string into a integer, because you can't do 5 + "5", everying appended in a list
        # Will become a string. So int(x) is just saying turn whatever value into a integer, so "5" is 5.
        Even.append(x)
        # So we're then going to add whatever the outcome of x is happening here. So x is going to % (mod) 2. This just means if I have 5 % 2 the return would be 1.
        # Because 2 can go 2 times into, because to 2 * 2 = 4      5 - 4 = 1, so it's just a remainder.
        # So the if statement is saying if x = 0 which is the ==, then it will append the number to the even list, because 2 can go into any even number, and return a zero.
    else:
        Odds.append(x)
    # So here if x doesn't follow the first if statement, then it will just go to the Odds list, because if it's not even then it must be odd.

print("These are Odd", Odds)

print("\n")
#This just adds a new line to the program, so that way these two lists arent clumped.
# Ex: These are Odd ['1', '3']
#     These are Even ['0', '2', '4']
#
# Instead: These are Odd ['1', '3']
#
#          These are Even ['0', '2', '4']

print("These are Even", Even)
# These are just printing the Odd, and Evens list.

# Also the reason 0 works is that 0 % 2 returns 0, because 2 can't go into anything, so the only remainder is 0.