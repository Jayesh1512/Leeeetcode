class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def rec(i,j):
            if i == 0 and j == 0:
                return 1
            if i<0 or j<0 :
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            up = rec(i-1,j)
            left = rec(i,j-1)

            dp[i][j] = up+left
            return up+ left

        dp = [[-1 for i in range(n)]for i in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(n):
            dp[0][i] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

