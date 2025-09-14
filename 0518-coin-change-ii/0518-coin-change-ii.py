class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        def rec(i,t):
            if i == 0:
                if t % coins[0] == 0:
                    return 1
                else:
                    return 0
            if t == 0:
                return 1
            if i<0 or t<0:
                return 0
            
            if (i,t) in memo:
                return memo[(i,t)]

            take = rec(i, t-coins[i])
            notTake = rec(i-1,t)
            memo[(i,t)] = take + notTake
            return take + notTake
        memo = {}
        return rec(len(coins)-1,amount)