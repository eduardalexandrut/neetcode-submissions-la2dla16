class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mCell = collections.defaultdict(list)
        mCol = collections.defaultdict(list)
        mRow = collections.defaultdict(list)

        for i,row in enumerate(board):
            for j,col in enumerate(row):
                currNum = board[i][j] 
                if currNum == ".":
                    continue

                if currNum in mCol[j]:
                    return False
                mCol[j].append(currNum)

                if currNum in mRow[i]:
                    return False
                mRow[i].append(currNum)

                if currNum in mCell[(i // 3, j // 3)]:
                    return False
                mCell[(i // 3, j // 3)].append(currNum)

        return True