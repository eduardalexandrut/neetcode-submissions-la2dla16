class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        if ROWS == 1 and COLS == 1:
            return grid[0][0]

        done = False
        level = 0

        while not done:
            if grid[0][0] > level:
                level += 1
                continue
            q = deque([(0,0)])
            visited = {(0, 0)}
            #print('ci')
            while q:
                rr, cc = q.popleft()

                for dr, dc in directions:
                    nr = rr + dr
                    nc = cc + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] <= level and (nr, nc) not in visited:
                        if nr == ROWS -1 and nc == COLS - 1:
                            done = True
                            break
                        q.append((nr, nc))
                        visited.add((nr, nc))
            if not done:
                level += 1
            visited = set()
        return level