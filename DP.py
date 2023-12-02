# Acknowledgement
# https://www.geeksforgeeks.org/vertex-cover-problem-dynamic-programming-solution-for-tree/

class Node:
	def __init__(self):
		self.data = 0
		self.vc = 0
		self.left = None
		self.right = None


# Driver program to test above functions
def main():
	# Let us construct the tree given in the above diagram
	root = Globals.newNode(20)
	root.left = Globals.newNode(8)
	root.left.left = Globals.newNode(4)
	root.left.right = Globals.newNode(12)
	root.left.right.left = Globals.newNode(10)
	root.left.right.right = Globals.newNode(14)
	root.right = Globals.newNode(22)
	root.right.right = Globals.newNode(25)

	print("Size of the smallest vertex cover is ", end='')
	print(Globals.vCover(root), end='')
	print("\n", end='')


class Globals:
	# A utility function to find min of two integers
	@staticmethod
	def min(x, y):
		if(x < y):
			return x
		else:
			return y

	# A memoization based function that returns size of the minimum vertex cover.

	@staticmethod
	def vCover(root):
		# The size of minimum vertex cover is zero if tree is empty or there
		# is only one node
		if root is None:
			return 0
		if root.left is None and root.right is None:
			return 0

		# If vertex cover for this node is already evaluated, then return it
		# to save recomputation of same subproblem again.
		if root.vc != 0:
			return root.vc

		# Calculate size of vertex cover when root is part of it
		size_incl = 1 + Globals.vCover(root.left) + Globals.vCover(root.right)

		# Calculate size of vertex cover when root is not part of it
		size_excl = 0
		if root.left:
			size_excl += 1 + \
				Globals.vCover(root.left.left) + \
				Globals.vCover(root.left.right)
		if root.right:
			size_excl += 1 + \
				Globals.vCover(root.right.left) + \
				Globals.vCover(root.right.right)

		# Minimum of two values is vertex cover, store it before returning
		root.vc = Globals.min(size_incl, size_excl)

		return root.vc

	# A utility function to create a node
	@staticmethod
	def newNode(data):
		temp = Node()
		temp.data = data
		temp.left = temp.right = None
		temp.vc = 0 # Set the vertex cover as 0
		return temp

if __name__ == '__main__':
    main()