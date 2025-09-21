class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        board = [['.' for i in range(n)]for i in range(n)]

        def check(i,j):
            for x in range(n):
                if board[x][j] == 'Q':
                    return False
            for x in range(n):
                for y in range(n):
                    if board[x][y] == 'Q' and abs(x-i) == abs(y-j):
                        return False
            return True

        def rec(i,board):
            if i == n:
                ans.append(["".join(row) for row in board])
                return
            for j in range(n):
                if check(i,j):
                    board[i][j] = 'Q'
                    rec(i+1,board)
                    board[i][j] = '.'

        ans = []
        rec(0,board)
        return ans