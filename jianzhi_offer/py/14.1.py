class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            a = n // 3
            b = n % 3 
            if b == 0:
                return 3 ** a
            elif b == 1:
                return 3 ** (a-1) * 4
            else:
                return 3 ** a * 2