class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return []

        rows, cols = len(board), len(board[0])
        directions = [[0,1], [0, -1], [1,0], [-1,0]] 
        queue = deque()

        # Discover survivors at the first and last columns
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == "O":
                    queue.append((r,c))
                    board[r][c] = "S"

        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == "O":
                    queue.append((r,c))
                    board[r][c] = "S"

        while queue:
            curr_r, curr_c = queue.popleft()
            for dr, dc in directions:
                nr = dr + curr_r
                nc = dc + curr_c

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    queue.append((nr,nc))
                    board[nr][nc] = "S"


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"



        