import QRMatrix as QR

print "=== Nana's QR decomposition ==="
dim = input("Please enter dimensions you would like to use for the matrix A : ")

A = QR.generateSymMatrix(dim)
QR.printMatrix("Matrix A =", A)

Q, R = QR.QRdecomposition(A)
QR.printMatrix("Initial Matrix Q =", Q)
QR.printMatrix("Initial Matrix R =", R)

eigenvalues, eigenvectors = QR.QRIteration(A)

QR.printMatrix("eigenvalues =", eigenvalues)
QR.printMatrix("eigenvectors =", eigenvectors)

f = open('result.txt','w')
f.write("Eigenvalues: " + '\n')
f.write(str(eigenvalues) + "\n\n")
f.write("Eigenvectors: " + '\n')
f.write(str(eigenvectors) + '\n')
f.close()
