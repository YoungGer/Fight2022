class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        accu_value = [[0]*n for i in range(m)]
        
        # init
        for i in range(n):
            if i == 0:
                accu_value[0][0] = grid[0][0]
            else:
                accu_value[0][i] = accu_value[0][i-1] + grid[0][i]
        for i in range(m):
            if i == 0:
                accu_value[0][0] = grid[0][0]
            else:
                accu_value[i][0] = accu_value[i-1][0] + grid[i][0]
        
        # dp
        for i in range(1, m):
            for j in range(1, n):
                accu_value[i][j] = max(accu_value[i-1][j], accu_value[i][j-1]) + grid[i][j]
        
        return accu_value[m-1][n-1]