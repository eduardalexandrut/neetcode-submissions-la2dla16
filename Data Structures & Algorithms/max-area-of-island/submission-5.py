class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    count = 1
                    q = deque([(r, c)])
                    grid[r][c] = 0

                    while q:
                        curr_r, curr_c = q.popleft()

                        for dr, dc in directions:
                            nr = curr_r + dr
                            nc = curr_c + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                count += 1
                                grid[nr][nc] = 0
                                q.append((nr, nc))
                    max_area = max(max_area, count)

        return max_area

                    