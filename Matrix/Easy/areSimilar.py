class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        m = len(mat[0])
        for row in mat:
            for j in range(m):
                if row[(j + k) % m] != row[j]:
                    return False

        return True
