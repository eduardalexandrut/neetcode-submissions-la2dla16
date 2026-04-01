class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        rows, cols = len(grid), len(grid[0])
        numIslands = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for d in directions:
                nr, nc = r + d[0], c + d[1]

                dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                # If we find land, we've found a new island
                if grid[r][c] == "1":
                    numIslands += 1
                    dfs(r,c)
                            
        return numIslands