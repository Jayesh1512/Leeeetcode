class Solution(object):
    def findTargetSumWays(self, nums, target):
        memo = {}
        
        def rec(i, t):
            if i < 0:
                return 1 if t == 0 else 0
            
            if (i, t) in memo:
                return memo[(i, t)]
            
            plus = rec(i - 1, t - nums[i])
            minus = rec(i - 1, t + nums[i])
            
            memo[(i, t)] = plus + minus
            return memo[(i, t)]
        
        return rec(len(nums) - 1, target)
