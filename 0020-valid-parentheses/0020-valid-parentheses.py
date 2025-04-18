class Solution(object):
    @staticmethod
    def match(a, b):
        if a == ')' and b == '(': 
            return True
        if a == ']' and b == '[': 
            return True
        if a == '}' and b == '{': 
            return True
        return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif stack and self.match(i, stack[-1]):
                stack.pop()
            else:
                return False

        return len(stack) == 0
