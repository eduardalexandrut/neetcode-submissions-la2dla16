class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        m = {i:[] for i in range(n)}

        for u, v in edges:
            m[u].append(v)
            m[v].append(u)

        res = 0
        visited = set()

        def dfs(node):
            visited.add(node)

            for ne in m[node]:
                if ne in visited:
                    continue

                dfs(ne)

        for e in range(n):
            if e not in visited:
                dfs(e)
                res += 1

        return res
