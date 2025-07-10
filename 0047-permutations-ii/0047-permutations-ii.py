class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def bt(ind, visited, nums, curr, ans):
            if ind == len(nums):
                ans.append(list(curr))
                return
            prev = None
            for i in range(len(nums)):
                if not visited[i]:
                    if prev is not None and nums[i] == prev:
                        continue
                    visited[i] = True
                    curr.append(nums[i])
                    bt(ind + 1, visited, nums, curr, ans)
                    curr.pop()
                    visited[i] = False
                    prev = nums[i]

        nums.sort()  
        visited = [False] * len(nums)
        ans = []
        bt(0, visited, nums, [], ans)
        return ans
