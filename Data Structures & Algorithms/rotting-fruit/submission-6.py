class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        minutes = 0
        freshFruit = 0

        q = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshFruit += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        if freshFruit == 0:
            return 0

        while q and freshFruit > 0:
            minutes += 1

            for _ in range(len(q)):
                rr, cc = q.popleft()

                for dr, dc in directions:
                    nr = rr + dr
                    nc = cc + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        freshFruit -= 1
            

        if freshFruit > 0:
            print(freshFruit)
            return -1
        else:
            return minutes




        