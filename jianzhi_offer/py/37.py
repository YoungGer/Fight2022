# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # 前序遍历进行序列化和反序列化

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        result = []
        def encodes(root):
            if not root:
                result.append('$')
                return
            result.append(root.val)
            encodes(root.left)
            encodes(root.right)
        encodes(root)
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        index = [0] #全局变量
        def decodes(data):
            if data[index[0]] == '$':
                index[0] += 1
                return None
            node = TreeNode(data[index[0]])
            index[0] += 1
            node.left = decodes(data)
            node.right = decodes(data)
            return node
    
        return decodes(data)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))