class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = suf = 1
        ans = float('-inf')
        n = len(nums)
        for i in range(n):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
            pre = pre * nums[i]
            suf = suf * nums[n-i-1]

            ans = max(ans,max(pre,suf))

        return ans