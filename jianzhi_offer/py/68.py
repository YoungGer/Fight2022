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
        if p.val > q.val:
            min_, max_ = q.val, p.val
        else:
            min_, max_ = p.val, q.val
        
        if root.val >= min_ and root.val <= max_:
            return root
        elif min_ > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif max_ < root.val:
            return self.lowestCommonAncestor(root.left, p, q)