class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def allow(i, j, res):
            for r in range(len(res)):
                c = res[r]
                if c == j or abs(i - r) == abs(j - c): 
                    return False
            return True

        def backtrack(i, res, ans):
            if i == n:
                ans.append(list(res))
                return
            for j in range(n):
                if allow(i, j, res):
                    res.append(j)
                    backtrack(i + 1, res, ans)
                    res.pop()
        ans = []
        backtrack(0,[],ans)
        return len(ans)