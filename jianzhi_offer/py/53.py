class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i = 0
        j = len(nums) - 1
        while i <= j:
            mi = (i + j) // 2
            if nums[mi] <= target:
                i = mi + 1
            else:
                j =  mi - 1
        right = i

        i = 0
        j = len(nums) - 1
        while i <= j:
            mi = (i + j) // 2
            if nums[mi] < target:
                i = mi + 1
            else:
                j =  mi - 1
        left = j

        return right - left - 1