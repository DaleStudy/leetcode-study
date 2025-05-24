"""
시간 복잡도: O(n * m)
공간 복잡도: O(n * m)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        state = 0
        vis = [[False] * m for _ in range(n)]

        result = [matrix[0][0]]
        vis[0][0] = True
        x, y = 0, 0
        
        while len(result) < n * m:
            nx = x + dx[state % 4]
            ny = y + dy[state % 4]

            if not (0 <= nx < m) or not (0 <= ny < n) or vis[ny][nx]:
                state += 1
                continue
            
            vis[ny][nx] = True
            result.append(matrix[ny][nx])
            x, y = nx, ny
        
        return result
