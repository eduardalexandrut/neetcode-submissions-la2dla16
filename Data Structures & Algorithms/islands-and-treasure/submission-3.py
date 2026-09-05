class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dist = [[0,1], [0,-1], [1, 0], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])

        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()

            for dr, dc in dist:
                nr, nc = r + dr, c + dc

                # Check boundaries and whether the cell is an empty room (2**31 - 1)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2**31 - 1:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
