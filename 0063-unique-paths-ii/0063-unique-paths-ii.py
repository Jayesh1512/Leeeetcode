class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        def rec(i,j,grid,dp):
            if grid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            left =0
            right=0
            if i-1 >= 0:
                left = rec(i-1,j,grid,dp)
            if j-1 >= 0:
                right = rec(i,j-1,grid,dp)
            dp[i][j] = left+right
            return left+right
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)]for _ in range(m)]
        # if obstacleGrid[0][0] == 1:
        #     return 0
        ans = rec(m-1,n-1,obstacleGrid,dp)   
        return ans