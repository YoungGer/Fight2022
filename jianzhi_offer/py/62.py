class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n < 1 or m < 1:
            return None
        last = 0
        for i in range(2, n+1):
            last = (last + m)%i
        return last