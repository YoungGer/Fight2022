class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [1]
        i2, i3, i5 = 0, 0, 0

        for i in range(1, n):
            v2 = a[i2] * 2
            v3 = a[i3] * 3
            v5 = a[i5] * 5

            max_v = min([v2, v3, v5])
            a.append(max_v)

            if v2 == max_v:
                i2 += 1
            if v3 == max_v:
                i3 += 1
            if v5 == max_v:
                i5 += 1
        return a[-1]