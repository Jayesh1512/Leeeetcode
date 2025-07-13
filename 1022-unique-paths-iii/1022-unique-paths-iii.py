class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        reject = 0
        srow = scol = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    reject += 1
                elif grid[i][j] == 1:
                    srow, scol = i, j

        total = len(grid[0]) * len(grid) - reject

        def rec(total, i, j, grid, visited):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == -1 or visited[i][j] == 1:
                return 0
            if grid[i][j] == 2:
                if total == 1:
                    return 1
                else:
                    return 0

            visited[i][j] = 1
            count = (
                rec(total - 1, i + 1, j, grid, visited)
                + rec(total - 1, i - 1, j, grid, visited)
                + rec(total - 1, i, j + 1, grid, visited)
                + rec(total - 1, i, j - 1, grid, visited)
            )
            visited[i][j] = -1  
            return count

        return rec(total, srow, scol, grid, visited)
