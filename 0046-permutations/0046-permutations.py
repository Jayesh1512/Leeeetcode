class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        else:
            perms = self.permute(nums[1:])
            ins = nums[0]
            res = []
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = list(p)
                    p_copy.insert(i,ins)
                    res.append(p_copy)
            return res
        