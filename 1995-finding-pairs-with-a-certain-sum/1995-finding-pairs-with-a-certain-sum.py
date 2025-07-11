class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.freq[self.nums2[index]] -= 1  
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1  

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        ans = 0
        for a in self.nums1:  
            ans += self.freq[tot - a]  
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)