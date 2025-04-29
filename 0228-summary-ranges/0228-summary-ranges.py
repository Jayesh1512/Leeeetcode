class Solution(object):
    def summaryRanges(self, nums):
        res = []
        if not nums:
            return res
        start = nums[0]
        end = nums[0]
        for n in nums[1:]:
            if n == end + 1:
                end = n
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
                start = n
                end = n
        if start == end:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(end))
        return res