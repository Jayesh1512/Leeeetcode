class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def rec(i, j, grid, dp):
            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[0][0]
            if dp[i][j] != -1:
                return dp[i][j]
            
            up = rec(i-1, j, grid, dp)
            left = rec(i, j-1, grid, dp)
            dp[i][j] = grid[i][j] + min(up, left)
            return dp[i][j]

        row = len(grid)
        col = len(grid[0])
        dp = [[-1 for i in range(col)] for j in range(row)]
        return rec(row-1, col-1, grid, dp)
