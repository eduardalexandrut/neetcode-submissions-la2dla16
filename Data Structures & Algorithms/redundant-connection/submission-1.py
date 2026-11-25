class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for  i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node):
            if node == parents[node]: #node is it's own father, we return it
                return parents[node]

            parents[node] = find(parents[node])
            return parents[node]

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2: # node1 and node2 have the same root/parent -> they are united
                return False

            if rank[parent1] > rank[parent2]:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]

            return True


        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]