class UF:
    def __init__(self,n):
        self.parent = [i for i in range(0,n+1)]
        self.size = [1 for i in range(n+1)]

    def fp(self,n):
        if n == self.parent[n]:
            return n
        self.parent[n] = self.fp(self.parent[n])
        return self.parent[n]

    def union(self,u,v):
        pu = self.fp(u)
        pv = self.fp(v)

        if pu == pv:
            return
        
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]


class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        n = len(nums)
        uf = UF(n)
        num_to_index = {}

        for i, num in enumerate(nums):
            if num in num_to_index:
                continue 
            num_to_index[num] = i

            if num - 1 in num_to_index:
                uf.union(i, num_to_index[num - 1])
            if num + 1 in num_to_index:
                uf.union(i, num_to_index[num + 1])

        max_len = 0
        for i in range(n):
            if uf.fp(i) == i:  
                max_len = max(max_len, uf.size[i])

        return max_len
