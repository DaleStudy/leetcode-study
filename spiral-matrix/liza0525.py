# 7기 풀이
# 풀이 1
# 시간 복잡도: O(n * m)
# - matrix의 가로, 세로 길이의 곱에 비례하여 시간복잡도가 계산됨(모든 칸을 다 돌기 때문)
# 공간 복잡도: O(n * m)
# - matrix를 방문할 때마다 visited를 업데이트 해주고 있어, n * m의 길이 만큼 늘어남
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        len_i = len(matrix)
        len_j = len(matrix[0])
        visited = set()  # 확인한 인덱스의 경우에는 tuple의 형태로 넣어주려고 함

        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 시계 방향을 나타내는 tuple(오른쪽, 아래쪽, 왼쪽, 위쪽 순서)

        curr_dir_idx = 0  # 현재 방향을 나타내는 dirs의 index(0이면 오른쪽을 의미)
        curr_i, curr_j = 0, 0  # 처음 시작점인 (0, 0) 인덱스를 지정 

        result = []

        while len(visited) < len_i * len_j:  # 모든 인덱스에 방문할 때까지 루프 돌기
            result.append(matrix[curr_i][curr_j])  # result에 값을 먼저 넣어주고
            visited.add((curr_i, curr_j))  # visited에 방문했다는 것을 표시

            dir_i, dir_j = dirs[curr_dir_idx]  # 현재의 진행 방향 가져오기

            if (
                (curr_i + dir_i, curr_j + dir_j) in visited  # 다음 방문할 곳이 이미 방문했던 했거나
                or not (0 <= curr_i + dir_i < len_i)  # i 인덱스 범위를 벗어나거나
                or not (0 <= curr_j + dir_j < len_j)  # j 인덱스 범위를 벗어나면
            ):
                curr_dir_idx = (curr_dir_idx + 1) % 4  # 방향 index를 하나 올려서
                dir_i, dir_j = dirs[curr_dir_idx]  # 방향을 바꿔준다.

            # curr_i, curr_j를 업데이트 하여 다음 루프에서 탐방하게 한다.
            curr_i, curr_j = curr_i + dir_i, curr_j + dir_j

        return result


# 풀이 2
# 시간 복잡도: O(n * m)
# - matrix의 가로, 세로 길이의 곱에 비례하여 시간복잡도가 계산됨(모든 칸을 다 돌기 때문)
# 공간 복잡도: O(1)
# - 변수 몇 개만 사용했음(풀이 1과의 가장 큰 차이)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 각각에 대한 경계를 지정하여 계산하는 방법이다.
        # 위, 아래, 왼쪽, 오른쪽에 대한 최초 경계 설정
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        # 처음 방향 설정(오른쪽으로 가기)
        dir_i, dir_j = 0, 1

        # 처음 방문 인덱스 설정
        curr_i, curr_j = 0, 0

        result = []

        # top은 bottom보다 커지면 안되고
        # left는 right보다 커지면 안된다.
        # 이에 따라 top <= bottom and left <= right 조건으로 루프 돌기
        while top <= bottom and left <= right:
            result.append(matrix[curr_i][curr_j])  # 해당 인덱스에 있는 값을 result에 넣기

            if curr_i + dir_i < top:  # 1. 다음 인덱스가 top 경계를 넘어가려고 할 때
                dir_i, dir_j = 0, 1  # 방향을 오른쪽으로 변경해주고
                left += 1  # 지나온 인덱스들이 새로운 왼쪽 경계가 되므로, left을 하나 올려준다.
            elif curr_i + dir_i > bottom:  # 2. 다음 인덱스가 bottom의 경계를 넘어가려고 할 때
                dir_i, dir_j = 0, -1  # 방향을 왼쪽으로 변경해주고
                right -= 1  # 지나온 인덱스들이 새로운 오른쪽 경계가 되므로, right를 하나 내려준다.
            elif curr_j + dir_j < left:  # 3. 다음 인덱스가 left 경계를 넘어가려고 할 때
                dir_i, dir_j = -1, 0  # 방향을 위쪽으로 변경해주고
                bottom -= 1  # 지나온 인덱스들이 새로운 아랫쪽 경계가 되므로, bottom을 하나 내려준다.
            elif curr_j + dir_j > right:  # 4. 다음 인덱스가 right 경계를 넘어가려고 할 떄
                dir_i, dir_j = 1, 0  # 방향을 아랫쪽으로 변경해주고
                top += 1  # 지나온 인덱스들이 새로운 윗쪽 경계가 되므로, top을 하나 올려준다.

            # curr_i, curr_j를 업데이트 하여 다음 루프에서 탐방하게 한다.
            curr_i, curr_j = curr_i + dir_i, curr_j + dir_j

        return result
