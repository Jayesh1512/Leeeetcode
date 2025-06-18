#FIBONACCI HAI BC
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        prev2 = 2
        prev1 = 3
        for i in range(4,n+1):
            curr = prev2+prev1
            prev2 = prev1
            prev1 = curr

        return curr