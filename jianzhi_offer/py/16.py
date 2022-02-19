class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == -1:
            return 1.0 / x
        if n % 2 == 0:
            a = self.myPow(x, n // 2)
            return a * a
        else:
            return self.myPow(x, n-1) * x