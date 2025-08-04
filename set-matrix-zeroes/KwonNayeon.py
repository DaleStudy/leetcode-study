"""
Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

<Solution 1>

Time Complexity: O(m * n)
- m은 행, n은 열을 의미함
- 0 찾기: O(m * n)
- 행과 열 변환: O(m * n)

Space Complexity: O(m * n)
- zeros 배열이 최대 m * n 크기까지 저장 가능

풀이 방법:
1. 0 위치를 탐색/저장
2. 저장된 0의 행과 열을 모두 0으로 변환
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
            # 행(row)을 0으로 채움
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
            # 열(column)을 0으로 채움
            for i in range(len(matrix)):
                matrix[i][c] = 0

"""
<Solution 2>

Time Complexity: O(m * n)
- 행렬 순회: O(m * n)
- 행과 열 변환: O(m * n)

Space Complexity: O(m + n)
- zero_rows: O(m)
- zero_cols: O(n)

풀이 방법:
1. set 자료구조를 활용하여 중복 제거
2. 행과 열 정보를 분리 저장하여 메모리를 효율적으로 사용
3. 행과 열을 독립적으로 처리하여 불필요한 반복 연산 제거
"""
class Solution:
   def setZeroes(self, matrix: List[List[int]]) -> None:
       """
       Do not return anything, modify matrix in-place instead.
       """
       zero_rows = set()
       zero_cols = set()
       
       for r in range(len(matrix)):
           for c in range(len(matrix[0])):
               if matrix[r][c] == 0:
                   zero_rows.add(r)
                   zero_cols.add(c)
                   
       for r in zero_rows:
           for i in range(len(matrix[0])):
               matrix[r][i] = 0
               
       for c in zero_cols:
           for i in range(len(matrix)):
               matrix[i][c] = 0

"""
<Solution 3>

Time Complexity: O(m * n)

Space Complexity: O(1)
- 추가적인 메모리를 사용하지 않고 첫 행과 열을 마커로 활용하여 해결
- first_row_zero, first_col_zero 두 변수만 사용

풀이 방법:
1. 첫 행과 첫 열의 0 여부를 변수에 저장 (나중에 처리하기 위함)
2. 첫 행과 첫 열을 마커로 사용: 행렬의 0 위치를 첫 행/열에 표시
3. 표시된 0을 기준으로 나머지 행렬을 변경 (행/열 전체를 0으로 변경)
4. 저장해둔 변수로 첫 행/열 처리 (원래 0이었던 행/열 처리)
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 첫 행/열의 0 여부 저장
        first_row_zero = any(matrix[0][c] == 0 for c in range(len(matrix[0])))
        first_col_zero = any(matrix[r][0] == 0 for r in range(len(matrix)))

        # 0이 있는 위치의 첫 행/열에 표시
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0   # 첫 열에 표시
                    matrix[0][c] = 0   # 첫 행에 표시

        # 표시된 0을 기준으로 나머지 위치 변경
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # 첫 행/열 처리
        if first_row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
                
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
