class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def dfs(x, y, index):
            if index == len(word):
                return True

            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[index]:
                return False

            temp = board[x][y]
            board[x][y] = '#'

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if dfs(nx, ny, index + 1):
                    return True

            board[x][y] = temp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False

"""
================================================================================
풀이 과정
================================================================================

[1차 시도] DFS + 방향 배열로 접근
────────────────────────────────────────────────────────────────────────────────
1. 격자에서 상하좌우로 이동하며 단어를 찾아야 함
2. 같은 셀은 한 번만 사용 가능 → 방문 체크 필요
3. DFS(깊이 우선 탐색) + 백트래킹으로 풀면 될 것 같음
4. 상하좌우 이동을 위한 dx, dy 배열 만들자

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]


[2차 시도] DFS 함수 구조 설계
────────────────────────────────────────────────────────────────────────────────
5. dfs(x, y, index) 형태로 현재 위치와 단어의 인덱스를 추적
6. base case:
   - index == len(word): 단어 끝까지 찾음 → True
   - 범위 벗어남 or 문자 불일치 → False

        def dfs(x, y, index):
            if index == len(word):
                return True

            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[index]:
                return False

7. 방문한 셀은 어떻게 표시하지?


[3차 시도] 방문 표시와 백트래킹
────────────────────────────────────────────────────────────────────────────────
8. 현재 셀을 '#' 같은 특수 문자로 임시 변경 (방문 표시)
9. 4방향으로 재귀 탐색
10. 탐색 실패 시 원래 값으로 복원 (백트래킹)

        temp = board[x][y]
        board[x][y] = '#'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if dfs(nx, ny, index + 1):
                return True

        board[x][y] = temp
        return False


[4차 시도] 조기 종료 최적화 추가
────────────────────────────────────────────────────────────────────────────────
11. 빈 보드는 바로 False 반환
12. 첫 글자가 일치하는 셀에서만 DFS 시작 (불필요한 탐색 방지)

        if not board or not board[0]:
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True


[최종 구현] 최적화된 DFS 탐색
────────────────────────────────────────────────────────────────────────────────
13. 조기 종료로 불필요한 탐색 제거
14. 백트래킹으로 방문 상태 관리
15. 하나라도 성공하면 즉시 True 반환

16. 시간복잡도: O(m * n * 4^L) - 최악의 경우, 조기 종료로 실제로는 더 빠름
17. 공간복잡도: O(L) - 재귀 깊이
"""
