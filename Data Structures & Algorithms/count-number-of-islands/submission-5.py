class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        sol = 0

        def bfs(r, c):
            q = deque([])
            q.append((r,c))

            while q:
                rr, cc = q.pop()

                for dr, dc in directions:
                    nr = rr + dr
                    nc = cc + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"
                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    sol +=1

        return sol