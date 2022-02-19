# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = deque([root])
        
        rst = []
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                rst.append(node.val)
        return rst