"""search시: TC: O(m*n), SC: O(1)

아이디어:
2차원 배열에서 아직 훑고 가지 않은 영역을 →, ↓, ←, ↑ 방향으로 훑는다. 이때, 한 번에 훑고 갈 선의
시작과 끝 역할을 할 값들(즉, boundary 값들)을 잘 관리해준다.
- top, bottom, left, right의 역할을 할 값을 각각 0, m, 0, n으로 초기화.
- → 방향으로 훑고 나서 top을 한 칸 아래로(즉, top++).
- ↓ 방향으로 훑고 나서 right를 한 칸 왼쪽으로(즉, right--).
- ← 방향으로 훑고 나서 bottom을 한 칸 위로(즉, bottom--).
- ↑ 방향으로 훑고 나서 left를 한 칸 오른쪽으로(즉, left++).
- right가 left보다 왼쪽에 있거나 top이 bottom보다 아래 있으면 탐색 종료.

SC:
- boundary 값만 관리. O(1).

TC:
- 배열의 모든 아이템에 정확히 한 번씩 접근. O(m*n).
- 선을 한 번 긋는 과정에서 일어나는 일이 총 O(1)인데(코드 참조), 이게 아무리 많아도 O(m*n)을 넘지는
  못한다. 한 선에 최소 하나의 값은 들어있기 때문.
- 종합하면 O(m*n).

"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def read_line(start: tuple[int, int], end: tuple[int, int]) -> list[int]:
            if start[0] == end[0]:
                # column 방향
                s, e = sorted([start[1], end[1]])  # TC: O(1)
                line = range(s, e + 1)
                if start[1] > end[1]:  # TC: O(1)
                    line = reversed(line)
                return [matrix[i][start[0]] for i in line]
            else:
                # row 방향
                s, e = sorted([start[0], end[0]])  # TC: O(1)
                line = range(s, e + 1)
                if start[0] > end[0]:  # TC: O(1)
                    line = reversed(line)
                return [matrix[start[1]][i] for i in line]

        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        sol = []
        while True:
            # 위
            if right < left:
                break
            line = read_line((left, top), (right, top))
            sol += line
            top += 1  # TC: O(1)

            # 오른쪽
            if top > bottom:
                break
            line = read_line((right, top), (right, bottom))
            sol += line
            right -= 1  # TC: O(1)

            # 아래
            if right < left:
                break
            line = read_line((right, bottom), (left, bottom))
            sol += line
            bottom -= 1  # TC: O(1)

            # 왼쪽
            if top > bottom:
                break
            line = read_line((left, bottom), (left, top))
            sol += line
            left += 1  # TC: O(1)

        return sol
