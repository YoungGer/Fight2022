class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_n = str(n)
        length = len(str_n)
        
        rst = 0
        for i in range(length):
            base = 10**(length-1-i)
            
            # a,mi,b
            if length == 1:
                a = 0
                b = 0
            else:
                if i == 0:
                    a = 0
                    b = int(str_n[i+1:])
                elif i == length - 1:
                    a = int(str_n[:i])
                    b = 0
                else:
                    a = int(str_n[:i])
                    b = int(str_n[i+1:])
            
            mi = int(str_n[i])
            if mi > 1:
                rst += (a+1) * base
            elif mi == 1:
                rst += a*base + b + 1
            elif mi == 0:
                rst += a * base

        return rst