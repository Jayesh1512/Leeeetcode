from collections import deque

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        out_degree = [0] * n
        reverse_graph = [[] for _ in range(n)]

        # Build reverse graph and count out-degrees
        for u in range(n):
            out_degree[u] = len(graph[u])
            for v in graph[u]:
                reverse_graph[v].append(u)

        # Queue for terminal nodes
        q = deque()
        for i in range(n):
            if out_degree[i] == 0:
                q.append(i)

        safe = [False] * n

        while q:
            node = q.popleft()
            safe[node] = True
            for parent in reverse_graph[node]:
                out_degree[parent] -= 1
                if out_degree[parent] == 0:
                    q.append(parent)

        return [i for i in range(n) if safe[i]]
