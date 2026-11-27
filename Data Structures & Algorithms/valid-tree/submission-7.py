class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        parent = [0] * n
        rank = [1] * n

        for i in range(n):
            parent[i] = i

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] = rank[rootA] + 1
            return True

        for a,b in edges:
            if not union(a, b):
                return False

        return True
        