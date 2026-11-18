class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i, r, c):
            #base case
            if i == len(word):
                return True

            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == word[i]:
                #set current as visited
                temp = board[r][c]
                board[r][c] = "#"

                #check all neighbors
                condition = (dfs(i + 1, r + 1, c) or
                    dfs(i + 1, r -1, c) or
                    dfs(i + 1, r, c + 1) or
                    dfs(i + 1, r, c - 1))
            
                board[r][c] = temp

                return condition
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True
        
        return False