class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        def helper(text, pat):
            a = pat[0]
            b = pat[1]
            
            if a == b:
                count = text.count(a)
                return (count * (count + 1)) // 2
            occA = []
            occB = []
            for i in range(len(text)):
                if text[i] == a:
                    occA.append(i)
                if text[i] == b:
                    occB.append(i)
            
            if len(occA) > len(occB):
                occB.append(len(text))
            else:
                occA.insert(0, 0)
            
            k = 0
            ans = 0
            for j in range(len(occA)):
                while k < len(occB) and occA[j] > occB[k]:
                    k += 1
                ans += len(occB) - k
            return ans
        
        return helper(text, pattern)
