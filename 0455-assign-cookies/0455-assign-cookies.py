class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse = True)
        s.sort(reverse = True)
        ans = 0
        for i in range(len(g)):
            if len(s) > 0:
                cookie = s[0]
                greed = g[i]

                if cookie >= greed:
                    ans += 1
                    s.pop(0)
        return ans
