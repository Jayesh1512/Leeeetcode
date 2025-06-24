class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = set()  # use set to avoid duplicates

        for i in range(n):
            if nums[i] == key:
                for j in range(max(0, i - k), min(n, i + k + 1)):
                    ans.add(j)

        return sorted(ans)
