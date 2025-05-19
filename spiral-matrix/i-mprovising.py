"""
Time complexity O(m*n)

단순구현
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        111  
        1M1   visited
        111 
        """
        m, n = len(matrix), len(matrix[0])
        
        board = [[0] * (n+2)]
        for i in range(m):
            tmp = [0] + matrix[i] + [0]
            board.append(tmp)
        board.append([0] * (n+2))

        visited = [[True] * (n+1)]
        for _ in range(m):
            tmp = [True] + [False] * n + [True]
            visited.append(tmp)
        visited.append([True] * (n+1))

        direction = 0
        x, y = 1, 1
        numbers = []

        for _ in range(m * n):
            numbers.append(board[x][y])
            visited[x][y] = True

            i, j = self.next_idx(direction, x, y)
            if visited[i][j]:
                direction = self.change_dir(direction)
                x, y = self.next_idx(direction, x, y)
            else:
                x, y = i, j

        return numbers

    def next_idx(self, dir, x, y):
        """
        0 1 2 3 : R D L U
        """
        if dir == 0:
            y += 1
        elif dir == 1:
            x += 1
        elif dir == 2:
            y -= 1
        else:
            x -= 1
        return x, y
    
    def change_dir(self, dir):
        return (dir + 1) % 4
