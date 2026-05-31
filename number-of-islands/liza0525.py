# 7기 풀이
# 시간 복잡도: O(n * m)
# - grid의 크기 n * m 에 따라 시간 복잡도가 정해짐(최악은 모든 grid 인덱스를 다 돌 때)
# 공간 복잡도: O(n * m)
# - 재귀 호출 스택의 최대 크기는 grid 이차 배열의 크기와 동일
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_i, len_j = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0 , 1)]  # 탐색 방향(위, 아래, 왼쪽, 오른쪽 순)

        res = 0

        def dfs(i, j):
            grid[i][j] = "0"  # 방문을 했으면 grid의 값을 "0"으로 변경해 다음 탐색 시 다시 방문하지 않도록 함
            for dir_i, dir_j in directions:
                next_i, next_j = i + dir_i, j + dir_j

                # 다음 탐색 인덱스가 배열 범위 내이면서
                # grid[next_i][next_j]가 "1"이어야 그 다음 방문을 할 수 있다.
                if (
                    0 <= next_i < len_i
                    and 0 <= next_j < len_j
                    and grid[next_i][next_j] == "1"
                ):
                    dfs(next_i, next_j)

        for i in range(len_i):
            for j in range(len_j):
                if grid[i][j] == "0":  # grid가 "0"일 땐 섬이 아니므로 탐색하지 않는다.
                    continue
                dfs(i, j)  # 섬 찾기
                res += 1  # 섬을 다 찾은 후엔 res에 1을 추가한다.

        return res
