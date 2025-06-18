class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums,i,curr,sets):
            if(i == len(nums)):
                sets.add(tuple(curr))
                return
            curr.append(nums[i])
            helper(nums,i+1,curr,sets)
            curr.pop()
            helper(nums,i+1,curr,sets)
        nums.sort()
        a = set()
        curr = []
        helper(nums,0,curr,a)
        return list(a)