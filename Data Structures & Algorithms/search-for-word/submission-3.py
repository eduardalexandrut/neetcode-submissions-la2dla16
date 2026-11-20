class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i):

            if i == len(word):
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or word[i] != board[r][c]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            find = (
                dfs(r + 1, c,  i + 1) or
                dfs(r - 1, c,  i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))

            board[r][c] = temp
            
            return find


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False