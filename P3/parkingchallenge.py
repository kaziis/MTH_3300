#******************************************************************************
# parkingchallenge.py Programming Problem 3b -- BONUS!
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
# 
#

car1 = int (input ('Car 1 preferred spot: '))
car2 = int (input ('Car 2 preferred spot: '))
car3 = int (input ('Car 3 preferred spot: '))

# if they are equal
def equal (c1, c2, c3):
    # print (f'Car 1 parks in spot {c1}')
    if c1 == 1: # EXECUTES WHEN PARKING SPOT 1 IS TAKEN
        if c2 == 3 and c3 == 1:
            c3 = 2
            print (f'Car 1 parks in spot {c1}')
            print (f'Car 2 parks in spot {c2}')
            print (f'Car 3 parks in spot {c3}')
        elif c2 == 3 and c3 == 3:
            print ('not possible for all vehicles to park')
            # print (f'Car 2 parks in spot {c2}')
            # print (f'Car 3 cannot park')
        else:
            c2 = 2 
            c3 = 3
            print (f'Car 1 parks in spot {c1}')
            print (f'Car 2 parks in spot {c2}')
            print (f'Car 3 parks in spot {c3}')
    if c1 == 2: # EXECUTES WHEN PARKING SPOT 2 IS TAKEN
        if c2 >= 2 and c3 >= 2:
            print ('not possible for all vehicles to park')
            # c2 = 3
            # print (f'Car 2 parks in spot {c2}')
            # print (f'Car 3 cannot park')
        elif c2 == 1:
            c2 = 1
            c3 = 3
            print (f'Car 1 parks in spot {c1}')
            print (f'Car 2 parks in spot {c2}')
            print (f'Car 3 parks in spot {c3}')
        else:
            c2 = 3
            c3 = 1 
            print (f'Car 1 parks in spot {c1}')
            print (f'Car 2 parks in spot {c2}')
            print (f'Car 3 parks in spot {c3}')
    if c1 == 3: # EXECUTES WHEN PARKING SPOT 3 IS TAKEN
        if c3 > c2:
            print ('not possible for all vehicles to park')
            # print (f'Car 2 parks in spot {c2}')
            # print (f'Car 3 cannot park')
        elif c2 > c3:
            print ('not possible for all vehicles to park')
            # print (f'Car 2 cannot park')
            # print (f'Car 3 parks in spot {c3}')
        elif c2 == 3 and c3 == 3:
            print ('not possible for all vehicles to park')
            # print (f'Car 2 cannot park')
            # print (f'Car 3 cannot park')
        elif c2 == 1 and c3 == 1:
            c3 = 2
            print (f'Car 1 parks in spot {c1}')
            print (f'Car 2 parks in spot {c2}')
            print (f'Car 3 parks in spot {c3}')
        elif c2 == 2 and c3 == 2:
            print ('not possible for all vehicles to park')
            # print (f'Car 2 parks in spot {c2}')
            # print (f'Car 3 cannot park')

# when they are not equal
def not_equal (c1, c2, c3):
    print (f'Car 1 parks in spot {c1}')
    print (f'Car 2 parks in spot {c2}')
    print (f'Car 3 parks in spot {c3}')

# make the code run
if car1 == car2 or car1 == car3 or car2 == car3:
    equal (car1, car2, car3)
else:
    not_equal (car1, car2, car3)

# probably a simpler way to code this... sorry about the mess lol