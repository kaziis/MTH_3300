#******************************************************************************
# montecarlosimulation.py
#******************************************************************************
# Name: Kazi Shahria
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
# NONE
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# So the sum of has to be grater than x -> if not, you pay -$100
# You get $1 (if you roll a 1 or a 2), $5 (if you roll a 3), $10 (if you roll a 4), $20 (if you roll a 5), or $100 (if you roll a 6)

import random
num_of_plays = 10 ** 6
success = 0 # variable for number of successes (success for a trial means getting at least *dollars* - variable below)
earnings = 0 # variable for total amount of sum
num_rolls = int (input()) # first input: number of dice rolls
dollars = int (input()) # second input: the dollar amount needed to keep the money

# The above six lines should be before any of your code
# Use the variable names provided above in your simulation

# START CODE FOR SIMULATION BELOW THE NEXT LINE

# first we need to configure each play, so for example, play 1... play 2... play 3...
for p in range (num_of_plays):
    # print (f'Play {p+1}')
    sum = 0
# we create a dice which rolls based on the "num_rolls" input
    for i in range (num_rolls):
        dice = random.randrange(1, 7)
        # print (f'You rolled the numbers {dice}')
# we take that roll and check what amount the person made  which goes as followed
        if dice == 1 or dice == 2:
            sum += 1
        elif dice == 3:
            sum += 5
        elif dice == 4:
            sum += 10
        elif dice == 5:
            sum += 20
        else:
            sum += 100
    # print (f'So far you have made {sum}')
# you get $1 (if you roll a 1 or a 2), $5 (if you roll a 3), $10 (if you roll a 4), $20 (if you roll a 5), or $100 (if you roll a 6)
# then if the sum of all the rolls is greater than or equal to the dollars amount, they get to keep the money and the success is +1
    if sum >= dollars:
        earnings += sum
        success += 1
# else you have to pay -$100 and your sum is subtracted by it
    else:
        earnings -= 100
    # print (f'Earned/Lost {earnings}')
    # print (f'Success: {success}')
    # print ()

################################################

# these last two print lines should be at the very end of your code
print(f'{success/num_of_plays:.1f}')

# # # rounding output to the nearest tens place (bad estimate) but to allow for variability due to probability
print(int(round(earnings/num_of_plays,-1))) 
