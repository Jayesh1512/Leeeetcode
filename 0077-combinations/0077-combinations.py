class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
            
        result= []
        stack= [[]]
        
        while stack:
            current = stack.pop()
            start = current[-1] + 1 if current else 1
            
            for i in range(start, n + 1):
                new_combo = current + [i]
                if len(new_combo) == k:
                    result.append(new_combo)
                else:
                    stack.append(new_combo)
                    
        return result