'''
Docstring for word-search.ZetBe
문제: 2D 보드에서 단어를 찾으시오.
풀이: 깊이 우선 탐색(DFS)을 사용하여 보드의 각 셀에서 시작하여 단어를 찾습니다. 방문한 셀은 다시 방문하지 않도록 표시합니다.
시간 복잡도: O(m * n * 3^k), m과 n은 보드의 행과 열의 수, k는 단어의 길이입니다. 각 셀에서 시작하여 최대 3가지 방향으로 탐색할 수 있으므로 전체 시간 복잡도는 O(m * n * 3^k)입니다.
공간 복잡도: O(k), k는 단어의 길이입니다. 재귀 호출 스택이 최대 k 깊이까지 쌓일 수 있으므로 공간 복잡도는 O(k)입니다.
사용한 자료구조: 함수(재귀 호출 스택), 2D 리스트(방문 표시)
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        answ = False
        dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
        def dfs(x, y, i, v):
            nonlocal answ
            if i == len(word):
                answ = True
                return True
            if board[y][x] != word[i-1]:
                return False
            for j in range(4):
                ny, nx = y+dy[j], x+dx[j]
                if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and v[ny][nx] == 0 and board[ny][nx] == word[i]:
                    v[ny][nx] = 1
                    dfs(nx, ny, i+1, v)
                    v[ny][nx] = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                v = [[0 for i in range(len(board[0]))] for j in range(len(board))]
                if board[i][j] == word[0]:
                    v[i][j] = 1
                    dfs(j, i, 1, v)
                
        return answ


