class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rst = 0
        d = {}

        start_idx = 0
        for i, k in enumerate(s):
            if k not in d:
                d[k] = i
            else:
                last_idx = d[k]
                if last_idx >= start_idx:
                    start_idx = last_idx + 1
                d[k] = i
            rst = max(rst, i - start_idx + 1)

        return rst