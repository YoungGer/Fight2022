class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        last_idx = -1
        for i, k in enumerate(nums):
            if k % 2 == 1:
                last_idx += 1
                nums[i], nums[last_idx] = nums[last_idx], nums[i]
        return nums