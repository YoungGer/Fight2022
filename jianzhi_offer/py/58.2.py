class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        if n > len(s) or not s:
            return ''
        return ''.join([s[n:],s[:n]])