class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        
        m = {i:list() for i in range(n)}

        for u, v in edges:
            m[u].append(v)
            m[v].append(u)

        visiting = set()

        def dfs(node, parent):
            visiting.add(node)

            for neighbor in m[node]:
                if neighbor == parent:
                    continue

                if neighbor in visiting:
                    return False

                if not dfs(neighbor, node):
                    return False
            
            return True

        
        if not dfs(0, -1):
            return False

        return len(visiting) == n