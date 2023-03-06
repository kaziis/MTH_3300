#******************************************************************************
# binary.py
#******************************************************************************
# Name: Kazi Shahria
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used): NONE
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# binary = ((digit8 + 8) + (digit4 + 4) + (digit2 + 2) + (digit1 + 1))

import random
# The two lines below set the random seed for testing on Gradescope. Comment out these lines to test your code on Spyder.
#####################
seed = input() # comment out to test on Spyder, but leave for Gradescope submission
random.seed(seed) # comment out to test on Spyder, but leave for Gradescope submission
#####################

# inputting the numbers and generating random number
digit8 = int (input ("Enter 8's digit: "))
digit4 = int (input ("Enter 4's digit: "))
digit2 = int (input ("Enter 2's digit: "))
digit1 = int (input ("Enter 1's digit: "))
x = random.randrange (0,16)

# combining the binary numbers
combined = str (digit8) + str (digit4) + str (digit2) + str (digit1)

#checking the numbers are a 1
if digit8 == 1:
    digit8 = 8
else:
    digit8 = 0

if digit4 == 1:
    digit4 = 4
else:
    digit4 = 0

if digit2 == 1:
    digit2 = 2
else:
    digit2 = 0

if digit1 == 1:
    digit1 = 1
else:
    digit1 = 0

# adding the numbers
num = (digit8 + digit4 + digit2 + digit1)

print (f'The binary number {combined} is {num} in base ten')
print (f'Less than the randomly generated number {x}? {num < x}')
