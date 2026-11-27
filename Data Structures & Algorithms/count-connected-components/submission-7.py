class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parents = [0] * n
        rank = [1] * n

        for i in range(n):
            parents[i] = i
        
        res = n

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union(a, b):
            nonlocal res
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return

            if rank[rootA] < rank[rootB]:
                parents[rootA] = rootB
            elif  rank[rootA] > rank[rootB]:
                parents[rootB] = rootA
            else:
                parents[rootB] = rootA
                rank[rootA] += 1
            res -= 1

        for src, dst in edges:
            union(src, dst)

        return res