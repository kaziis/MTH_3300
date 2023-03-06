#******************************************************************************
# parking.py
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

# car one will always go first and car two will come next
# if available it will go ahead and park in the preferred spot
# if spot taken, then next available spot it'll park  (ex. preferred spot is 2 -> attempt to park at 3 -> if 3 is taken it will not park)

# Car 1 preferred spot: 3
# Car 2 preferred spot: 3
# Car 1 parks in spot 3
# Car 2 cannot park

# ask the user to input the preferences of each of the two cars: 1, 2, or 3. Use the input prompt format as specified in the sample runs above.
# print out the parking configuration, given that the cars will park according to the rules specified above. (Use the output format as in the sample runs above.)
# NOT use lists or tuples (or other structures we have not yet discussed)!

# input car preferred spots
car1 = int (input ('Car 1 preferred spot: '))
car2 = int (input ('Car 2 preferred spot: '))

# if they are equal
def equal (c1, c2):
    print (f'Car 1 parks in spot {c1}')
    if c1 == 1:
        c2 += 1
        print (f'Car 2 parks in spot {c2}')
    if c1 == 2:
        c2 += 1
        print (f'Car 2 parks in spot {c2}')
    if c1 == 3:
        print (f'Car 2 cannot park')


# when they are not equal
def not_equal (c1, c2):
    print (f'Car 1 parks in spot {c1}')
    print (f'Car 2 parks in spot {c2}')

# make the code run
if car1 == car2:
    equal (car1, car2)
else:
    not_equal (car1, car2)
