class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = curr = nums[0]
        for i in range(1,n):
            curr += nums[i]
            curr = max(curr,nums[i])
            ans = max(ans,curr)
        return ans
        