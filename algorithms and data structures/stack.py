class Stack: 
	def __init__(self):
		self.stack = []

	def push(self, elem):
		self.stack.append(elem)

	def pop(self):
		if len(self.stack) == 0:
			return None
		else:
			return self.stack.pop()

	def empty(self):
		return len(self.stack) == 0

	def stackTop(self):
		if self.empty():
			return None
		else:
			return self.stack[len(self.stack) - 1]

charactersStack = Stack()

for i in range(4):
	charactersStack.push(i)

# The stack has even number of elements now.

# works only for stacks with length > 1
def insertInTheMiddle(stack, elementToInsert):
	helperStack = Stack()
	size = 0
	while stack.empty() == False:
		helperStack.push(stack.pop())
		size += 1

	if (size % 2) == 0:
		#size is even
		position = size / 2
	else:
		#size is odd
		position = (size // 2) + 1

	for i in range(size + 1):
		if i == position:
			stack.push(elementToInsert)
		else:
			stack.push(helperStack.pop())
	
	return stack



insertInTheMiddle(charactersStack, '*')
# Checking the result:
while charactersStack.empty() == False:
	print(charactersStack.pop())
#expected result: 
# 3
# 2
# *
# 1
# 0
print('=========================================')
#test the function on odd sized stack:
charactersStack2 = Stack()
for i in range(5):
	charactersStack2.push(i)

insertInTheMiddle(charactersStack2, '*')

while charactersStack2.empty() == False:
	print(charactersStack2.pop())
#expected result
# 4
# 3
# *
# 2
# 1
# 0


