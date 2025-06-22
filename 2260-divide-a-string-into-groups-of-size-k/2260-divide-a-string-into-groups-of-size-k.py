class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        ans = []
        a = ""
        for i in range(len(s)):
            if(i%k == 0):
                ans.append(a)
                a = ""
            a += s[i]
        while(len(a)%k != 0):
            a += fill
        ans.append(a)
        ans.pop(0)
        return ans
