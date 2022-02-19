class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2

        a, b = 1, 2
        for _ in range(n-2):
            a, b = b, a + b
        return b % 1000000007