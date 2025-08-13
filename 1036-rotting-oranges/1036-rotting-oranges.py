from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        d = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        q = deque()
        fresh = 0

        # Step 1: Collect all rotten oranges and count fresh ones
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i, j, 0))  # (row, col, time)
                elif grid[i][j] == 1:
                    fresh += 1

        time_elapsed = 0

        while q:
            i, j, time = q.popleft()
            time_elapsed = max(time_elapsed, time)

            for dx, dy in d:
                ni, nj = i + dx, j + dy
                if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == 1:
                    grid[ni][nj] = 2   # now rotten
                    fresh -= 1
                    q.append((ni, nj, time + 1))

        # Step 3: Check if all fresh oranges are rotted
        return time_elapsed if fresh == 0 else -1
