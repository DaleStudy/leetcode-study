class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["$"] = word
        rows, cols = len(board), len(board[0])
        result = []
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node:
                return
            next_node = node[char]
            word = next_node.pop("$", None)
            if word:
                result.append(word)
            board[r][c] = "#"
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            board[r][c] = char
            if not next_node:
                node.pop(char)
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)
        return result
