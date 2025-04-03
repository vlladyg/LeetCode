class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        left = matrix[0][0]
        right = matrix[n - 1][n - 1]



        def less_k(mid):
            counter = 0
            for row in range(n):
                x = bisect_right(matrix[row], mid)
                counter += x
            return counter

        while left < right:
            mid = (left + right) // 2
            if less_k(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left
