class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rec(i, nums, dp):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            left = rec(i - 2, nums, dp) + nums[i]
            right = rec(i - 1, nums, dp)
            dp[i] = max(left, right)
            return dp[i]

        dp = [-1] * len(nums) 
        return rec(len(nums) - 1, nums, dp)
