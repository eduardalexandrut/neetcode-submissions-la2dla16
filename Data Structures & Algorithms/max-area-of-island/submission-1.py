from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]

        visited = set()

        def bfs(rr, cc):
            q = deque([(rr, cc)])
            visited.add((rr, cc))

            count = 1
            while q:
                r, c = q.popleft()
                #visited.add((r,c))
                for dr, dc in directions:
                    nc, nr = dc + c, dr + r
                    if (0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == 1):
                        visited.add((nr, nc))
                        q.append((nr,nc))
                        count +=1
                
            return count
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(bfs(i,j), maxArea)

        return maxArea 


        
        