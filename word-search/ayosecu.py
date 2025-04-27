from typing import List

class Solution:
    """
        - Time Complexity: O(m*n*3^w)
            - m = len(board), n = len(board[0]), w = len(word)
            - m * n => finding start point
            - 3^w => There are three ways for visiting recursively until find a word
        - Space Complexity: O(w)
            - The sum of stack's space => The depth of dfs => len(word)
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        # DFS approach
        def dfs(i, j, leng):
            if leng == len(word):
                # Found!
                return True
            
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[leng]:
                # Wrong position or Not matched
                return False

            temp = board[i][j]  # Backup
            board[i][j] = "#"   # Visited
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if dfs(i + dx, j + dy, leng + 1):
                    return True
            board[i][j] = temp  # Restore

            return False
        
        # Finding Start Point
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    if dfs(i, j, 0):
                        return True
    
        return False

tc = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False)
]

for i, (board, word, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.exist(board, word)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
