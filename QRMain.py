import QRMatrix as QR

print "=== Nana's QR decomposition ==="
dim = input("Please enter dimensions you would like to use for the matrix A : ")

A = QR.t1 #QR.generateSymMatrix(dim)
QR.printMatrix("Matrix A =", A)

Q, R = QR.gram_schmidt(A)
QR.printMatrix("Initial Matrix Q =", Q)
QR.printMatrix("Initial Matrix R =", R)

eigenvalues, eigenvectors = QR.QRIteration(A)

QR.printMatrix("eigenvalues =", eigenvalues)
QR.printMatrix("eigenvectors =", eigenvectors)
