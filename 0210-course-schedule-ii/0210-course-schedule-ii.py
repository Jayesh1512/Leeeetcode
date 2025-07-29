from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            inDegree[a] += 1

        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])
        ans = []
        count = 0
        while queue:
            node = queue.popleft()
            ans.append(node)
            count += 1
            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        ans[::-1]
        if count == numCourses:
            return ans
        else:
            return []