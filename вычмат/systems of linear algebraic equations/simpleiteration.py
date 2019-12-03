from printmatrix import pprint
import unittest
from fractions import Fraction

def simpleIteration(A, eps = 1e-4, maxIterations = 1e4):
	n = len(A)
	beta = [0 for i in range(n)]
	alpha = [[0 for i in range(n)] for i in range(n)]
	roots = [0 for i in range(n)]
	for i in range(n):
		beta[i] = A[i][n] / A[i][i]
		for j in range(n):
			alpha[i][j] = - A[i][j] / A[i][i] if (i != j) else 0
	
	# the first approximation - assign roots to be beta
	for i in range(n):
		roots[i] = beta[i]

	nextRoots = [0 for i in range(n)]
	deltas = [0 for i in range(n)]
	precisionReached = False
	iterationsCount = 0

	while not precisionReached and iterationsCount < maxIterations:
		for i in range(n):
			sum = 0
			for j in range(n):
				sum += alpha[i][j] * roots[j]
			nextRoots[i] = beta[i] + sum
			deltas[i] = abs(nextRoots[i] - roots[i])
			roots[i] = nextRoots[i]
		if (max(deltas) < eps):
			precisionReached = True
		iterationsCount += 1
	if precisionReached:
		print("Finished in {0} iterations".format(iterationsCount))
	else:
		print("Iterations limit rechead")
	return roots

class TestSimpleIteration(unittest.TestCase):
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
		x = simpleIteration(A)

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