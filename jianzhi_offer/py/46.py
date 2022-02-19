class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        a, b = 1, 1

        num_s = str(num)
        for i in range(1, len(num_s)):
            a, b = b, (a + b) if (10<= int(num_s[i-1: i+1]) <= 25) else b
        return b