class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(i, visited, n):
            if i > n:
                return 1
            count = 0
            for j in range(1,n+1):
                if  not visited[j] and ((j%i == 0) or (i%j ==0)):
                    visited[j] = True
                    count += f(i+1, visited, n)
                    visited[j] = False
            return count
        visited = [False] * (n+1)
        ans = f(1, visited, n)
        return ans





