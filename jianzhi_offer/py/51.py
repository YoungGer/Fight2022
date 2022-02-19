class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def ms(a):
            n = len(a)
            
            if n <= 1:
                return a, 0
            
            mi = n // 2
            
            left_a, left_reverse_pairs = ms(a[:mi])
            right_a, right_reverse_pairs = ms(a[mi:])
            
            # merge
            m, n = len(left_a), len(right_a)
            i, j = 0, 0
            
            a_update = []
            cross_reverse_pairs = 0
            while (i < m) and (j < n):
                if right_a[j] < left_a[i]:
                    # reverse pair
                    a_update.append(right_a[j])
                    cross_reverse_pairs += (m - i)
                    j += 1
                else:
                    a_update.append(left_a[i])
                    i += 1
            
            while (i < m):
                a_update.append(left_a[i])
                i += 1
                
            while (j < n):
                a_update.append(right_a[j])
                j += 1
            
            return a_update, left_reverse_pairs + right_reverse_pairs + cross_reverse_pairs
                
        _, rst = ms(nums)
        return rst