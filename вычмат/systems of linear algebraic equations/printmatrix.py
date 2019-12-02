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