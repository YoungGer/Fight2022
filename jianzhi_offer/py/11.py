class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        def b_search(numbers, l, r):
            mi = (l + r) // 2
            mi_num = numbers[mi]
            head_num = numbers[l]
            tail_num = numbers[r]

            if head_num < tail_num:
                return head_num
            if r - l == 0:
                return head_num

            if mi_num < head_num:
                return b_search(numbers, l, mi)
            elif mi_num > head_num:
                return b_search(numbers, mi + 1, r)
            else:
                return b_search(numbers, l+1, r)
            
        N = len(numbers)
        return b_search(numbers, 0, N-1)