class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = m*n - 1
        while left <= right:
            mid = (right + left) // 2
            if matrix[mid // m][mid % m] == target:
                return True
            if target < matrix[mid // m][mid % m]:
                right = mid - 1
            else:
                left = mid + 1

        return False
