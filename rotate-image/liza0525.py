class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_matrix = len(matrix)

        
        for i in range(len_matrix // 2):
            for j in range(i, len_matrix - i - 1):
                (
                    matrix[i][j],
                    matrix[j][len_matrix - i - 1],
                    matrix[len_matrix - i - 1][len_matrix - j - 1],
                    matrix[len_matrix - j - 1][i],
                ) = (
                    matrix[len_matrix - j - 1][i],
                    matrix[i][j],
                    matrix[j][len_matrix - i - 1],
                    matrix[len_matrix - i - 1][len_matrix - j - 1],
                )
