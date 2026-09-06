class Solution:
    def solve(self, board: List[List[str]]) -> None:

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        queue = deque([])
        # Find survivors
        for c in range(len(board[0])):
            if board[0][c] == "O":
                board[0][c] = "S"
                queue.append((0, c))

        for c in range(len(board[0])):
            if board[len(board) -1][c] == "O":
                board[len(board) - 1][c] = "S"
                queue.append((len(board) -1, c))

        for r in range(len(board)):
            if board[r][0] == "O":
                board[r][0] = "S"
                queue.append((r, 0))

        for r in range(len(board)):
            if board[r][len(board[0]) -1] == "O":
                board[r][len(board[0]) -1] = "S"
                queue.append((r, len(board[0]) -1))

        while queue:
            curr_r, curr_c = queue.popleft()

            for dr, dc in dirs:
                nr = curr_r + dr
                nc = curr_c + dc

                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == "O":
                    board[nr][nc] = "S"
                    queue.append((nr, nc))


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"


        