class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        def get_res(n):
            return n and n + get_res(n - 1)
        return get_res(n)