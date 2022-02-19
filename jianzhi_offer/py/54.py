# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:

        self.cnt = 0
        self.rst = -1
        self.k = k

        def dfs(node):
            if node:
                dfs(node.right)
                self.cnt += 1
                if self.cnt == self.k:
                    self.rst = node.val
                    return
                dfs(node.left)

        dfs(root)
        return self.rst