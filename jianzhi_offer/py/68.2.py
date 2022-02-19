# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.rst = None

        def dfs(node, p, q):
            if not node:
                return False, False

            p1, q1 = dfs(node.left, p, q)
            p2, q2 = dfs(node.right, p, q)

            if node == p and (q1 or q2):
                self.rst = node
            if node == q and (p1 or p2):
                self.rst = node
            if (p1 and q2) or (q1 and p2):
                self.rst = node
            
            return p1 or p2 or node==p, q1 or q2 or node==q 

        dfs(root, p, q)
        return self.rst