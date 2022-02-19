class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        res=[]
        dp=[[0 for _ in range(6*n+1)]for _ in range(n+1)]#此处多留了一行0和一列0。也是为了i=1时候预留出第0行。
        for k in range(1,7):
            dp[1][k]=1
        for i in range(2,n+1):
            for j in range(i,6*i+1):
                for z in range(1,7):#此处可以理解为第i个骰子的可以掷1-6。   是转移方程dp[i][j]=dp[i-1][j-1]+dp[i-1][j-2]+...+dp[i-1][j-6]
                    if j-z>=1 and dp[i-1][j-z]!=0:
                        dp[i][j]+=dp[i-1][j-z]
        for h in range(6*n+1):
            if dp[n][h]>0:
                res.append(dp[n][h]/6.0**n)
        return res