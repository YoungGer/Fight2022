class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        length = len(a)
        C = [1] * length
        D = [1] * length
        result = []
        for i in range(1,length):#求C[i]
            C[i] = C[i-1] * a[i-1]
        for i in reversed(range(length-1)):#D[i]
            D[i] = D[i+1] * a[i+1]
        for i in range(length):#求B[i]
            result.append(C[i]*D[i])
        return result