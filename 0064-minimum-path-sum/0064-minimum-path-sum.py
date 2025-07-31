class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        def rec(i,j):
            if i == 0 and  j == 0:
                return grid[i][j]
            if i<0 or j<0:
                return float('inf')
            
            if dp[i][j] != -1:
                return dp[i][j]

            up = rec(i-1,j)
            left = rec(i,j-1)

            dp[i][j] = (min(up,left)+grid[i][j])

            return dp[i][j]



        dp = [[-1 for i in range(n)]for i in range(m)]
        ans = rec(m-1,n-1)
        return ans