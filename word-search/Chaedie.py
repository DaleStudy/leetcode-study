"""
Solution: 
    1) board의 상하좌우를 탐색하되 아래 조건을 base case로 걸러준다.
    1.1) index 가 word의 길이이면 결과값 판단
    1.2) out of bounds 판단
    1.3) index를 통해 현재 글자와 board의 글자의 일치 판단
    1.4) 방문 여부 판단
    2) board를 돌면서 backtrack 이 True 인 케이스가 있으면 return True

m = row_len
n = col_len
L = 단어 길이
Time: O(m n 4^L)
Space: O(mn + L^2) = visit set O(mn) + 호출 스택 및 cur_word O(L^2)
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def backtrack(r, c, index, cur_word):
            if index == len(word):
                return word == cur_word
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return False
            if word[index] != board[r][c]:
                return False
            if (r, c) in visit:
                return False

            visit.add((r, c))
            condition = (
                backtrack(r + 1, c, index + 1, cur_word + board[r][c])
                or backtrack(r - 1, c, index + 1, cur_word + board[r][c])
                or backtrack(r, c + 1, index + 1, cur_word + board[r][c])
                or backtrack(r, c - 1, index + 1, cur_word + board[r][c])
            )
            visit.remove((r, c))
            return condition

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0, ""):
                    return True
        return False


"""
Solution: 
    공간 복잡도 낭비를 줄이기 위해 cur_word 제거
Time: O(m n 4^L)
Space: O(mn + L)
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def backtrack(r, c, index):
            if index == len(word):
                return True
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return False
            if word[index] != board[r][c]:
                return False
            if (r, c) in visit:
                return False

            visit.add((r, c))
            condition = (
                backtrack(r + 1, c, index + 1)
                or backtrack(r - 1, c, index + 1)
                or backtrack(r, c + 1, index + 1)
                or backtrack(r, c - 1, index + 1)
            )
            visit.remove((r, c))
            return condition

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True
        return False


"""
Solution: 
    공간 복잡도를 줄이기 위해 visit set 제거 
    -> board[r][c]에 빈문자열을 잠깐 추가하는것으로 대체
Time: O(m n 4^L)
Space: O(L)
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r, c, index):
            if index == len(word):
                return True
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return False
            if word[index] != board[r][c]:
                return False

            temp = board[r][c]
            board[r][c] = ""
            condition = (
                backtrack(r + 1, c, index + 1)
                or backtrack(r - 1, c, index + 1)
                or backtrack(r, c + 1, index + 1)
                or backtrack(r, c - 1, index + 1)
            )
            board[r][c] = temp
            return condition

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True
        return False
