class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i:list() for i in range(n)}

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()
        res = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
            return

        for i in range(n):
            if i not in visited:
                dfs(i)
                res +=1

        return res