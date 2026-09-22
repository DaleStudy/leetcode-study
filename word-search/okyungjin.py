# https://leetcode.com/problems/word-search/

# board: 영문 대/소문자 배열, m * n
# board의 상하좌우로 인접한 문자열을 이어붙여서 word를 완성할 수 있는지 여부를 반환한다.
# 단, 셀은 한번만 사용 가능하다

# [접근법]
# dfs로 문자열을 상,하,좌,우로 탐색한다.

# [복잡도]
# L: word 의 길이
# 시간 복잡도: O(m * n * 3^L), 이전 문자에서 이동한 방향은 제외하므로 3^L
# 공간 복잡도: O(L)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_size = len(board)
        col_size = len(board[0])

        # board에 word를 만들 수 있는 문자열이 충분히 있는지 확인
        for char in set(word):
            # board 전체에서 해당 알파벳이 몇 개인지 카운트한다.
            board_char_count = sum(row.count(char) for row in board)
            if board_char_count < word.count(char):
                return False

        # 빈도수가 더 적은 글자부터 탐색하도록 단어를 뒤집는다
        count_first = sum(row.count(word[0]) for row in board)
        count_last = sum(row.count(word[-1]) for row in board)
        
        if count_first > count_last:
            word = word[::-1]

        VISITED_MARK = '#'
        def dfs(row: int, col: int, str_idx: int) -> bool:
            if str_idx == len(word):
                return True
            
            # 종료조건1: 보드의 좌표를 넘어가는 경우
            if not (0 <= row < row_size and 0 <= col < col_size):
                return False
            
            # 종료조건 2: 이미 방문함 (#: 방문했음을 표시하는 마크)
            # 종료조건 3: 문자열 불일치
            if board[row][col] == VISITED_MARK or board[row][col] != word[str_idx]:
                return False

            # 방문을 표시하는 마크(#)로 임시 교체
            origin_char = board[row][col]
            board[row][col] = VISITED_MARK

            # 좌표를 탐색한다
            found = (
                   dfs(row - 1, col, str_idx + 1) # 상
                or dfs(row + 1, col, str_idx + 1) # 하
                or dfs(row, col - 1, str_idx + 1) # 좌
                or dfs(row, col + 1, str_idx + 1) # 우
            )

            # 원본 문자열로 복원
            board[row][col] = origin_char

            return found


        # 시작점을 찾는다
        for r in range(row_size):
            for c in range(col_size):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
