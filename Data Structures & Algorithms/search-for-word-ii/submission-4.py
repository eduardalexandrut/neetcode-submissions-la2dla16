class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = dict()
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = dict()
                curr = curr[c]
            curr["word"] = word


        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(r, c,  parentNode):
            char = board[r][c]
            currNode = parentNode[char]

            if "word" in currNode:
                res.append(currNode["word"])
                del currNode["word"]

            board[r][c] = "#"

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc  < cols and board[nr][nc] in currNode:
                    dfs(nr, nc, currNode)

            board[r][c] = char

            if not currNode:
                del parentNode[char]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r,c, trie)
        
        return res