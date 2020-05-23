# A collection of tree-structure related class and functions

# Class
# TreeNode: constructs the binary tree node, with two children and self value
# BinaryTree: constructs a binary tree with the first node as root

from collections import deque 

class TreeNode:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

class BinaryTree:
	def __init__(self, root):
		self.root = TreeNode(root)

	def compute_tree_depth(self):
		# compute tree depth of a given tree node
		# Return:
		#		int: depth of the tree
		def _get_depth(cur_node):
			if not cur_node:
				return -1
			return max(1 + _get_depth(cur_node.right), 1 + _get_depth(cur_node.left))
		return _get_depth(self.root)

	def is_exist_val(self, val):
		# check whether a val exists in the tree
		# Return:
		#		bool: whether or not a node's value equals the query val
		def _is_val(cur_node):
			if not cur_node:
				return False
			if cur_node.val == val:
				return True
			return _is_val(cur_node.right) or _is_val(cur_node.left)
		return _is_val(self.root)

	def is_exist_subtree(self, subtree):
		# locate subtree root in the parent tree
		# Return:
		#		bool: whether a subtree is a part of the tree
		def _is_equal(node1, node2):
			if not node2:
				return True
			if node1.val != node2.val:
				print('not euqal: ', node1.val, node2.val)
				return False
			return _is_equal(node1.left, node2.left) and _is_equal(node1.right, node2.right)

		def _is_subtree(cur_node):
			if not cur_node:
				return False
			if cur_node.val == subtree.root.val:
				return _is_equal(cur_node, subtree.root)
			return _is_subtree(cur_node.left) or _is_subtree(cur_node.right)

		return _is_subtree(self.root)

	def get_closest_val(self, value):
		# retrieve the node with value that is closest to the query value
		# Return:
		#		int: the closeest value
		def _get_closest(cur_node, cur_min_val):
			if not cur_node:
				return cur_min_val
			if abs(cur_min_val - value) > abs(cur_node.val - value):
				cur_min_val = cur_node.val
			left_minval = _get_closest(cur_node.left, cur_min_val)
			right_minval = _get_closest(cur_node.right, cur_min_val)
			return left_minval if abs(left_minval - value) <= abs(right_minval - value) else right_minval
		return _get_closest(self.root, float('inf'))

	def compute_num_node_at_depth(self, depth):
		# given a tree depth, compute the number of nodes at that depth
		# Return:
		# 		int: the number of nodes at given depth
		queue = deque([])
		queue.append(self.root)
		queue.append(None)
		level = 1
		num_node = 0
		while queue:
			cur_node = queue.popleft()
			if cur_node == None:
				# finish traversing through level, going to next level
				if level == depth:
					return num_node
				if len(queue) == 0:
					return num_node
				level += 1
				num_node = 0
				queue.append(None)
			else:
				if cur_node.left:
					queue.append(cur_node.left)
					num_node += 1
				if cur_node.right:
					queue.append(cur_node.right)
					num_node += 1

	def compute_max_tree_path(self):
		# Compute the maximum path sum of the tree
		# Return:
		#		int: max sum of path
		def _get_max_path(cur_node):
			left = 0
			right = 0
			leftsum = 0
			rightsum = 0
			if cur_node.left:
				left, leftsum = _get_max_path(cur_node.left)
				left = max(left, 0)
			if cur_node.right:
				right, rightsum = _get_max_path(cur_node.right)
				right = max(right, 0)
			
			return cur_node.val + max(left, right), max(cur_node.val + left + right, leftsum, rightsum)
		return _get_max_path(self.root)[1]


	def is_consin(self, val1, val2):
		# check whether val1 and val2 have the same depth while not the same parent
		# Return:
		#		bool: whether val1 and val2 is a cousin pair
		stored = dict()
		parent = dict()
		
		def get_depth_and_parent(cur_node, key, depth, par):
			if not cur_node:
				return
			if cur_node.val == key:
				stored[cur_node.val] = depth
				parent[cur_node.val] = par.val

			get_depth_and_parent(cur_node.left, key, depth+1, cur_node)
			get_depth_and_parent(cur_node.right, key, depth+1, cur_node)
		
		get_depth_and_parent(root, x, 0, None)
		get_depth_and_parent(root, y, 0, None)
		
		return stored[x] == stored[y] and parent[x] != parent[y]

# --------------- Construct our test binary tree ----------------
tree = BinaryTree(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(10)
tree.root.left.left.left = TreeNode(14)
tree.root.left.left.right = TreeNode(12)
tree.root.left.right.left = TreeNode(8)
tree.root.left.right.right = TreeNode(9)

subtree = BinaryTree(3)
subtree.root.left = TreeNode(6)
subtree.root.right = TreeNode(10)

# ----------------------- Begin our tests ----------------------
query_val = 9
query_depth = 3
print('1. Tree depth is: ', tree.compute_tree_depth())
print('2. Value %d exits in tree? '%(query_val), tree.is_exist_val(query_val))
print('3. Closest value in the tree to query is: ', tree.get_closest_val(query_val))
print('4. Subtree exits in tree?', tree.is_exist_subtree(subtree))
print('5. Number of nodes at tree depth %d is: '%(query_depth), tree.compute_num_node_at_depth(query_depth))
print('6. Max tree path has value: ', tree.compute_max_tree_path())
