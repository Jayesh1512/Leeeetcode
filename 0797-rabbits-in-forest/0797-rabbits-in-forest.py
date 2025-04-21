from math import ceil

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        freq = dict()
        ans = 0
        for i in answers:
            freq[i] = freq.get(i, 0) + 1
        for i in freq:
            ans += ceil(freq[i] / float(i + 1)) * (i + 1)
        return int(ans)
