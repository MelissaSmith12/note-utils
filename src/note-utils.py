import numpy as np
import fractions
from IPython.display import display, Math

def printAugmentedMatrix(fullmatrix, precision=2, augmented=1):
    latex = r'\left[\begin{array}{'
    
    for _ in range(fullmatrix.size[0] - augmented):
        latex += 'r' 
    latex += '|'
    for _ in range(augmented):
        latex += 'r' 
    latex += '} '

    stringifier = "%." + str(precision) + "f"
    for row in np.asarray(fullmatrix):
        if(precision == 'f'):
            latex += " & ".join([str(fractions.Fraction(number).limit_denominator()) for number in row])
        else:
            latex += " & ".join([stringifier % number for number in row])
        latex += r' \\ '
    latex += r'\end{array} \right]'
    display(Math(latex))   
 
def solveMatrix(LHS, RHS):
    solution = np.linalg.solve(LHS,RHS)
    newLHS = np.zeros(LHS.shape)
    np.fill_diagonal(newLHS, 1)
    return np.column_stack((newLHS, solution))