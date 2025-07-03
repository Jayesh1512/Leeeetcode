class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # def rec(i,j,m,n,dp):
        #     if i == 0 and j == 0:
        #         return 1
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     left =0
        #     right=0
        #     if i-1 >= 0:
        #         left = rec(i-1,j,m,n,dp)
        #     if j-1 >= 0:
        #         right = rec(i,j-1,m,n,dp)
        #     dp[i][j] = left+right
        #     return left+right
        # dp = [[-1 for _ in range(n)]for _ in range(m)]
        # ans = rec(m-1,n-1,m,n,dp)   
        # return ans



        #Tabulation

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i - 1][j]  
                if j > 0:
                    dp[i][j] += dp[i][j - 1]  

        return dp[m - 1][n - 1]
