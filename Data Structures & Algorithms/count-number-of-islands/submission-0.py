from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()


        def bfs(rr,cc):
            q = deque([(rr,cc)])
            visited.add((rr, cc))
            while q:
                r,c = q.popleft()
                visited.add((r,c))
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if(0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited):
                        if(grid[nr][nc] == "1" ):
                            q.append((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    bfs(r, c)
        return count
                
