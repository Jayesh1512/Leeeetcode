class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
    
        dp = [[-1 for i in range(n)]for i in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(n):
            dp[0][i] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

