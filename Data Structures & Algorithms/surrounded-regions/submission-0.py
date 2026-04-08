class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return []

        rows, cols = len(board), len(board[0])
        directions = [[0,1], [0, -1], [1,0], [-1,0]] 

        borderOs = []
        queue = deque(borderOs)

        # 1. Find border 'O's and mark them as survivors
        for r in range(rows):
            for c in [0, cols - 1]: # Just the first and last columns
                if board[r][c] == "O":
                    board[r][c] = "S"
                    queue.append((r, c))
        
        for c in range(cols):
            for r in [0, rows - 1]: # Just the first and last rows
                if board[r][c] == "O":
                    board[r][c] = "S"
                    queue.append((r, c))


        while queue:
            curr_r, curr_c = queue.popleft()

            for dr, dc in directions:
                nr = dr + curr_r
                nc = dc + curr_c

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "S"
                    queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"



        