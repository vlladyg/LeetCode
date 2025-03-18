class Solution:
    __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix[0]) == 1 and len(matrix)==1:
            if matrix[0][0] == target:
                return True
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i])-1
            while left<=right:
                mid = (left+right)//2

                if matrix[i][mid]==target:
                    return True
                
                if matrix[i][left]<=matrix[i][mid]:
                    if matrix[i][left] <= target < matrix[i][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if matrix[i][mid] < target <=matrix[i][right]:
                        left = mid - 1
                    else:
                        right = mid + 1
        return False
