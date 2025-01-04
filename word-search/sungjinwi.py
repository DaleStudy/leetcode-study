"""
    풀이 :
        상하좌우 이동한 좌표가 board범위 벗어나면 False
        board[m][n]이 word[idx]와 불일치하면 False
        이미 방문했을경우 False
        단어가 완성되면 True
        상하좌우 한칸 이동한칸에 대해 재귀적 호출
        상하좌우 중 True 있으면 True 없으면 False

    TC : O(M * N * 4 ^ W)
        board의 크기에 비례 -> M * N
        단어의 길이 만큼 상하좌우 재귀 호출 -> 4 ^ W

    SC : O(M * N + W)
        set의 메모리는 board 크기에 비례 -> M * N
        함수 호출 스택은 단어 길이에 비례 -> W
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        
        def dfs(m: int, n: int, idx: int) -> bool:
            if not (0 <= m < row and 0 <= n < col):
                return False
            if not board[m][n] == word[idx]:
                return False
            if (m, n) in visit:
                return False
            if idx == len(word) - 1:
                return True
            
            visit.add((m, n))
            if any (dfs(m + r, n + c, idx + 1) \
            for (r, c) in [(1, 0), (-1, 0), (0, 1), (0, -1)]):
                return True
            visit.remove((m, n))
            return False
        
        row = len(board)
        col = len(board[0])

        for m in range(row):
            for n in range(col):
                if dfs(m, n, 0):
                    return True
        return False
