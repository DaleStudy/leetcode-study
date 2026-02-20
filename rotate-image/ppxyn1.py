# idea: -
# Time Complexity: O(n^2)

'''
1 2 3
4 5 6
7 8 9
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose (diagonal elements are fixed)
        '''
        1 4 7
        2 5 8
        3 6 9
        '''
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j] 
        
        # Reverse each row
        '''
        7 4 1
        8 5 2
        9 6 3
        '''
        for r in matrix:
            r.reverse()
