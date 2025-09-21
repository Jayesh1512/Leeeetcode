class Solution(object):
    def solveSudoku(self, b):
        """
        :type b: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(b)

        def check(i, j, val):
            # Row and col check
            for x in range(n):
                if b[i][x] == val or b[x][j] == val:
                    return False

            # 3x3 subgrid check
            start_row = (i // 3) * 3
            start_col = (j // 3) * 3
            for x in range(start_row, start_row + 3):
                for y in range(start_col, start_col + 3):
                    if b[x][y] == val:
                        return False

            return True

        def rec(x, y):
            if x == n:  # board completely filled
                return True
            if y == n:
                return rec(x + 1, 0)

            if b[x][y] != '.':  # skip pre-filled cells
                return rec(x, y + 1)

            for z in range(1, 10):  # try digits 1–9
                val = str(z)
                if check(x, y, val):
                    b[x][y] = val
                    if rec(x, y + 1):  # if solution found
                        return True
                    b[x][y] = '.'  # backtrack

            return False  # no valid number

        rec(0, 0)
