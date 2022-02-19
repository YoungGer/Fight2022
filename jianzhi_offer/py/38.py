class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 1:
            return [s]

        n = len(s)
        rst = []
        seen = []
        for i in range(n):
            if s[i] not in seen:
                rst += [s[i] + j for j in self.permutation(s[:i] + s[i+1:])]
                seen.append(s[i])
        return rst