class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = collections.Counter(s)
	
        # Build string
        res = []
        for k, v in cnt.most_common():
            res += [k] * v
        return "".join(res)