def shellSort(array):
	gapSizes = [7, 3, 1]
	for gap in gapSizes:
		for startPosition in range(gap):
			gapInsertionSort(array, startPosition, gap)

def gapInsertionSort(array, low, gap):
	for i in range(low + gap, len(array), gap):
		currentvalue = array[i]
		position = i

		while position >= gap and array[position - gap] < currentvalue:
			array[position] = array[position - gap]
			position = position - gap

		array[position] = currentvalue

sortedList = [1, 2, 5, 10, 15, 43, 55, 67, 87, 90, 99, 100]
shellSort(sortedList)
print(sortedList)