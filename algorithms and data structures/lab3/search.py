import unittest

# Linear Search
def linearSearch(numbers, search):
	for number in numbers:
		if number == search:
			return number
	return None

def findAllMatchesUsingLinearSearch(numbers, searches):
	matches = []
	for search in searches:
		match = linearSearch(numbers, search)
		if (match != None):
			matches.append(match)
	return matches

# Binary Search
def binarySearch(numbers, search):
	left = 0
	right = len(numbers) - 1
	while left < len(numbers) and right >= 0:
		mid = (left + right)//2
		middleNumber = numbers[mid]
		if middleNumber < search:
			left = mid + 1
		elif middleNumber > search:
			right = mid
		else: # it's a match
			return middleNumber
	return None

def findAllMatchesUsingBinarySearch(numbers, searches):
	matches = []
	for search in searches:
		match = binarySearch(numbers, search)
		if (match != None):
			matches.append(match)
	return matches

# Linear Indexed Search

def linearIndexedSearch(numbers, index, search):
	start = 0
	end = len(numbers) - 1
	for entry in index:
		if entry['val'] < search:
			start = entry['ind']
		if entry['val'] > search:
			end = entry['ind']
			break
		if entry['val'] == search:
			return search
	for i in range(start, end + 1):
		if numbers[i] == search:
			return search
	return None

def findAllMatchesUsingLinearIndexedSearch(numbers, index, searches):
	matches = []
	for search in searches:
		match = linearIndexedSearch(numbers, index, search)
		if (match != None):
			matches.append(match)
	return matches
		
	
class TestSearch(unittest.TestCase):
	def testLinearSaerch(self):
		sortedNumbers = [1, 3, 5, 9, 11, 16, 24, 28, 35, 40, 89, 100]
		multiplesOfFour = [16, 24, 28, 40, 100]
		linearSearchResultList = findAllMatchesUsingLinearSearch(sortedNumbers, multiplesOfFour)
		print('The result of linear search:')
		for num in linearSearchResultList:
			print(num)
		self.assertListEqual(linearSearchResultList, multiplesOfFour)
	
	def testBinarySearch(self):
		sortedNumbers = [1, 3, 5, 9, 11, 16, 24, 28, 35, 40, 89, 100]
		multiplesOfFour = [16, 24, 28, 40, 100]
		binarySearchResultList = findAllMatchesUsingBinarySearch(sortedNumbers, multiplesOfFour)
		print('The result of binary search:')
		for num in binarySearchResultList:
			print(num)
		self.assertListEqual(binarySearchResultList, multiplesOfFour)

	def testLinearIndexedSearch(self):
		index = [
			{'val': 1, 	'ind': 0}, 
			{'val': 11, 'ind': 4}, 
			{'val': 35, 'ind': 8}
		]
		sortedNumbers = [1, 3, 5, 9, 11, 16, 24, 28, 35, 40, 89, 100]
		multiplesOfFour = [16, 24, 28, 40, 100]
		linearIndexedSearchResult = findAllMatchesUsingLinearIndexedSearch(
		sortedNumbers, index, multiplesOfFour)
		print('The result of linear indexed search:')
		for num in linearIndexedSearchResult:
			print(num)
		self.assertListEqual(linearIndexedSearchResult, multiplesOfFour)

if __name__ == '__main__':
	unittest.main()
