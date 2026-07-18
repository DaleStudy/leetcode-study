# board: 영문 대/소문자 배열, m * n
# board의 상하좌우로 인접한 문자열을 이어붙여서 word를 완성할 수 있는지 여부를 반환한다.
# 단, 셀은 한번만 사용 가능하다

# dfs를 통해 백트랙킹으로 정답을 찾도록 구현했다.
# TODO: 시간/공간 복잡도 계산
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_size = len(board)
        col_size = len(board[0])

        # 방문 여부를 기록하는 2차원 배열
        visited = [[False] * col_size for _ in range(row_size)]

        def dfs(row, col, str_idx) -> bool:
            # 종료조건1: 보드의 좌표를 넘어가는 경우
            if row < 0 or row >= row_size or col < 0 or col >= col_size:
                return False
            
            # 종료조건2: 이미 방문한 경우
            if visited[row][col]:
                return False

            # 종료조건3: 문자열 불일치
            if board[row][col] != word[str_idx]:
                return False

            # 정답 발견 시 종료
            if str_idx + 1 == len(word):
                return True

            visited[row][col] = True

            # 차례대로 상, 하, 좌, 우의 좌표를 탐색
            found = dfs(row - 1, col, str_idx + 1) or \
                    dfs(row + 1, col, str_idx + 1) or \
                    dfs(row, col - 1, str_idx + 1) or \
                    dfs(row, col + 1, str_idx + 1)

            visited[row][col] = False # 백트래킹

            return found


        # 시작점을 찾는다
        for r in range(row_size):
            for c in range(col_size):
                # board[r][c] == word[0] 인 시작점만 호출하도록 해서 최적화
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
