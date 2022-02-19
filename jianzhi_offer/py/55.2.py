# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def f(node):
            if not node:
                return True, 0
            
            left_balance, left_depth = f(node.left)
            right_balance, right_depth = f(node.right)

            flag_balance = left_balance and right_balance and abs(left_depth - right_depth) <= 1
            return flag_balance, max(left_depth, right_depth) + 1
        
        rst, _ = f(root)
        return rst