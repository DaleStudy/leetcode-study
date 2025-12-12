# 시간 복잡도: O(m · n · 4^k)
# - 보드의 모든 칸(m·n)을 시작점으로 고려하고
# - 각 칸에서 단어 길이 k만큼 DFS 탐색을 수행한다.
# - 각 단계마다 최대 4방향으로 뻗을 수 있기 때문에 지수적 탐색 구조를 가진다.
#   (다만 visits로 중복 방문을 막아 실제 탐색량은 줄어든다.)

# 공간 복잡도: O(m · n)
# - 방문 여부를 저장하는 2차원 배열 때문에 m·n의 공간이 필요하다.
# - DFS 재귀 깊이는 최대 단어 길이 k까지 깊어질 수 있어 O(k) 스택을 추가로 사용하지만,
#   전체 공간에서 보면 visits가 차지하는 비중이 더 크다.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 보드의 행(row)과 열(column) 개수를 가져온다.
        m = len(board)
        n = len(board[0])

        # 전체 칸 수보다 단어 길이가 길다면 애초에 만들 수 없으니 바로 False
        if len(word) > m * n:
            return False

        # 방문 여부를 기록할 2차원 배열 생성
        # - 같은 칸은 다시 사용하지 못하므로 DFS에서 체크해야 한다.
        visits = [[False for _ in range(n)] for _ in range(m)]

        # DFS 함수: (i, j)에서 word[str_index] 문자를 만족시키는지 재귀적으로 탐색한다.
        def dfs(i, j, str_index):
            # 범위 벗어나는지, 이미 방문한 칸인지, 현재 문자가 일치하는지 확인
            if not (
                0 <= i < m
                and 0 <= j < n
                and str_index < len(word)
                and not visits[i][j]
                and board[i][j] == word[str_index]
            ):
                return

            # 현재 문자가 마지막 문자라면 단어를 모두 찾은 것
            if str_index == len(word) - 1:
                return True

            # 현재 칸 방문 처리
            visits[i][j] = True

            # 상하좌우 네 방향으로 다음 문자를 찾으러 이동
            # - 하나라도 성공하면 그대로 True를 반환
            if (
                dfs(i + 1, j, str_index + 1)
                or dfs(i - 1, j, str_index + 1)
                or dfs(i, j + 1, str_index + 1)
                or dfs(i, j - 1, str_index + 1)
            ):
                return True

            # 모든 방향 실패 시 백트래킹: 방문 기록을 원복해줘야 다른 경로에서 다시 사용할 수 있다.
            visits[i][j] = False
            return False

        # 모든 칸을 단어의 시작점으로 삼아 DFS 시도
        for start_i in range(m):
            for start_j in range(n):
                if dfs(start_i, start_j, 0):
                    return True

        # 모든 시도를 해도 못 찾으면 False
        return False
