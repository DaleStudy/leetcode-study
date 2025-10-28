class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        res = set()

        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['$'] = word

        def dfs(x, y, node):
            ch = board[x][y]
            if ch not in node:
                return
            nxt = node[ch]

            if '$' in nxt:
                res.add(nxt['$'])

            board[x][y] = "#"
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "#":
                    dfs(nx, ny, nxt)
            board[x][y] = ch

        for i in range(n):
            for j in range(m):
                dfs(i, j, trie)

        return list(res)
