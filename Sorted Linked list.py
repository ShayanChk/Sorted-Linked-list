class SortedList:
	class Node:
		def __init__(self, data, next=None,prev=None):
			self.data=data
			self.next=next
			self.prev=prev
	def __init__(self):
		self.front=None
		self.back=None

	def insert(self,data):
		
		if self.front is None:  
			self.front = SortedList.Node(data)
			self.back = self.front
			return

		start = self.front
		if start.data > data: 
			new_node = SortedList.Node(data,start,None)
			self.front.prev = new_node
			self.front = new_node
			return

		end = self.back
		if end.data < data: 
			new_node = SortedList.Node(data,None,end)
			self.back.next = new_node
			self.back = new_node
			return
			
		_node = self.front 
		pre = _node
		while data > _node.data:
			pre=_node
			_node = _node.next
			
		new_node = SortedList.Node(data , _node , pre) # O(1)
		pre.next = new_node
		_node.prev = new_node


	def remove(self,data):
		if self.front == self.back and self.front.data == data:
			self.front = None
			self.back = None
			return True

		if self.front.data == data: 
			self.front = self.front.next
			self.front.prev = None
			return True

		if self.back.data == data: 
			tm = self.back.prev 
			tm.next = None
			self.back = tm
			return True
		
		last = self.front
		pre = last
		while data != last.data: 
			pre=last
			last = last.next
		if last.data == data:
			last.next.prev = pre 
			pre.next = last.next
			return True
		

		return False	




	def is_present(self, data): 
		for node in self.__iter__():  
			if data == node: 
				return True 
		return False 

	def __len__(self):
		count = 0  
		node = self.front 
		while node: 
			count +=1 
			node=node.next
		return count 


# The functions below called __iter__ and __reversed__ 
# allows an external function to
# iterate through your list. 
#
# myll = SortedList()
# 
# for i in myll:
#     print(i)
# 
# for i in reversed(myll):
# 	  print(i)
#
# with each iteration, curr goes through only one step of the while loop
# (ie you don't run it all at once..)
# there are two versions of these function as sentinels nodes do 
# make a difference in terms of where you start and end
# keep only the version you are using and erase the version you are 
# not using (or comment it out...)

# NOTE: if you change the names of your data members, you need
# to change them in the functions below or your tests won't pass.

# This is the version you need if you do not use sentinels:
	def __iter__(self):
		curr = self.front
		while curr:
			yield curr.data
			curr=curr.next

	def __reversed__(self):
		curr = self.back
		while curr:
			yield curr.data
			curr=curr.prev

# This is the version you need if you used sentinels:
	# def __iter__(self):
	# 	curr = self.front.next
	# 	while curr != self.back:
	# 		yield curr.data
	# 		curr=curr.next

	# def __reversed__(self):
	# 	curr = self.back.prev
	# 	while curr != self.front:
	# 		yield curr.data
	# 		curr=curr.prev
