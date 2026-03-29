class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        n_rows = len(matrix)
        n_cols = len(matrix[0]) # Questa deve restare costante!
        
        l = 0
        r = (n_rows * n_cols) - 1
            
        while l <= r:
            m = (l + r) // 2
            
            # Calcoliamo row e col usando n_cols che è fisso
            curr_row = m // n_cols
            curr_col = m % n_cols
            
            val = matrix[curr_row][curr_col]
            
            if val == target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        return False