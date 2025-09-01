class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        def rec(i,c):
            if i < 0:
                ans.append(list(c))
                return
            rec(i-1,c+[nums[i]])
            rec(i-1,c)
        ans = list()
        rec(n-1,[])
        return ans

        