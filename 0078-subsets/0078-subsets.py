class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def rec(i,nums,curr,ans):
            if i == len(nums):
                ans.append(list(curr))
                return
            curr.append(nums[i])
            rec(i+1,nums,curr,ans)
            curr.pop()
            rec(i+1,nums,curr,ans)
        rec(0,nums,[],ans)
        return ans