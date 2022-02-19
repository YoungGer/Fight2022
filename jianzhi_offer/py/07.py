# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        inorder_root_index = inorder.index(root_val)
        left_length = inorder_root_index
        right_length = len(inorder) - inorder_root_index - 1
        
        left_preorder = preorder[1: 1+left_length]
        left_inorder = inorder[:left_length]
        
        right_preorder = preorder[1+left_length:]
        right_inorder = inorder[left_length+1:]
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root