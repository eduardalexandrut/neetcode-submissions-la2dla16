class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [0] * (len(edges) + 1)
        rank = [1] * (len(edges) + 1)

        for i in range((len(edges) + 1)):
            parents[i] = i

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            if rank[rootA] < rank[rootB]:
                parents[rootA] = rootB
            elif rank[rootA] > rank[rootB]:
                parents[rootB] = rootA
            else:
                parents[rootB] = rootA
                rank[rootA] += 1

            return True

        for src, dst in edges:
            if not union(src, dst):
                return [src, dst]