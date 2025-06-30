class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        cmax = 0
        for key in freq:
            if key + 1 in freq:
                cmax = max(cmax, freq[key] + freq[key + 1])
        return cmax
