"""
[문제풀이]
# Inputs
- board: m*n grid of characters
- word: str
# Outputs
- word 가 grid 안에 있으면 true, 아니면 false
# Constraints
- 탐색: 상하좌우
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15

- board, word => 무조건 대소문자로 구성
# Ideas
1. 퍼지면서 탐색 -> bfs?
q = cur.append(i, j, "")
q.pop() 해서
if 현재 w 가 word랑 같다면 그 즉시 bfs stop하고 return True
만약 bfs 끝까지 했는데도 안나오면 return False

bfs: q에 다음 원소 넣을 때 현재 값에 이어붙인문자가 w랑 어떤식으로 비교해야 맞는 조건절이 되는걸까?
=> cur_w의 len 값을 i로 사용하려했지만 w가 더 짧으면 idxError 뜰까봐 보류
=> 메모리 초과 오류 뜸..
=> 아..같은 자리를 방문하면 안됨!! 즉, 원복이 필요함!
-> 백트래킹으로 풀이 change

2. dfs로도 꼭 풀어보기!
백트래킹 복습 용으로 굿

board안의 숫자는 오직 대소문자 -> isalpha() 로 체킹 가능
=> 방문하면 0으로 바꾸기

풀기는 풀었지만..7090ms : Beats 7.34%

Follow up : Could you use search pruning to make your solution faster with a larger board
가지치기 기법 어떻게 도입할까??
=> cur_idx 하나 둬서, AB.. ABC -> 진행 도중, 하나라도 word랑 다르면 바로 그 경로 컷
=> 그래도 4587ms.. Beats 41.00%
=> 먼가 더 정석 성능 개선이 필요

해설 참고
=> word_idx를 이용, any문을 이용한 리팩토링
=> 해설 풀이 : 4385ms

[회고]
idx를 이용한 가지치기 방법 잘 알아두자
"""

# from collections import deque
# class Solution:
#     def exist(board, word):
#
#         q = deque([])
#         n, m = len(board), len(board[0])
#
#         q.append((0, 0, board[0][0]))
#
#         dy = [-1, 0, 1, 0]
#         dx = [0, 1, 0, -1]
#
#         while q:
#             cur_y, cur_x, cur_w = q.popleft()
#
#             if cur_w == word:
#                 return True
#
#             for i in range(3):
#                 ny = cur_y + dy[i]
#                 nx = cur_x + dx[i]
#
#                 if 0 <= ny < n and 0 <= nx < m:
#                     q.append((ny, nx, cur_w + board[ny][nx]))
#
#         return False
#
#     exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCDE")


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n, m = len(board), len(board[0])

        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

        v = [[False for _ in range(m)] for _ in range(n)]

        def dfs(y, x, w):
            #print('y, x : ', y, x)
            #print('w: ', w)
            if w == word:
                return True

            if len(w) >= len(word):
                return False

            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]

                if 0 <= ny < n and 0 <= nx < m and not v[ny][nx]:
                    v[ny][nx] = True
                    if dfs(ny, nx, w + board[ny][nx]):
                        return True
                    v[ny][nx] = False

        for i in range(n):
            for j in range(m):
                if not v[i][j] and board[i][j] == word[0]:
                    v[i][j] = True
                    if dfs(i, j, board[i][j]):
                        return True
                    v[i][j] = False

        return False

# 해설
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n, m = len(board), len(board[0])

        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

        def dfs(y, x, idx):
            if idx == len(word):
                return True

            if not (0 <= y < n and 0 <= x < m):
                return False

            if board[y][x] != word[idx]:
                return False

            temp = board[y][x]
            board[y][x] = ""

            for i in range(4):
                if dfs(y + dy[i], x + dx[i], idx + 1):
                    return True

            board[y][x] = temp
            return False

        return any(dfs(i, j, 0) for i in range(n) for j in range(m))

