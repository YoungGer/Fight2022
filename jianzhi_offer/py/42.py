class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_array = []

        for i in nums:
            if len(max_array) == 0:
                max_array.append(i)
            else:
                max_array.append(max_array[-1] + i if max_array[-1]>0 else i)
        return max(max_array)