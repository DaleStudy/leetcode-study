class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(row, col, idx):
            # 끝까지 탐색시 길이와 k가 같아지므로 True 반환
            if idx == len(word):
                return True
            # 범위를 벗어난 경우, 방문한 경우, 같은 word가 없는 경우 False 반환
            if not (0 <= row < rows) or not (0 <= col < cols) or (row, col) in visited or board[row][col] != word[idx]:
                return False
            
            visited.add((row, col))
            res = dfs(row + 1, col, idx + 1) or dfs(row - 1, col, idx + 1) or dfs(row, col + 1, idx + 1) or dfs(row, col - 1, idx + 1)
            visited.remove((row, col))
            return res
        # 시작점 탐색
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        # 시간복잡도 O(rows*cols*4^(word))
        # 공간복잡도 O(rows*cols)
        return False
