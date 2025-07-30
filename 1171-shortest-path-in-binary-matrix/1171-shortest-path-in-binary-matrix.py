import heapq

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        dx = [-1,-1,-1, 0,0, 1,1,1]
        dy = [-1, 0, 1,-1,1,-1,0,1]

        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = 1 

        pq = [(1, 0, 0)]  

        while pq:
            curr, x, y = heapq.heappop(pq)

            if x == n - 1 and y == n - 1:
                return curr

            if curr > dist[x][y]:
                continue

            for i in range(8):
                newx = x + dx[i]
                newy = y + dy[i]

                if 0 <= newx < n and 0 <= newy < n and grid[newx][newy] == 0:
                    if dist[newx][newy] > curr + 1:
                        dist[newx][newy] = curr + 1
                        heapq.heappush(pq, (curr + 1, newx, newy))

        return -1
