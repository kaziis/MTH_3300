#******************************************************************************
# population.py
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
# growth_value = f'{growth_value:6f}'
# Enter the initial population: 300
# Enter the first time period in years: 4
# Enter the first growth rate as a percentage: 1.2
# Enter the second time period in years: 2.5
# Enter the second growth rate as a percentage: 5
# The ending population is 356.659832
# The overall growth in the 6.5 year period is 18.887 percent

import math 

# First calculation
e = math.exp(1)
p = float (input ('Enter the initial population: ')) # only taking this number back into second equation
t1 = float (input ('Enter the first time period in years: '))
r = float (input ('Enter the first growth rate as a percentage: '))/100
growth_value = p * e ** (r * t1)

# Second calculation
t2 = float (input ('Enter the second time period in years: '))
r = float (input ('Enter the second growth rate as a percentage: '))/100
growth_value = growth_value * e ** (r * t2)

# Percentage growth
percentage_growth = ((growth_value - p) /p) * 100

# Total years
total_years = t1 + t2

# Print statements
print (f'The ending population is {growth_value:.6f}')
print (f'The overall growth in the {total_years} year period is {percentage_growth:.3f} percent')