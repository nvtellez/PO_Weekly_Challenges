class Node:
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None

	def sortedArrToBST(arr):
		if not arr:
			return None
		mid = (len(arr)) / 2

		root = Node(arr[mid])
		root.left = sortedArrToBST(arr[:mid])
		root.right = sortedArrToBST(arr[mid+1:])