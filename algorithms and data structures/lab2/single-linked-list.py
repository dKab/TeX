class SingleLinkedList:
	def __init__(self):
		self.lst = None
	# Inserts node with info propery = value to the beginning of the list
	def unshift(self, value):
		node = ListNode(value)
		if self.lst != None:
			node.setPointerTo(self.lst)
		self.lst = node
	# Removes first node of the list
	# Returns removed node's 'info' property
	def shift(self):
		if self.lst == None:
			return None
		else:
			data = self.lst.info
			self.lst = self.lst.ptr
			return data 

	# Inserts node which info property is set to "value" param
	# after the node to which pointer p refers
	def insertAfter(self, p, value):
		node = ListNode(value)
		node.setPointerTo(p.ptr)
		p.setPointerTo(node)
	
	# Removes list node to which pointer of p node refers
	# Returns removed node's 'info' property
	def removeAfter(self, p):
		if p.ptr == None:
			return None
		else:
			node = p.ptr
			p.setPointerTo(node.ptr)
			return node.info

class ListNode:
	ptr = None

	def __init__(self, info):
		self.info = info
	
	def setPointerTo(self, node):
		self.ptr = node

# Removes n-th element from the list
# n is 1 based. So if it was an array, n = 1 would mean that
# elemenent at index 0 would be deleted.
# Returns info property of removed node
def removeNth(list, n):
	#find a node before the one that we need to remove, i.e. n - 1
	node = list.lst
	if n > 1:
		for i in range(n - 2):
			node = node.ptr
			if node == None:
				return
		return list.removeAfter(node)
	else: # n == 1 - removing first element
		return list.shift()

# Testing:
testList = SingleLinkedList()
testList.unshift('d')
testList.unshift('c')
testList.unshift('b')
testList.unshift('a')
# list now have structure: abcd
removeNth(testList, 2) # removing "b" letter
#printing to check
letter = testList.lst
while letter.ptr != None:
	print(letter.info)
	letter = letter.ptr
print(letter.info) 
# expected result: acd



