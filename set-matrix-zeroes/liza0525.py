# 7기 풀이
# 시간 복잡도: O(m * n)
# - matrix 크기 만큼 시간 복잡도가 듦
# 공간 복잡도: O(m + n)
# - 가로, 세로에서 각각 대상 인덱스를 저장
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_i = len(matrix)
        len_j = len(matrix[0])

        # 0이 발견된 행/열 인덱스를 각각 저장하는 set
        target_i_set, target_j_set = set(), set()

        for i in range(len_i):
            for j in range(len_j):
                if matrix[i][j] != 0:
                    continue

                # matrix[i][j]가 0인 경우에는 인덱스를 저장한다.
                target_i_set.add(i)
                target_j_set.add(j)

                
        for i in range(len_i):
            for j in range(len_j):
                if matrix[i][j] == 0:
                    continue
                if i in target_i_set or j in target_j_set:
                    # i, j 인덱스가 set에 있는 경우에는 0으로 변경한다.
                    matrix[i][j] = 0
