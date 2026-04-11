class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        nodeMap = { i:list() for i in range(n)}

        for u, v in edges:
            nodeMap[u].append(v)
            nodeMap[v].append(u)

        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)

            for neighbour in nodeMap[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components

        