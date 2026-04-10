class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. The edge count MUST be n - 1
        if len(edges) != n - 1:
            return False

        # 2. Build the Adjacency List (Bi-directional)
        nodeMap = {i: [] for i in range(n)}
        for u, v in edges:
            nodeMap[u].append(v)
            nodeMap[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            
            for neighbor in nodeMap[node]:
                # Ignore the node we just came from
                if neighbor == parent:
                    continue
                
                # If neighbor is already in visited, it's a cycle!
                if neighbor in visited:
                    return False
                
                if not dfs(neighbor, node):
                    return False
            
            return True

        # 3. Start DFS and check for cycles
        # (Start at node 0, parent is -1)
        if not dfs(0, -1):
            return False

        # 4. Connectivity check: Did we reach every node?
        return len(visited) == n