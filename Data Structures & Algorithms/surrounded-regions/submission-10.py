class Solution:
    def solve(self, board: List[List[str]]) -> None:

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        rows = len(board)
        cols = len(board[0])
        queue = deque([])

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == "O":
                    board[r][c] = "S"
                    queue.append((r, c))


        while queue:
            curr_r, curr_c = queue.popleft()
            
            for dr, dc in dirs:
                nr = curr_r + dr
                nc = curr_c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "S"
                    queue.append((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        