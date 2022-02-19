from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def remove_deque(q, i, k):
            # remove elem whose index small
            while q and q[0] <= i-k:
                q.popleft()
                
            # remove elem whose value small
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
        
        rst = []
        q = deque()
        for i, _ in enumerate(nums):
            # remove
            remove_deque(q, i, k)
            # add
            q.append(i)
            
            if i >= k-1:
                rst.append(nums[q[0]])
        return rst