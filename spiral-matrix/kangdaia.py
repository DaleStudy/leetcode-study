class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        주어진 2D 행렬을 나선형으로 순회하여 요소들을 반환하는 함수

        방법:
        1. transpose 행렬을 만들어 열을 쉽게 접근할 수 있도록 함
        2. while 루프를 사용하여 나선형으로 순회
        3. 각 단계에서 top row, right column, bottom row, left column을 순서대로 추가
        4. 각 단계가 끝날 때마다 row와 col을 증가시켜 다음 레이어로 이동

        시간복잡도 O(m*n), 공간복잡도 O(m*n)

        Args:
            matrix (list[list[int]]): 2D 행렬

        Returns:
            list[int]: 나선형으로 순회한 요소들의 리스트
        """
        row, col = 0, 0
        m, n = len(matrix), len(matrix[0])
        t_matrix = list(zip(*matrix))
        spiral = []
        while row < m and col < n:
            top, left = row, col
            bottom, right = m - row - 1, n - col - 1
            if top > bottom or left > right:
                break
            # first row: left -> right
            first_row = matrix[top][left : right + 1]
            spiral += first_row
            # last col: top+1 -> bottom
            last_col = list(t_matrix[right][top + 1 : bottom + 1])
            spiral += last_col
            # last row: right-1 -> left (역순)
            if top < bottom:
                last_row = matrix[bottom][left:right][::-1]
                spiral += last_row
            # first col: bottom-1 -> top+1 (역순)
            if left < right:
                first_col = list(t_matrix[left][top + 1 : bottom][::-1])
                spiral += first_col
            # add
            row += 1
            col += 1
        return spiral
