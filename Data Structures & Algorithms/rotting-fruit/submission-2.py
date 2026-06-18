class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        minutes = 0
        fresh_oranges = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        while queue and fresh_oranges > 0:
            minutes += 1
            for _ in range(len(queue)):
                curr_r, curr_c = queue.popleft()
                for dr, dc in directions:
                    nr = dr + curr_r
                    nc = dc + curr_c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        queue.append((nr, nc))
            
        
        return minutes if fresh_oranges == 0 else -1


        