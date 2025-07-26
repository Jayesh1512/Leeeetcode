class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])

        ans = [[-1 for i in range(cols)] for i in range(rows)]  # -1 = unvisited

        q = []

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    ans[i][j] = 0  # visited & distance 0

        while len(q) != 0:
            x, y, count = q.pop(0)

            cDist = count + 1

            if x - 1 >= 0 and ans[x - 1][y] == -1:
                ans[x - 1][y] = cDist
                q.append((x - 1, y, cDist))

            if y - 1 >= 0 and ans[x][y - 1] == -1:
                ans[x][y - 1] = cDist
                q.append((x, y - 1, cDist))

            if x + 1 < rows and ans[x + 1][y] == -1:
                ans[x + 1][y] = cDist
                q.append((x + 1, y, cDist))

            if y + 1 < cols and ans[x][y + 1] == -1:
                ans[x][y + 1] = cDist
                q.append((x, y + 1, cDist))

        return ans
