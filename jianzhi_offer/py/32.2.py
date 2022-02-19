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
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        rst = []
        a = deque([root])
        flag = True
        while a:
            n = len(a)
            curr_l = []
            for _ in range(n):
                curr_node = a.popleft()
                curr_l.append(curr_node.val)
                
                if curr_node.left:
                    a.append(curr_node.left)
                if curr_node.right:
                    a.append(curr_node.right)
            
            if flag:
                rst.append(curr_l)
            else:
                rst.append(curr_l[::-1])
            
            flag = not flag
        return rst