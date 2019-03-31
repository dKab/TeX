def pprint(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")


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

# First input asks for the matrix size (n).
# For inputs afterwards, you give the rows of the matrix one-by one, each separated by a newline.
# Enter an additional newline before entering the b, solution column. Then hitting enter will start the algorithm.
if __name__ == "__main__":
    from fractions import Fraction
    n = eval(input())

    A = [[0 for j in range(n+1)] for i in range(n)]

    # Read input data
    for i in range(0, n):
        line = map(Fraction, input().split(" "))
        for j, el in enumerate(line):
            A[i][j] = el
    input() # this is just to add one line as a separator between A matrix and B vector in console 

    lastLine = list(map(Fraction, input().split(" ")))
    for i in range(0, n):
        A[i][n] = lastLine[i]

    # Print input
    pprint(A)

    # Calculate solution
    x = gauss(A)

    # Print result
    line = "Result:\t"
    for i in range(0, n):
        line += str(x[i]) + "\t"
    print(line)
