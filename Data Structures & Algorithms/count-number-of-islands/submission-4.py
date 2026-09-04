class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1], [0, -1], [1, 0], [-1,0]]
        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":

                    numIslands += 1
                    q = deque([(r, c)])
                    grid[r][c] = "0"

                    while q:
                        curr_r, curr_c = q.popleft()

                        for d in directions:
                            nr = curr_r + d[0]
                            nc = curr_c + d[1]

                            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"):
                                grid[nr][nc] = "0"
                                q.append((nr, nc))

        return numIslands
