class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1, 0]
        ]

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    queue = deque([(r, c)])
                    grid[r][c] = 0
                    curr_area = 1

                    while queue:
                        curr_r, curr_c = queue.popleft()

                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc

                            if 0 <= nr < rows and  0 <= nc < cols and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                queue.append((nr, nc))
                                curr_area += 1
                    
                    max_area = max(max_area, curr_area)
        
        return max_area
