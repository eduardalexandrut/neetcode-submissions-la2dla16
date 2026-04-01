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

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    currMaxArea = 1
                    print(1)
                    
                    queue = deque([(r,  c)])

                    while queue:
                        curr_r, curr_c = queue.popleft()

                        for d in directions:

                            nr = curr_r + d[0]
                            nc = curr_c + d[1]

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                currMaxArea += 1
                                grid[nr][nc] = 0
                                queue.append((nr, nc))
                    print(currMaxArea)
                    maxArea = max(maxArea, currMaxArea)


        return maxArea