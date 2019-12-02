from fractions import Fraction
import unittest
from printmatrix import pprint

def gauss(A):
	n = len(A)
	# First we transform the original matrix to 
	# triangular shape 
	for i in range(0, n):
		# Search for maximum in this column
		maxEl = abs(A[i][i])
		maxRow = i
		for k in range(i+1, n):
			if abs(A[k][i]) > maxEl:
				maxEl = abs(A[k][i])
				maxRow = k

		# Swap maximum row with current row (column by column)
		for k in range(i, n+1):
			tmp = A[maxRow][k]
			A[maxRow][k] = A[i][k]
			A[i][k] = tmp

		# Make all rows below this one 0 in current column
		# This is achieved by summing the two rows (multiplying one row by a number so that the modules of  the leftmost members of two rows are equal but signs are opposite)
		for k in range(i+1, n):
			# c - is the factor by which we should multiply A[i][i]
			# so that we get 0 if we sum A[i][i] with A[k][i]
			c = -A[k][i]/A[i][i]
			for j in range(i, n+1):
				if i == j:
					A[k][j] = 0
				else:
					A[k][j] += c * A[i][j]

	# Solve equation Ax=b for an upper triangular matrix A
	x = [0 for i in range(n)]
	# for every row starting from the last
	for i in range(n-1, -1, -1):
		x[i] = A[i][n]/A[i][i] # x[i] = b/A[i][i]
		# for every row in current column starting from the last
		for k in range(i-1, -1, -1):
			# moving the corresponding member to the right side of the equation
			A[k][n] -= A[k][i] * x[i] # b -= A[k][i] * x[i]
	return x

class TestGauss(unittest.TestCase):
	def test_0(self):
		# First line of the file is the matrix size (n).
		# last row is vector B
		f = open('matrix.txt', 'r')
		n = int(f.readline()[0])

		A = [[0 for j in range(n+1)] for i in range(n)]

		for i in range(0, n):
			line = f.readline()
			line = map(Fraction, line[:len(line) - 1].split(" "))
			for j, el in enumerate(line):
				A[i][j] = el

		lastLine = f.readline()
		lastLine = list(map(Fraction, lastLine[:len(lastLine) - 1].split(" ")))
		for i in range(0, n):
			A[i][n] = lastLine[i]

		f.close()
		# Print input
		pprint(A)

		# Calculate solution
		x = gauss(A)

		# Print result
		line = "Result:\t"
		for i in range(0, n):
			line += str(float(x[i])) + "\t"
		print(line)
		x1, x2, x3 = 4.76, -3.23, 7.12
		# x = gauss(A)
		self.assertAlmostEqual(x1, round(float(x[0]), 2), 2)
		self.assertAlmostEqual(x2, round(float(x[1]), 2), 2)
		self.assertAlmostEqual(x3, round(float(x[2]), 2), 2)

if __name__ == '__main__':
	unittest.main()