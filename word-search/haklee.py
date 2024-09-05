"""TC: O(m * n * (4^l)), SC: O(m * n)

아이디어:
- 격자판의 각 칸을 노드로, 이웃한 칸들의 관계를 엣지로 생각하면 격자판을 그래프로 볼 수 있다.
- 위 그래프에서 dfs를 돌린다.
- 이때, 기존에 방문했던 노드를 재방문하지 않도록 visited라는 2차원 배열을 같이 관리해주자.

SC:
- visited 배열에서 O(m * n)
- 호출 스택은 찾고자 하는 단어의 길이 l, 즉, O(l).
    - 그런데 l이 격자 전체 칸 개수보다 클 수 없으므로 무시 가능.
- 총 O(m * n).

TC:
- visited 배열 세팅, O(m * n)
- dfs, 최악의 경우
    - 단어를 찾는 시도를 하는 데에 4^l 만큼의 탐색이 걸림
    - 그런데 답을 찾을 수 있는 시작 칸을 하필 제일 마지막으로 탐색한 경우 위의 시도를 m*n번 해야함
    - 즉, O(m * n * (4^l))
- 총 O(m * n * (4^l))
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        visited = [[False for _ in range(c)] for _ in range(r)]

        def search(ind: int, pos: tuple[int, int]) -> bool:
            if ind == len(word):
                # 찾는 데에 성공.
                return True

            if not (0 <= pos[0] < r and 0 <= pos[1] < c):
                # 격자판을 벗어남.
                return False

            if visited[pos[0]][pos[1]]:
                # 이미 방문함.
                return False

            if word[ind] != board[pos[0]][pos[1]]:
                # 글자가 안 맞음.
                return False

            visited[pos[0]][pos[1]] = True  # 방문한 것으로 체크

            found = (
                search(ind + 1, (pos[0] - 1, pos[1]))  # 상
                or search(ind + 1, (pos[0] + 1, pos[1]))  # 하
                or search(ind + 1, (pos[0], pos[1] - 1))  # 좌
                or search(ind + 1, (pos[0], pos[1] + 1))  # 우
            )  # 다음 글자 찾기

            # 앞에서 못 찾았을 경우에는 방문을 해제해야 한다.
            # 찾은 경우에는 방문을 해제하든 말든 상관 없음.
            visited[pos[0]][pos[1]] = False

            return found

        return any(search(0, (i, j)) for i in range(r) for j in range(c))
