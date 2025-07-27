class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ## Detect Border Cells -> DFS on Each 
        def dfs(x,y):
            visited[x][y] == True
            grid[x][y] = 0
            if x-1 >=0 and not visited[x-1][y] and grid[x-1][y] == 1:
                dfs(x-1,y)
            
            if y-1 >=0 and not visited[x][y-1] and grid[x][y-1] == 1:
                dfs(x,y-1)
            
            if x+1 < rows and not visited[x+1][y] and grid[x+1][y] == 1:
                dfs(x+1,y)
            
            if y+1 < cols and not visited[x][y+1] and grid[x][y+1] == 1:
                dfs(x,y+1)



        border = set()

        rows = len(grid)
        cols = len(grid[0])
        ones = 0

        visited = [[False for i in range(cols)]for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and grid[i][j] == 1:
                    border.add((i,j))
                if i == rows-1 and grid[i][j] == 1:
                    border.add((i,j))
                if j == 0 and grid[i][j] == 1:
                    border.add((i,j))
                if j == cols-1 and grid[i][j] == 1:
                    border.add((i,j))
                
                if grid[i][j] == 1:
                    ones += 1

        for i in border:
            x,y = i
            if not visited[x][y]:
                dfs(x,y)

        on = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    on += 1

        print(grid)

        return on