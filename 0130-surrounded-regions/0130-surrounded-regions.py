class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(x,y):
            visited[x][y] = True
            dnd.append((x,y))
            if x-1 >=0 and not visited[x-1][y] and board[x-1][y] == 'O':
                dfs(x-1,y)
            if y-1 >=0 and not visited[x][y-1] and board[x][y-1] == 'O':
                dfs(x,y-1)
            if x+1 <len(board) and not visited[x+1][y] and board[x+1][y] == 'O':
                dfs(x+1,y)
            if y+1 <len(board[0]) and not visited[x][y+1] and board[x][y+1] == 'O':
                dfs(x,y+1)

        reg = set()
        

        m = len(board)
        n = len(board[0])

        visited = [[False for i in range(n)] for i in range(m)]

        # 1st row
        for i in range(n):
            if board[0][i] == 'O':
                reg.add((0,i))
        
        # last row
        for i in range(n):
            if board[m-1][i] == 'O':
                reg.add((m-1,i))

        #1st col
        for i in range(m):
            if board[i][0] == 'O':
                reg.add((i,0))

        #last col
        for i in range(m):
            if board[i][n-1] == 'O':
                reg.add((i,n-1))

        dnd = []
        for i in reg:
            x,y = i
            if not visited[x][y]:
                dfs(x,y)
        

        for i in range(m):
            for j in range(n):
                if (i,j) not in dnd and board[i][j] == 'O':
                    board[i][j] = 'X'