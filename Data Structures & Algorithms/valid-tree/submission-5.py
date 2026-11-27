class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        adj = {i:list() for i in range(n)}

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        visiting = set()

        def dfs(node, parent):
            if node in visiting:
                return False
            
            visiting.add(node)

            for nei in adj[node]:
                if parent == nei:
                    continue

                if not dfs(nei, node):
                    return False
            #visiting.remove(node)
            return True

        if not dfs(0, -1):
            return False
        return len(visiting) == n
        