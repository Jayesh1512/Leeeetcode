class Solution(object):
    def permute(self, nums):
        n = len(nums)
        ans = []
        used = [False] * n

        def rec(i, l):
            if i == n:
                ans.append(list(l))
                return
            for j in range(n):
                if not used[j]:
                    used[j] = True
                    l.append(nums[j])
                    rec(i + 1, l)  
                    l.pop()
                    used[j] = False

        rec(0, [])
        return ans
