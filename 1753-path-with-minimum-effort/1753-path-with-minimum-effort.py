import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        # Min-heap: (effort, x, y)
        pq = [(0, 0, 0)]

        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            effort, x, y = heapq.heappop(pq)
            if x == rows - 1 and y == cols - 1:
                return effort

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    diff = abs(heights[nx][ny] - heights[x][y])
                    new_effort = max(effort, diff)
                    if dist[nx][ny] > new_effort:
                        dist[nx][ny] = new_effort
                        heapq.heappush(pq, (new_effort, nx, ny))
        return 0
