class Stack():
	"""Stack lies on FILO principle"""
	def __init__(self):
		self.data = []


	def get_data(self):
		return self.data.pop()

	def set_data(self, value):
		self.data.append(value)

	def del_data(self):
		del self.data


class Queue(object):
	"""Queue lies on FIFO principle"""
	def __init__(self):
		self.data = []


	def get_data(self):
		result = self.data[0] if bool (len(self.data)) else 0
		return result

	def set_data(self, value):
		self.data.insert(-1, value)

	def del_data(self):
		del self.data
		










if __name__ == "__main__":
	my_stack = Stack()

	[my_stack.set_data(i) for i in range(20)]

	print(my_stack.get_data())


	my_queue = Queue()

	[my_queue.set_data(i) for i in range(20)]

	print(my_queue.get_data())
		