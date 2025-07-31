class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        if grid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if grid[i][0] == 0 else 0

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if grid[0][j] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
