class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS = len(board)
        COLS = len(board[0])

        directions = [[0,1], [1, 0], [-1, 0], [0, -1]]

        q = deque([])
        for r in range(ROWS):
            for c in range(COLS):

                if (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1) and board[r][c] == "O":
                    board[r][c] = "S"
                    q.append((r, c))

        while q:
            curr_r, curr_c = q.popleft()

            for dr, dc in directions:
                nc = dc + curr_c
                nr = dr + curr_r

                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                    q.append((nr, nc))
                    board[nr][nc] = "S"


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"