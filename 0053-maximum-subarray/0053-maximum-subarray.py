class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        cmax = nums[0]
        for i in range(1,len(nums)):
            cmax = max(cmax+nums[i] , nums[i])
            ans = max(ans,cmax)
        return ans