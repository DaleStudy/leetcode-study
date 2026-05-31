# 7기 풀이
# 시간 복잡도: O(m * n)
# - 최대 재귀 스택
# 공간 복잡도: O(m * n)
# - 인덱스 모두가 대서양과 태평양에 도달할 때 최대 공간 복잡도
class Solution:
    # 문제 접근 방향
    # 각 지점에서 시작하는 것이 아닌, 태평양과 대서양에 맞닿아 있는 인덱스에서 시작해서
    # 최대 높이에 도달할 때까지 DFS로 접근 후, 두 대양에서 모두 도달하는 인덱스를 찾는다.
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        pacific_dest = set()  # 태평양에서 시작할 때 갈 수 있는 곳
        atlantic_dest = set()  # 대서양에서 시작했을 때 갈 수 있는 곳

        def dfs(i, j, dest):
            dest.add((i, j))
            for dir_i, dir_j in directions:
                next_i, next_j = i + dir_i, j + dir_j

                if (
                    0 <= next_i < len(heights)
                    and 0 <= next_j < len(heights[0])
                    and (next_i, next_j) not in dest
                    and heights[next_i][next_j] >= heights[i][j]  # 다음 인덱스가 같거나 높은 경우만 탐색
                ):
                    dfs(next_i, next_j, dest)

        for j in range(len(heights[0])):
            dfs(0, j, pacific_dest)  # 태평양에서 시작(맨 윗줄)
            dfs(len(heights) - 1, j, atlantic_dest)  # 대서양에서 시작(맨 아랫줄)

        for i in range(len(heights)):
            dfs(i, 0, pacific_dest)  # 태평양에서 시작(맨 왼쪽 줄)
            dfs(i, len(heights[0]) - 1, atlantic_dest)  # 대서양에서 시작(맨 오른쪽 줄)

        return list(pacific_dest.intersection(atlantic_dest))  # 겹치는 도착지만 리턴
