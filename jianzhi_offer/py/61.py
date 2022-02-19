class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        cnt = 0
        for i in range(4):
            if nums[i] != 0:
                if nums[i+1] == nums[i]:
                    return False
                else:
                    cnt += nums[i+1] - nums[i]
        return cnt < 5