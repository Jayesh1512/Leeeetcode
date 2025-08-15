class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1) 

    def findParent(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return False  # No merge happened

        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return True  # Merge happened


class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        r, c = len(grid), len(grid[0])
        idx = 1
        count = 0  # Track number of islands

        # Step 1: Assign IDs & count land
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    grid[i][j] = idx
                    idx += 1
                    count += 1  
                else:
                    grid[i][j] = 0

        us = UF(idx-1)

        directions = [(0, 1), (1, 0)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    for dx, dy in directions: 
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] != 0:
                            if us.union(grid[i][j], grid[ni][nj]):
                                count -= 1

        return count
