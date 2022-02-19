class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        def remainder(x, a, p):
            rem = 1
            for _ in range(a):
                rem = (rem * x) % p
            return rem
        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            a = n // 3
            b = n % 3 
            if b == 0:
                return int(remainder(3, a, 1e9+7))
            elif b == 1:
                return int((remainder(3, a-1, 1e9+7) * 4) % (1e9+7))
            else:
                return int((remainder(3, a, 1e9+7) * 2) % (1e9+7))