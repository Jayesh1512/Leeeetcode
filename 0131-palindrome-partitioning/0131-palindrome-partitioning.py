class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path, ans):
            if start == len(s):
                ans.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if is_palindrome(substr):
                    path.append(substr)
                    backtrack(end, path, ans)
                    path.pop()

        ans = []
        backtrack(0, [], ans)
        return ans
