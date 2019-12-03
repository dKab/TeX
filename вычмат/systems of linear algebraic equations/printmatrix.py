def pprint(A, b = None):
	rowsCount = len(A)
	coumnsCount = rowsCount if b is not None else rowsCount + 1
	for i in range(0, rowsCount):
		line = ""
		for j in range(0, coumnsCount):
			line += str(A[i][j]) + "\t"
			if j == rowsCount-1:
				line += "| "
		if b is not None:
			line += str(b[i])
		print(line)
	print("")