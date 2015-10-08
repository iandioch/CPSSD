class BinaryTreeNode:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

	# add a child to this node or the appropriate subnode
	def add_child(self, child_value):
		if(child_value < self.value):
			if self.left is None:
				self.left = BinaryTreeNode(child_value)
			else:
				self.left.add_child(child_value)
		else:
			if self.right is None:
				self.right = BinaryTreeNode(child_value)
			else:
				self.right.add_child(child_value)


	def print_children(self):
		print str(self.value) + ": " + str(self.left) + ", " + str(self.right)
		if self.left is not None:
			self.left.print_children()
		if self.right is not None:
			self.right.print_children()

	def __str__(self):
		return "BinaryTreeNode(" + str(self.value) + ")"

	# return a reference to the node with the given value
	def find_value(self, looking_for):
		print "Looking for " + str(looking_for) + " in " + str(self)
		if looking_for == self.value:
			return self
		if looking_for < self.value and self.left is not None:
			return self.left.find_value(looking_for)
		if self.right is not None:
			return self.right.find_value(looking_for)
		return None

# contains a reference to the root
class BinarySearchTree:
	def __init__(self, nums):
		self.root = BinaryTreeNode(nums[0])
		for i in nums[1:]:
			self.root.add_child(i)
		self.root.print_children()

	def find_value(self, looking_for):
		return self.root.find_value(looking_for)

# read in the input and split by space
raw_nums = raw_input("Enter a list of space separated integers: ").split()
nums = []
# convert to ints
for s in raw_nums:
	nums.append(int(s.strip()))
tree = BinarySearchTree(nums)

print tree.find_value(7)
print tree.find_value(21)
