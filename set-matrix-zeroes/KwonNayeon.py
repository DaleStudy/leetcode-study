"""
Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

Time Complexity: O(m*n)
- m은 행, n은 열을 의미
- 0 찾기 - O(m*n)
- 행과 열 변환 - O(m*n)

Space Complexity: O(m*n)
- zeros 배열이 최대 m*n 크기까지 저장 가능

풀이 방법:
1. 0 위치 저장
2. 저장된 0의 행과 열을 모두 0으로 변환
3. 주의점 - 행렬 값 탐색과 변경을 동시에 수행하면 원래 어떤 값이 0이었는지 구분하기 어려워짐
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeros.append((r, c))
        
        for r, c in zeros:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
            for i in range(len(matrix)):
                matrix[i][c] = 0
