class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        queue = deque()

        # Add all the treasures to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        print(len(queue))
        while queue:
            curr_r, curr_c = queue.popleft()

            for dr, dc in directions:
                nr = curr_r + dr
                nc = curr_c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[curr_r][curr_c] + 1
                    queue.append((nr, nc))

