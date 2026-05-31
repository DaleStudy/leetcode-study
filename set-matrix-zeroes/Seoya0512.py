'''
Set 자료구조를 사용해서 0이 있는 행과 열을 기록한 후, 해당 행과 열을 0으로 변경

Time Complexity: O(m*n)
- 행렬의 모든 원소를 한 번씩 방문 
Space Complexity: O(m+n)
- 행과 열의 index를 저장하는데 각각 최대 m, n 크기가 필요함

참고: 문제에서 요구한 in-place 변경을 지키지 못함, 행과 열을 저장하는데 추가 공간이 필요하기 때문
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for row in zero_rows:
            for j in range(len(matrix[row])):
                matrix[row][j] = 0
        
        for col in zero_cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
