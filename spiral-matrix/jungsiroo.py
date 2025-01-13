from collections import deque

"""
BFS의 아이디어를 차용하여 풀이

끝에서부터 안쪽으로 돌아가야하기에 미리 돌아갈 방향 지정 : (dx, dy)
한칸씩 이동해가면서 범위 밖을 넘어갔거나 이미 visit한 데이터가 발견되면 방향을 꺾음

Tc : O(m*n)
Sc : O(m*n)
"""

# r, d, l ,u
dx = [0,1,0,-1]
dy = [1,0,-1,0]

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
    
    def in_range(self, r, c):
        if r<0 or r>=self.m or c<0 or c>=self.n:
            return False
        return True
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        INF = int(1e9)
        d = 0
        self.m, self.n = len(matrix), len(matrix[0])
        r, c = 0, 0

        ret = []

        for _ in range(self.m * self.n):
            ret.append(matrix[r][c])
            if not self.in_range(r+dx[d], c+dy[d]) or matrix[r+dx[d]][c+dy[d]] == INF:
                d = (d+1)%4
            matrix[r][c] = INF
            r, c = r+dx[d], c+dy[d]
        
        return ret
        
        
