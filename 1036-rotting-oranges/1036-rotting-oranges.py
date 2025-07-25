class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        q = []
        for i in rotten:
            q.append((i[0], i[1], 0))  

        time = 0 

         # BFS

        while len(q) != 0:
            x, y, t = q.pop(0)
            time = max(time, t)

            if x - 1 >= 0 and grid[x - 1][y] == 1:
                grid[x - 1][y] = 2
                q.append((x - 1, y, t + 1))
            if x + 1 < len(grid) and grid[x + 1][y] == 1:
                grid[x + 1][y] = 2
                q.append((x + 1, y, t + 1))
            if y - 1 >= 0 and grid[x][y - 1] == 1:
                grid[x][y - 1] = 2
                q.append((x, y - 1, t + 1))
            if y + 1 < len(grid[0]) and grid[x][y + 1] == 1:
                grid[x][y + 1] = 2
                q.append((x, y + 1, t + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return time
