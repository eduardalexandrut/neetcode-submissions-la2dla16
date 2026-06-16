class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [ [0, 1], [1, 0], [0, -1], [-1, 0]]

        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    numIslands += 1
                    queue = deque([(r,c)])

                    while queue:
                        current_r, current_c = queue.popleft()

                        for dr, dc in directions:
                            nr = dr + current_r
                            nc = dc + current_c

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                queue.append((nr, nc))
        
        return numIslands