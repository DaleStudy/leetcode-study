class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = {}
        row = len(board)
        col = len(board[0])
        
        def dfs(m : int, n : int, seq : str) :
            if visit[m, n] :
                return
            if not word.startswith(seq + board[m][n]) :
                return
            visit[(m, n)] = 1
            seq += board[m][n]
            if seq == word :
                return
            if m > 0 :
                if (dfs()) :
                    return True
            if down :
                dfs()
            if left :
                dfs()
            if right :
                dfs()
            visit(m, n) = 0
            seq = seq[:len(seq)-1]


        while m in range(row) :
            while n in range(col) :
                if dfs(m, n, "") :
                    return True
                visit.clear()
        return False
