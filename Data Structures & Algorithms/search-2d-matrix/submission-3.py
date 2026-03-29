class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: 
            return False

        n_rows = len(matrix)
        n_cols = len(matrix[0]) 
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = l + (r - l) //2
            row = mid // n_cols
            col = mid % n_cols

            if matrix[row][col] == target:
                return True

            if matrix[row][col] < target:
                l = mid + 1
            if matrix[row][col] > target:
                r = mid - 1

        return False