"""
[문제풀이]
# Inputs

# Outputs

# Constraints

# Ideas

[회고]

"""


class Solution:
    def pacificAtlantic(heights):
        ret = []

        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

        n, m = len(heights), len(heights[0])

        def isPacific(y, x):  # pacific 도달 가능한지
            if y == 0 or (0 <= y < n and x == 0):
                return True

            else:
                return False

        def isAtlantic(y, x):  # Atlantic 도달 가능한지
            if y == n - 1 or (0 <= y < n and x == m - 1):
                return True

            else:
                return False

        def inRange(y, x):
            if 0 <= y < n and 0 <= x < m:
                return True
            else:
                return False

        v = [[False for _ in range(m)] for _ in range(n)]

        def dfs(y, x, heights, v):
            if isPacific(y, x) and isAtlantic(y, x):
                return True

            v[y][x] = True

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if inRange(ny, nx) and not v[ny][nx] and \
                        heights[y][x] >= heights[ny][nx]:
                    if dfs(ny, nx, heights, v):
                        return True

            v[y][x] = False
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, heights, v):
                    ret.append((i, j))

        return ret

    pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])

