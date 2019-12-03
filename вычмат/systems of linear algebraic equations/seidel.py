from math import sqrt
import numpy as np
import unittest
from fractions import Fraction
from printmatrix import pprint

def seidel(A, b, eps, maxIterations = 1e3):
	n = len(A)
	x = [.0 for i in range(n)]
	iterationsCount = 0
	converge = False
	while not converge and iterationsCount < maxIterations:
		x_new = np.copy(x)
		for i in range(n):
			s1 = sum(A[i][j] * x_new[j] for j in range(i))
			s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
			x_new[i] = (b[i] - s1 - s2) / A[i][i]

		converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
		x = x_new
		iterationsCount += 1
	if converge:
		print("Finished in {0} iterations".format(iterationsCount))
	else:
		print("Iterations limit rechead")
	return x

class TestSeidel(unittest.TestCase):
	def test_0(self):
		# First line of the file is the matrix size (n).
		# last row is vector B
		f = open('matrix.txt', 'r')
		n = int(f.readline()[0])

		A = [[0 for j in range(n)] for i in range(n)]

		for i in range(0, n):
			line = f.readline()
			line = map(Fraction, line[:len(line) - 1].split(" "))
			for j, el in enumerate(line):
				A[i][j] = el

		lastLine = f.readline()
		b = list(map(Fraction, lastLine[:len(lastLine) - 1].split(" ")))

		f.close()
		# Print input
		pprint(A, b)

		# Calculate solution
		x = seidel(A, b, 1e-4)

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