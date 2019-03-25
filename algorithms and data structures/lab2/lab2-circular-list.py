from ListNode import ListNode

class CircularList:
	# receives ListNode to be the first element in the list
	def __init__(self, node):
		self.lst = node
		node.setPointerTo(node)
	# Inserts node which info property is set to "value" param
	# after the node to which pointer p refers
	def insertAfter(self, value, p):
		node = ListNode(value)
		node.setPointerTo(p.ptr)
		p.setPointerTo(node)
		return node
	
	# Removes list node to which pointer of p node refers
	# Returns removed node's 'info' property
	def removeAfter(self, p):
		node = p.ptr
		if node == self.lst:
			self.lst = p
		p.setPointerTo(node.ptr)
		return node.info

# In a ircle of n elements
# execute (remove) every m-th node (m > 1)
# returns k - original position of last remaining node (position is 0 - based)
def josephus(n, m):
	# create circular list with n elements
	for i in range(n):
		if i == 0:
			firstNode = ListNode(i)
			circle = CircularList(firstNode)
			last = firstNode
		else:
			last = circle.insertAfter(i, last)

	#start deleting every m-th item
	counter = n
	current = circle.lst
	while counter != 1:
		for j in range(m - 2):
			current = current.ptr
		circle.removeAfter(current)
		current = current.ptr
		counter -= 1
	return current.info
		
print(josephus(10, 3))