class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]

        rank = [1] * (n + 1)

        def findRoot(n):
            if parent[n] == n:
                return n

            parent[n] = findRoot(parent[n])
            return parent[n]

        def union(n1, n2):
            root1, root2 = findRoot(n1), findRoot(n2)

            if root1 == root2:
                return False

            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] > rank[root2]:
                parent[root1] = root2

            else:
                parent[root1] = root2
                rank[root2] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]