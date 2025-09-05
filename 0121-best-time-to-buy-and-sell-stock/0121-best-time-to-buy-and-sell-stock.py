class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        r = [0] * n
        r[n-1] = prices[n-1]
        for i in range(n-2,-1,-1):
            r[i] = max(prices[i],r[i+1])
        ans = 0
        for i in range(n):
            ans = max(ans,(r[i]-prices[i]))
        return ans
