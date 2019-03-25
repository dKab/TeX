class ListNode:
	ptr = None

	def __init__(self, info):
		self.info = info
	
	def setPointerTo(self, node):
		self.ptr = node