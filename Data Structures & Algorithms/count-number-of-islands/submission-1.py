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

        for r in range(rows):
            for c in range(cols):
                # If we find land, we've found a new island
                if grid[r][c] == "1":
                    numIslands += 1
                    
                    # Start BFS to "sink" this entire island
                    # Use a tuple for the start node as requested
                    queue = deque([(r, c)])
                    grid[r][c] = "0" # Mark as visited by sinking it

                    while queue:
                        curr_r, curr_c = queue.popleft()
                        
                        for d in directions:
                            nr, nc = curr_r + d[0], curr_c + d[1]
                            
                            # Boundary check + check if it's land
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                queue.append((nr, nc)) 
                            
        return numIslands