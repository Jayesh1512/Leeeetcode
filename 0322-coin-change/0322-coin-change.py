class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        sorted(coins)

        def rec(i,t):
            if t == 0:
                return 0
            if i < 0:
                if t != 0:
                    return 1000000
                return 1

            if dp[i][t] != -1:
                return dp[i][t]

            take = 1000000
            if t-coins[i] >= 0:
                take = rec(i,t-coins[i])+1
            notTake = rec(i-1,t)
            dp[i][t] = min(take,notTake)
            return dp[i][t]
        dp = [[-1 for i in range(amount+1)]for i in range(len(coins)+1)]
        ans = rec(len(coins)-1,amount)
        if ans > 100000:
            return -1
        return ans 

