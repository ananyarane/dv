

r = 0
c = 0
r1 = 0 
c1 = 0

def createMatrix (row_size,col_size):
	a = [[0 for j in range(col_size)] for i in range(row_size)]
	print("Enter elements of a 3 x 3 matrix")
	for i in range(row_size):
		for j in range(col_size):
			a[i][j] = int(input())

	return a

def AddMatrix (A,B):
	C = [[0 for j in range(c)] for i in range(r)]

	for i in range(r):
		for j in range(c):
			C[i][j] = A[i][j] + B[i][j]

	return C


def dotMultiplyMatrix (A, n):
	b = [[0 for j in range(c)] for i in range(r)]
	for i in range(c):
		for j in range(r):
			b[i][j] = n * A[i][j]

	return b

def crossMultiplyMatrix (A, B):
	C = [[0 for j in range(c)] for i in range(r)]
	for i in range(r):
		for j in range(c1):
			for k in range(c1):
				C[i][j] = C[i][j] + A[i][k] * B[k][j]

	return C

def determinant (A):
	d = A[0][0] *(A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) +\
	A[0][2] * (A[1][0] *A[2][1] - A[1][1] * A[2][0])

	return d

def transposeMatrix (A):
	t = [[0 for j in range(c)] for i in range(r)]
	for i in range(r):
		for j in range(c):
			t[i][j] = A[j][i]

	return t


r = 3
c = r
r1 = r
c1 = c
 

A = createMatrix(r,c)
print("Original Matrix 1:")
for i in range(r):
	for j in range(c):
		print(str(A[i][j]),end = '\t')
	print()

B = createMatrix(r1,c1)
print("Original Matrix 2:")
for i in range(r1):
	for j in range(c1):
		print(str(B[i][j]),end = '\t')
	print()

C = AddMatrix(A,B)
print("Added Matrices")
for i in range(r):
	for j in range(c):
		print(str(C[i][j]),end = '\t')
	print()

D = dotMultiplyMatrix(A,5)
print("Dot Multiplied Matrices")
for i in range(r):
	for j in range(c):
		print(str(D[i][j]),end ='\t')
	print()

E = crossMultiplyMatrix(A,B)
print("Cross Multiplied Matrices")
for i in range(r):
	for j in range(c):
		print(str(E[i][j]),end ='\t')
	print()

d = determinant(A)
print("Determinant of A: "+str(d))

F = transposeMatrix(A)
print("Transpose Matrix")
for i in range(r):
	for j in range(c):
		print(str(F[i][j]),end = ' \t')
	print()