class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if len(postorder) == 0:
            return True
        mi = postorder[-1]
        
        li, ri = -1, -1
        for i, k in enumerate(postorder[:-1]):
            if k > mi:
                li = i
                break
        for i, k in enumerate(postorder[:-1][::-1]):
            if k < mi:
                ri = len(postorder) - i - 2
                break 
        
        #print li, ri, postorder[li], postorder[ri]

        if li == -1 or ri == -1:
            return self.verifyPostorder(postorder[:-1])
        else:
            if li - 1 == ri:
                return self.verifyPostorder(postorder[:li+1]) and self.verifyPostorder(postorder[ri:-1])
            else:
                return False