class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        [0][0] [0][1] [0][2]
        [1][0] [1][1] [1][2]
        [2][0] [2][1] [2][2]

        [2][0] [1][0] [0][0]
        [2][1] [1][1] [0][1]
        [2][2] [1][2] [0][2]
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()
