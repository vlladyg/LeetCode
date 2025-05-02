class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        new_mat = defaultdict(list)
        
        for row in range(n):
            for col in range(m):
                heappush(new_mat[row - col], mat[row][col])
                
        
        for row in range(n):
            for col in range(m):
                mat[row][col] = heappop(new_mat[row - col])

        
        return mat

