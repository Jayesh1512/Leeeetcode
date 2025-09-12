class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for t in range(coin, amount + 1):
                dp[t] = min(dp[t], 1 + dp[t - coin])

        return dp[amount] if dp[amount] != float('inf') else -1
