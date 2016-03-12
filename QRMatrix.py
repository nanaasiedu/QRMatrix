from random import random, randint
#from numpy.linalg import

elemMax = 7 # Maximum matrix element

# Generates random matrix element
def randElem():
    return randint(0,elemMax) #random()*elemMax ================================

# Returns the position opposite to (i,j) in the matrix
def opPos(i, j):
    return j, i

# Generates a random symmetric matrix
def generateSymMatrix(dim):
    matrix = [[0 for x in range(dim)] for x in range(dim)]

    for j in range (0, dim):
        for i in range(0, dim):
            if i >= j:
                matrix[j][i] = randElem()
            else:
                opI, opJ = opPos(i, j)
                matrix[j][i] = matrix[opJ][opI]

    return matrix

def printMatrix(matrix):
    for r in matrix:
        print r
