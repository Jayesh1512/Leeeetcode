from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque

        rows = len(mat)
        cols = len(mat[0])
        ans = [[-1 for _ in range(cols)] for _ in range(rows)]

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    ans[i][j] = 0

        while q:
            x, y, count = q.popleft()  # O(1)

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
