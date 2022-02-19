# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        rst = []

        def f(node, target, seen):

            if not node:
                return

            if node.val == target and (not node.left) and (not node.right):
                rst.append(seen + [node.val])

            f(node.left, target-node.val, seen + [node.val])
            f(node.right, target-node.val, seen + [node.val])

        f(root, target, [])
        return rst