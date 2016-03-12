import QRMatrix as QR

print "=== Nana's QR decomposition ==="
dim = input("Please enter dimensions you would like to use for the matrix A : ")

matrixA = QR.generateSymMatrix(dim)
QR.printMatrix(matrixA)
