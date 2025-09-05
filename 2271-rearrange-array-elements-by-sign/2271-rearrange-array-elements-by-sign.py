from collections import deque
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = deque()
        n = deque()
        for i in nums:
            if i >= 0:
                p.append(i)
            else:
                n.append(i)
        i = 0
        while n:
            nums[i] = p.popleft()
            i+=1
            nums[i] = n.popleft()
            i+=1

        return nums