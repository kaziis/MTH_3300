#******************************************************************************
# newton.py
#******************************************************************************
# Name: Kazi Shahria
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
# Youtube videos on Newton's Method
# 
#
# Reminder: you are to write your own code.
#
# This assignment is optional and can be used to replace your lowest programming 
# problem score.
#
# Important note: If any of your submissions for this problem are flagged by the 
# plagiarism software or found to use any unauthorized resources, you will not 
# receive any credit for the submission. Additionally, the final exam bonus will 
# NOT be applied to compute your overall grade. (That is, your final exam score 
# will NOT be used to replace half of your lowest midterm score, provided your 
# final exam score is higher.) This assignment is the intellectual property of 
# Baruch College's MTH 3300 course. It is illegal to share it, in part or whole, 
# with anyone outside our current course, including posting on the internet.
# As stated in our course policy, you may be ineligible for any favorable changes 
# to the grading criteria if you are involved in academic dishonesty.
#******************************************************************************
# Overall notes (not to replace inline comments):
# This was a interesting problem, and also challenging! 


def poly_deriv(polylist):
    derivlist = []
    for i in range (1, len (polylist)):
        if i == 1:
            derivlist.append(polylist [i])
        else:
            derivlist.append (polylist [i]*(i))
    return derivlist

def poly_eval(polylist, x):
    value = 0
    for i in range (len (poly_deriv(polylist))+1):
        if i == 0: 
            value += (polylist)[i]
        else:
            value += (polylist)[i]*(x**i)
    return value

def org (polylist, x):
    org = 0
    for i in range (len (polylist)):
        if i == 0:
            org += polylist[i]
        else:
            org += polylist[i]*(x**i)
    return org

def main():
    clist = []
    for i in range(8):
        c = float(input(f'x^{i} coefficient: '))
        clist.append(c)
    g = float(input('guess: '))
    
    iter = int(input('number of iterations: '))

    for n in range (iter):
        x_n = (g-(org (clist, g)/(poly_eval(poly_deriv(clist), g))))
        g=x_n
    print (f'an approximate solution is {x_n:.11f}') 
main()
