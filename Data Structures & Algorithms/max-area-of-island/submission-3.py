class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [
            [0,1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        maxArea = 0
        currMaxArea = 0

        def dfs(r, c):
            nonlocal currMaxArea
            nonlocal maxArea
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return

            grid[r][c] = 0
            currMaxArea += 1
            print(currMaxArea)
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                dfs(nr, nc)
            maxArea = max(maxArea, currMaxArea)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    currMaxArea = 0
                    dfs(r, c)

        return maxArea