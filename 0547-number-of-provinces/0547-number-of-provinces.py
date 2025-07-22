class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(node, g, visited):
            visited[node] = True
            for i in range(len(g)):
                if g[node][i] == 1 and not visited[i]:
                    dfs(i, g, visited)

        n = len(isConnected)
        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                dfs(i, isConnected, visited)
                count += 1

        return count
