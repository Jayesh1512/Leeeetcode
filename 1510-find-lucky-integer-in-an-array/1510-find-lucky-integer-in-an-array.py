class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        uniq = freq.keys()
        ans = -1
        for i in uniq:
            if freq[i] == i:
                ans = i
        return ans   