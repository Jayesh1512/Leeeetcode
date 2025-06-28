class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def eval(nums):
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

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        return max(eval(nums[1:]), eval(nums[:-1]))
