# board: 영문 대/소문자 배열, m * n
# board의 상하좌우로 인접한 문자열을 이어붙여서 word를 완성할 수 있는지 여부를 반환한다.
# 단, 셀은 한번만 사용 가능하다

# dfs를 통해 백트랙킹으로 정답을 찾도록 구현했다.

# L: word 의 길이
# 시간 복잡도: O(m * n * 4^L)
# 공간 복잡도: O(m * n + L)
class SolutionA:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_size = len(board)
        col_size = len(board[0])

        # 방문 여부를 기록하는 2차원 배열
        visited = [[False] * col_size for _ in range(row_size)]

        def dfs(row, col, str_idx) -> bool:
            if str_idx == len(word):
                return True
            
            # 종료조건1: 보드의 좌표를 넘어가는 경우
            if row < 0 or row >= row_size or col < 0 or col >= col_size:
                return False
            
            # 종료조건 2: 이미 방문함
            # 종료조건 3: 문자열 불일치
            if visited[row][col] or board[row][col] != word[str_idx]:
                return False
            
        
            visited[row][col] = True

            # 차례대로 상, 하, 좌, 우의 좌표를 탐색
            found = (dfs(row - 1, col, str_idx + 1) or \
                    dfs(row + 1, col, str_idx + 1) or \
                    dfs(row, col - 1, str_idx + 1) or \
                    dfs(row, col + 1, str_idx + 1))

            visited[row][col] = False # 백트래킹

            return found


        # 시작점을 찾는다
        for r in range(row_size):
            for c in range(col_size):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False

# SolutionA 의 공간복잡도 최적화 버전, visited 제거
# L: word 의 길이
# 시간 복잡도: O(m * n * 4^L)
# 공간 복잡도: O(L)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        VISITED_MARK = '#'

        row_size = len(board)
        col_size = len(board[0])

        def dfs(row, col, str_idx) -> bool:
            if str_idx == len(word):
                return True
            
            # 종료조건1: 보드의 좌표를 넘어가는 경우
            if row < 0 or row >= row_size or col < 0 or col >= col_size:
                return False
            
            # 종료조건 2: 이미 방문함
            # 종료조건 3: 문자열 불일치
            if board[row][col] == VISITED_MARK or board[row][col] != word[str_idx]:
                return False
            

            # VISITED_MARK로 교체하여 방문을 기록
            origin_char = board[row][col]
            board[row][col] = VISITED_MARK

            # 차례대로 상, 하, 좌, 우의 좌표를 탐색
            found = (dfs(row - 1, col, str_idx + 1) or \
                    dfs(row + 1, col, str_idx + 1) or \
                    dfs(row, col - 1, str_idx + 1) or \
                    dfs(row, col + 1, str_idx + 1))

            # 원본 문자열로 복원
            board[row][col] = origin_char

            return found


        # 시작점을 찾는다
        for r in range(row_size):
            for c in range(col_size):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
