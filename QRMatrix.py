from random import random, randint
import numpy as np
from math import fabs

elemMax = 10 # Maximum matrix element
epsilon = 0.0000000001 # difference limit 10^-10

# Generates random matrix element
def randElem():
    return random()*elemMax

# Returns the position opposite to (i,j) in the matrix
def opPos(i, j):
    return j, i

# Generates a random symmetric matrix
def generateSymMatrix(dim):
    matrix = np.zeros((dim, dim))

    for j in range (dim):
        for i in range(dim):
            if i >= j:
                matrix[j][i] = randElem()
            else:
                opI, opJ = opPos(i, j)
                matrix[j][i] = matrix[opJ][opI]

    return matrix

def printMatrix(msg, matrix):
    print msg

    print matrix

    print ""

def QRdecomposition(A):
	n = np.shape(A)[1]

	Q =  np.zeros((n, n))
	R =  np.zeros((n, n))

	for j in range(n):

		v = A[:,j]

		for i in range(j):

			R[i,j] = dotProduct(Q[:,i], A[:,j])

			v = v.squeeze() - (R[i,j] * Q[:,i])

		R[j,j] =  np.linalg.norm(v)
		Q[:,j] = (v / R[j,j]).squeeze()

	return Q, R

def dotProduct(A, B):
    n = np.shape(A)[0]

    total = 0

    for i in range(n):
        total += A[i] * B[i]

    return total

# Returns diagonal of a square matrix
def getDiag(A):
    diag = []

    for i in range(A.shape[0]):
        diag.append(A[i][i])

    return diag

def QRIteration(A):
    Q, R = QRdecomposition(A)

    A2 = R.dot(Q)

    evectors = Q

    oldQ = Q
    while fabs(A[0][0] - A2[0][0]) >= epsilon:
        A = A2
        Q, R = QRdecomposition(A)
        A2 = R.dot(Q)

        evectors = oldQ.dot(Q)
        oldQ = evectors

    return getDiag(A2), evectors
