class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = [1.0] * n  # ratio to parent

    def find(self, x):
        if self.parent[x] != x:
            orig_parent = self.parent[x]
            self.parent[x] = self.find(orig_parent)
            self.weight[x] *= self.weight[orig_parent]
        return self.parent[x]

    def union(self, x, y, value):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y
        self.weight[root_x] = self.weight[y] * value / self.weight[x]

class Solution:
    def calcEquation(self, equations, values, queries):
        #  
        var_idx = {}
        idx = 0
        for a, b in equations:
            if a not in var_idx:
                var_idx[a] = idx
                idx += 1
            if b not in var_idx:
                var_idx[b] = idx
                idx += 1

        uf = UF(len(var_idx))

        for (a, b), val in zip(equations, values):
            uf.union(var_idx[a], var_idx[b], val)

        # Step 3: answer queries
        res = []
        for a, b in queries:
            if a not in var_idx or b not in var_idx:
                res.append(-1.0)
                continue
            root_a = uf.find(var_idx[a])
            root_b = uf.find(var_idx[b])
            if root_a != root_b:
                res.append(-1.0)
            else:
                res.append(uf.weight[var_idx[a]] / uf.weight[var_idx[b]])
        return res
