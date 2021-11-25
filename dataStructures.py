class Stack():
	"""Stack lies on FI-LO principle"""
	def __init__(self):
		self.data = []


	def get_data(self):
		return self.data.pop()

	def set_data(self, value):
		self.data.append(value)

	def del_data(self):
		del self.data


class Queue(object):
	"""Queue lies on FI-FO principle"""
	def __init__(self):
		self.data = []


	def get_data(self):
		return self.data.pop() if len(self.data) else "nul" #returns first entered element or "nul" if the Queue is empty 

	def set_data(self, value):
		self.data.insert(0, value)

	def del_data(self):
		del self.data
		










if __name__ == "__main__": #the block is executed if the program is launched inside the main directory
	my_stack = Stack() #initialise a Stack instance

	[my_stack.set_data(i) for i in range(20)] #pushes elements in stack in range of 0 to 20--> last element(lies on top)

	print(my_stack.get_data()) #pops off the last element entered


	my_queue = Queue()

	[my_queue.set_data(i) for i in range(20)] #inserts elements in queue in range of 0 to 20--> first element(stands first)

	print(my_queue.get_data()) #pops off the first element in queue




			
