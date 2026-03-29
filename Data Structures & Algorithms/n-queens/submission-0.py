class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol = []
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            if row == n:
                sol.append(["".join(r) for r in board])
                return

            for col in range(n):
                if self.isSafe(row, col, board):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
        
        backtrack(0)
        return sol

    def isSafe(self, r: int, c: int, board):
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True

