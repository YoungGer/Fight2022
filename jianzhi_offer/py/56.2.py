class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        if nums[0] != nums[1]:
            return nums[0]
        for i in range(1, length-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
        return nums[length-1]