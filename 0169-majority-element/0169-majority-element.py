from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c1 = Counter(nums)
        n = len(nums)
        for i in c1.keys():
            if c1[i] > n//2:
                return i
        return 0