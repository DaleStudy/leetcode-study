"""
Solution: 
    1) for 문을 돌면서 섬(1)인 경우 result 에 1을 더하고 dfs를 돌린다.
    2) dfs 를 통해 섬 전체를 순회하며 0으로 만들어준다.
    3) 섬의 갯수 result 를 return 한다.

육지의 갯수 n
Time: O(n) n회의 dfs 함수 실행 될 수 있음
Space: O(n) n의 호출스택이 사용 될 수 있음
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        result = 0

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                dfs(i + dx, j + dy)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    result += 1

        return result
