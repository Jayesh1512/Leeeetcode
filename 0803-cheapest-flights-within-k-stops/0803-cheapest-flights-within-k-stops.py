import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = {i: [] for i in range(n)}
        for u, v, w in flights:
            adj[u].append((v, w))

        heap = [(0, src, 0)]
        visited = {}

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops > k:
                continue

            if node in visited and visited[node] <= stops:
                continue

            visited[node] = stops

            for nei, wt in adj.get(node, []):
                heapq.heappush(heap, (cost + wt, nei, stops + 1))

        return -1
