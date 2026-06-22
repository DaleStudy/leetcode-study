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


# 7기 풀이
# 시간 복잡도: O((n * m) * 4 ^ d)
#  - depth의 길이(d)만큼 네 방향을 탐색하며, 출발점의 개수 n * m 모두 탐색할 때 최악의 시간
# 공간 복잡도: O(n * m)
#  - visited 변수를 사용하기 때문에 행 * 열의 개수만큼의 공간을 필요로 함
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 보드의 행, 열의 길이를 미리 저장
        num_rows = len(board)
        num_cols = len(board[0])

        # dfs 탐색 시 이미 방문한 경우를 체크하기 위한 visited를 생성
        visited = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        # dfs 탐색 시 한 칸을 기준으로 하여 4방향으로 탐색 가능하게 directions을 만든다.
        # 순서대로 아래로 진출, 위로 진출, 왼쪽으로 진출, 오른쪽으로 진출
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def check_exist_word(i, j, depth):
            if depth == len(word) - 1:
                # depth가 word의 길이에 가까워지면(배열이라 -1 해줌)
                # 탐색을 마쳤으므로 True를 반환
                return True

            # 현재의 칸은 방문했다는 의미로 1로 변경
            visited[i][j] = 1
            for dir_i, dir_j in directions:
                # 네 방향을 순차로 탐색한다.
                # 다음 칸의 위치를 나타내는 next_i와 next_j를 먼저 계산
                next_i, next_j = i + dir_i, j + dir_j
                if not (
                    0 <= next_i < num_rows  # 다음 칸의 행 번호가 행의 길이 내에 있고
                    and 0 <= next_j < num_cols  # 다음 칸의 열 번호가 열의 길이 내에 있고
                    and not visited[next_i][next_j]  # 아직 방문하지 않았으며
                    and board[next_i][next_j] == word[depth + 1]  # 다음 글자가 word의 다음 글자에 해당해야 함
                ):
                    # 그렇지 않은 경우에는 탐색할 필요가 없으므로 다음 방향을 찾는다
                    continue
                
                # 위의 조건을 모두 만족하면 탐색해도 된다.
                exist_word = check_exist_word(
                    next_i,
                    next_j,
                    depth + 1  # word의 다음 index를 찾아야 함
                )
                if exist_word:
                    # 단어를 찾았다고 하면 early return
                    return True
                
            # 백트래킹을 위해 현재 칸의 visited 값을 원복한다.
            visited[i][j] = 0

            # 단어를 찾지 못했을 땐 False 반환
            return False

        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] != word[0]:
                    # 출발 글자가 word의 첫 글자랑 같지 않으면 탐색할 필요가 없으므로 넘긴다.
                    continue

                exist_word = check_exist_word(i, j, 0)
                if exist_word:
                    # 단어를 찾았으면 탐색을 더이상 하지 않아도 되므로 early return
                    return True

        # 보드의 모든 탐색을 해도 찾지 못한 경우에는 False 반환
        return False
