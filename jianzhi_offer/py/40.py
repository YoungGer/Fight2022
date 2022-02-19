import heapq

class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []

        h = [-arr[i] for i in range(k)]
        heapq.heapify(h)

        for i in range(k, len(arr)):
            if (-arr[i] > h[0]):
                heapq.heappop(h)
                heapq.heappush(h, -arr[i])

        return  [-i for i in h]