##******************************************************************************
# numericalintegration.py
#******************************************************************************
# Name: Kazi Shahria
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
# I watched a Youtube video to know about the Trapezoidal Rule
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):

import math # (do not modify this line)

# DEFINE YOUR FUNCTION f HERE:
def f(x):
    return (3+math.exp(x**2))**(1/10)

# TEST CODE FOR THE FUNCTION f: (uncomment to test, comment out when submitting)
#print(f(0.2), '(this should equal 1.1498649904239635 if your function works)')
#print(f(-1.4), '(this should equal 1.260170311191703 if your function works)')


# CODE FOR GETTING THE INPUT (do not modify)
A = float(input('Enter A: '))
B = float(input('Enter B: '))
N = int(input('Enter N: '))


# INSERT CODE FOR COMPUTING APPROXIMATION OF DEFINITE INTEGRAL BELOW
# (USING TRAPEZOIDAL RULE, left-hand Riemann sum, and right-hand Riemann sum)
# name your variables representing the approximations so the provided print statements work below
################################################
delta_x = (B-A)/N # We need to divide this by 1/2

# So the pattern I see is that for whatever step the delta_x is being multiplied by
inner_sum = 0
for i in range (1,N): # We can forget about the first one and the last one and just focus on the stuff inside
    xi = 2*f(A+(delta_x*i))
    inner_sum += xi
trap = (delta_x/2*(f(A)+inner_sum+f(B)))
lhs = delta_x*(f(A)+(0.5*inner_sum))
rhs = delta_x*(f(B)+(0.5*inner_sum))
################################################
# CODE FOR PRINTING THE APPROXIMATIONS TO 7 DECIMAL PLACES (do not modify)
# trap, lhs, and rhs should be your variable names above for each respective approximation
print(f'{trap:.7f}')
print(f'{lhs:.7f}')
print(f'{rhs:.7f}')