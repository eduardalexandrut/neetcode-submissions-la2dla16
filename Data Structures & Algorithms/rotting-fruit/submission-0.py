from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        count = 0
        q = deque()

        for i in range(rows):
            for  j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

  
            
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < rows and 0<= nc < cols and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            count+=1
        
        
        return count if fresh == 0 else -1
                    
        


        