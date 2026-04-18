"""
# Approach
Grid의 원소에 일일이 dfs를 수행하되 값이 "1"(=육지)인 경우만 탐색을 수행합니다.
이때 방문한 노드는 값을 "-1"로 변경하여 방문 체크합니다.

# Complexity
Grid의 rows = M, cols = N이라고 할 때,
- Time complexity: O(M*N)
- Space complexity: visited set 최대 O(M*N)
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row = len(grid)
        col = len(grid[0])

        def can_go(x, y, row, col):
            if x < 0 or y < 0 or x >= row or y >= col:
                return False
            if grid[x][y] == "0":
                return False
            return True

        def dfs(x, y, row, col):
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if not can_go(nx, ny, row, col):
                    continue
                if grid[nx][ny] == "-1":  # 방문 확인
                    continue
                grid[nx][ny] = "-1"  # 방문 처리
                dfs(nx, ny, row, col)

        for x, row_list in enumerate(grid):
            for y, value in enumerate(row_list):
                if value != "1":
                    continue
                grid[x][y] = "-1"  # 방문 확인
                dfs(x, y, row, col)
                answer += 1

        return answer
