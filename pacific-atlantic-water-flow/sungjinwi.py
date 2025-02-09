"""
    풀이 :
        빗물이 흘러가서 바다에 도착하는 경우가 아닌 역으로 바다에서 출발해서 도달할 수 있는 경우를 찾는다
        4방향 중에 height가 현재 위치보다 높거나 같으면 위로 흘러갈 수 있고 visited set에 저장해서
        이미 도달한 곳은 return 으로 처리한다
        바다와 위아래로 맞닿은 해안과 좌우로 맞닿은 해안에서 각각 출발하도록 두번의 반복문을 수행

    r, c : 행렬의 길이
    
    TC : O(R * C)
        visited_set을 통해 pacific, atlantic이 최악의 경우에도 섬 전체를 한번씩 순회하므로

    SC : O(R * C)
        각 set의 크기와 dfs 호출 스택은 섬 크기에 비례하므로
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        paci_visited, atl_visited = set(), set()
        n_rows = len(heights)
        n_cols = len(heights[0])

        def dfs(r: int, c: int, visited: set) -> None:
            if (r, c) in visited:
                return
            visited.add((r, c))
            for (m, n) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= m < n_rows and 0 <= n < n_cols:
                    if heights[r][c] <= heights[m][n]:
                        dfs(m, n, visited)

        for r in range(n_rows):
            dfs(r, 0, paci_visited)
            dfs(r, n_cols - 1, atl_visited)

        for c in range(n_cols):
            dfs(0, c, paci_visited)
            dfs(n_rows - 1, c, atl_visited)

        result = []
        for both in paci_visited.intersection(atl_visited):
            result.append(list(both))

        return result
