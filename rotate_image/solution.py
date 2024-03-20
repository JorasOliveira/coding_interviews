class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # size = len(matrix)
        # for i in range(size):
        #     matrix[i] = matrix[(size - 1)- i]
        n = len(matrix)
        # transpose
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c] 
        
        # flip horizontally
        for r in range(n):
            for c in range(n//2):
                matrix[r][c], matrix[r][n-1-c] = matrix[r][n-1-c], matrix[r][c]

