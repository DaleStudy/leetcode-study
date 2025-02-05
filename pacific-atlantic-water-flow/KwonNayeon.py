"""
Constraints:
- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5

Time Complexity: O(m*n) 
- 각 셀을 최대 한 번씩만 방문함

Space Complexity: O(m*n)
- visited sets(pacific, atlantic)가 최대 m*n 크기
- 재귀 호출 스택도 최대 m*n 깊이 가능

풀이방법:
1. Pacific(좌측상단)과 Atlantic(우측하단)의 경계에서 시작함
2. DFS로 현재 높이보다 높거나 같은 인접 셀로만 이동함 (물은 위 -> 아래로 흐르지만, 거꾸로 접근했으니까)
3. 각 바다에서 도달 가능한 셀들을 Set에 저장
4. 두 Set의 교집합이 정답 (양쪽 바다로 모두 흐를 수 있는 지점들)
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (new_r < 0 or new_r >= rows or
                    new_c < 0 or new_c >= cols or
                    (new_r, new_c) in visited):
                    continue
                if heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, visited)

        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(rows-1, c, atlantic)
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        return list(pacific & atlantic)
