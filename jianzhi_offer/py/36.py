"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def dfs(node):
            if not node:
                return None, None

            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)
            
            node.left, node.right = left_max, right_min
            if left_max:
                left_max.right = node
            if right_min:
                right_min.left = node
            
            return left_min if left_min else node, right_max if right_max else node
        
        if not root:
            return None
        
        min_node, max_node = dfs(root)
        min_node.left, max_node.right = max_node, min_node
        return min_node