class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        print(freq)
        keys = freq.keys()
        keys = sorted(keys)
        cmax = 0
        for i in range(len(keys)-1):
            if (keys[i] == keys[i+1] + 1) or (keys[i] == keys[i+1] -1):
                cmax = max(cmax , freq[keys[i]]+freq[keys[i+1]])
        return cmax