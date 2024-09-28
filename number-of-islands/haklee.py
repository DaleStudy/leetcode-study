"""TC: O(m * n), SC: O(m * n)

아이디어:
- 특정 칸이 1일 경우 이와 같은 섬 안에 있는 모든 칸들을 0으로 바꿔주는 `remove_ground` 함수 구현.
- grid 내의 모든 칸들을 돌면서 `remove_ground`가 몇 번 최초 호출(즉, 재귀 호출 아님) 되었는지
  세면 전체 섬이 몇 개 있는지 찾을 수 있다.

SC:
- 모든 칸이 전부 1일 경우 remove_ground의 호출 스택 깊이가 m*n이 된다. 즉, O(m * n).

TC:
- 각 노드는 최대 5번씩 접근될 수 있다.
    - 이웃한 칸에서 remove_ground 하면서 접근
    - 최외곽에서 해당 칸이 1인지 체크하면서 접근
- 접근하고 나서 하는 연산이 O(1).
    - 해당 칸의 값이 1인지 체크하는 데에 O(1).
    - check_inside 연산을 4번 할 수 있는데 각각 O(1).
    - 종합하면 O(1).
- 종합하면 O(m * n).
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        minx, miny, maxx, maxy = 0, 0, len(grid[0]) - 1, len(grid) - 1

        def remove_ground(i, j):
            if minx <= j <= maxx and miny <= i <= maxy and grid[i][j] == "1":
                grid[i][j] = "0"
                remove_ground(i - 1, j)
                remove_ground(i + 1, j)
                remove_ground(i, j - 1)
                remove_ground(i, j + 1)

        sol = 0
        for i in range(maxy + 1):
            for j in range(maxx + 1):
                if grid[i][j] == "1":
                    sol += 1
                    remove_ground(i, j)
        return sol
