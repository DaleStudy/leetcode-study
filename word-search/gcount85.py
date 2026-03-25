"""
# Intuition
백트래킹으로 풀었습니다.

# Complexity
- Time complexity: O(M*N*3^L) => M*N 보드 한 칸을 모두 방문하며,
word 의 길이(L) 횟수 단계 만큼 탐색해야 한다. 매 단계 탐색할 때는 매번 3갈래씩 길을 찾는다.

- Space complexity: 재귀 스택 O(L), visited 크기 O(L)
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board[0]), len(board)
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y, cur_step, visited):
            if cur_step == len(word) - 1:
                return True

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if board[nx][ny] != word[cur_step + 1]:
                    continue
                if (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                if dfs(nx, ny, cur_step + 1, visited):
                    return True
                visited.discard((nx, ny))
            return False

        for x, row in enumerate(board):
            for y, start_word in enumerate(row):
                if word[0] != start_word:
                    continue
                if dfs(x, y, 0, {(x, y)}):
                    return True
        return False
