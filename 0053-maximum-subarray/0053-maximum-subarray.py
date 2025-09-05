class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = nums[0]          
        curr = nums[0]         

        for i in range(1, n):
            curr = max(nums[i], curr + nums[i])  
            ans = max(ans, curr)                 

        return ans
