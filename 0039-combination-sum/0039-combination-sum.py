class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(c, t, i, curr, ans, arr):
            if curr == t:
                ans.append(list(arr))
                return
            if i == len(c) or curr > t:
                return
            arr.append(c[i])
            backtrack(c, t, i, curr + c[i], ans, arr)
            arr.pop()
            backtrack(c, t, i + 1, curr, ans, arr)

        ans = []
        backtrack(candidates, target, 0, 0, ans, [])
        return ans
