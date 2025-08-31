class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def rec(i,oc,cc,c):
            if i == 2*n:
                ans.append(c)
                return
            if cc > oc:
                return
            if oc < n:
                rec(i+1,oc+1,cc,c+"(")
            if cc < oc:
                rec(i+1,oc,cc+1,c+')')

        ans = list()
        rec(0,0,0,"")
        return ans