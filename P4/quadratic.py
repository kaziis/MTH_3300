#******************************************************************************
# quadratic.py
#******************************************************************************
# Name: Kazi Shahria
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used): NONE
# 
# A lot of trial and error but works! 
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# math is imported and the code to get the three coefficients is provided to start off

import math

a = float(input('Enter x^2 coefficient: '))
b = float(input('Enter x^1 coefficient: '))
c = float(input('Enter x^0 coefficient: '))

# verifying the square root value to do the calculation (bool in this situation)
verify = ((b**2) - (4 * a * c))

# if the verify is a negative number that means it will fall under the complex solution!
def complex (a, b, c):
    sr = ((b**2) - (4 * a * c)) 
    sr = (sr) ** (1/2)
    sr_1 = ((-b - sr) / (2 * a)) # subtract
    sr_1 = (str (sr_1).split ()) # convert to str to start slicing parts we need
    solution_1 = sr_1 [0][2:-2]
    neg = sr_1 [0][1:2] # is it a negative integer?
    # print (neg) # <-  commented out because I only used them to check if they are working
    if '+' in solution_1:
        solution_1 = solution_1.split('+')
    else:
        solution_1 = solution_1.split('-')
    if neg == '-': # this is if the value is negative (checker)
        value_1 = round (float (solution_1 [0]), 4)
        value_2 = round (float (solution_1 [1]), 4)
        print (f'COMPLEX SOLUTIONS: x = -{value_1:.4f} - {value_2:.4f}i and x = -{value_1:.4f} + {value_2:.4f}i')
    else: # this is otherwise (positive checker)
        value_1 = round (float (solution_1 [0]), 4)
        value_2 = round (float (solution_1 [1]), 4)
        print (f'COMPLEX SOLUTIONS: x = {value_1:.4f} - {value_2:.4f}i and x = {value_1:.4f} + {value_2:.4f}i')
    return

# do the the quadratic equation if it's not complex
def not_complex (a, b, c):
    sr = ((b**2) - (4 * a * c)) 
    formula_add = ((-b + math.sqrt (sr)) / (2 * a))
    formula_sub = ((-b - math.sqrt (sr)) / (2 * a))
    formula_add = round (float (formula_add), 4)
    formula_sub = round (float (formula_sub), 4)
    if formula_add == formula_sub:
        print (f'ONE SOLUTION: x = {formula_add:.4f}')
    elif formula_add < formula_sub:
        print (f'TWO REAL SOLUTIONS: x = {formula_add:.4f} and x = {formula_sub:.4f}')
    elif formula_add > formula_sub:
        print (f'TWO REAL SOLUTIONS: x = {formula_sub:.4f} and x = {formula_add:.4f}')
    return

if a == 0:
    print ('The equation is not quadratic')
elif verify < 0:
    complex (a ,b, c)
else:
    not_complex (a, b, c)