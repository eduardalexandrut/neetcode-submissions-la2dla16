class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]

        pacific_reachable = set()
        atlantic_reachable = set()

        res = []

        def bfs(starts):
            reachable = set()
            queue = deque(starts)
            reachable.update(starts)

            while queue:
                curr_r, curr_c = queue.popleft()

                for dr, dc in directions:
                        nr = curr_r + dr
                        nc = curr_c + dc

                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reachable:
                            if heights[nr][nc] >= heights[curr_r][curr_c]:
                                reachable.add((nr, nc))
                                queue.append((nr, nc))
            return reachable

        pacific_start = []
        atlantic_start = []

        for r in range(rows):
            pacific_start.append((r, 0))          # Left edge
            atlantic_start.append((r, cols - 1))  # Right edge
            
        for c in range(cols):
            pacific_start.append((0, c))          # Top edge
            atlantic_start.append((rows - 1, c))  # Bottom edge
        
        pacific_reachable = bfs(pacific_start)
        atlantic_reachable = bfs(atlantic_start)
        
        return [list(cell) for cell in pacific_reachable.intersection(atlantic_reachable)]
                            
        