"""
시간복잡도: O(m * n)
공간복잡도: O(m * n)

1. 태평양과 대서양 각각에서 물이 도달할 수 있는 위치를 기록할 2차원 배열(check)을 만든다.
2. 태평양과 맞닿은 칸들(왼쪽 열과 위쪽 행)에는 태평양 도달 가능(값 1), 대서양과 맞닿은 칸들(오른쪽 열과 아래쪽 행)에는 대서양 도달 가능(값 2) 표시를 한다.
   - 1: 태평양, 2: 대서양 — 2진수로는 각각 01, 10이라는 의미임.
3. 각 바다에 인접한 칸들에서 시작해, BFS를 이용해 도달 가능한 모든 칸을 확장한다.
   - 인접한 칸으로 이동할 때, 항상 지금 칸보다 높이가 같거나 더 높은 칸으로만 물이 흐를 수 있다(즉, 물이 거슬러 흐르는 조건).
   - 이미 같은 바다에서 방문한 적이 있는 칸은 건너뛴다.
   - 새로운 위치에 도달할 때마다 check 배열을 갱신하고 큐에 추가한다.
4. 태평양과 대서양에서 모두 도달 가능한 칸(값이 3이 된 칸)을 답으로 모아 반환한다.

# 비트마스킹 기법 사용 원리 #
- 태평양과 대서양 두 바다에서 도달 가능한 칸을 표시하기 위해 비트마스킹 기법을 사용한다.
- 각 칸에 대해, 1비트(01)는 태평양(Pacific), 2비트(10)는 대서양(Atlantic) 도달 가능을 의미한다.
- 예를 들어 각 칸의 값이 1이면 태평양, 2이면 대서양, 3이면 두 바다 모두에 도달 가능한 칸임을 나타낸다.
- bfs/dfs로 인접 칸(상하좌우)로 확장할 때, 이미 해당 바다의 비트가 켜져 있으면 방문하지 않는다.
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        DIR = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]

        check = [[0] * COL for _ in range(ROW)]

        for r in range(ROW):
            check[r][0] |= 1
            check[r][COL - 1] |= 2

        for c in range(COL):
            check[0][c] |= 1
            check[ROW - 1][c] |= 2

        queue = deque([])

        for r in range(ROW):
            for c in range(COL):
                if check[r][c] != 0:
                    queue.append((r, c))

        def bound(row: int, col: int) -> bool:
            return 0 <= row < ROW and 0 <= col < COL

        while queue:
            r, c = queue.popleft()

            for dr, dc in DIR:
                tr, tc = r + dr, c + dc

                if not bound(tr, tc):
                    continue

                if heights[tr][tc] < heights[r][c]:
                    continue

                if check[tr][tc] | check[r][c] == check[tr][tc]:
                    continue

                check[tr][tc] |= check[r][c]
                queue.append((tr, tc))

        ans = []

        for r in range(ROW):
            for c in range(COL):
                if check[r][c] == 3:
                    ans.append([r, c])

        return ans
