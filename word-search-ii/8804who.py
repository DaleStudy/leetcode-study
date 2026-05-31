class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        answer = []
        trie = {}
        moves = [[-1,0],[1,0],[0,-1],[0,1]]

        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["$"] = word
        
        def dfs(y, x, node):
            if "$" in node:
                answer.append(node["$"])
                del node["$"]

            if 0 > y or y >= len(board) or 0 > x or x >= len(board[0]):
                return

            if board[y][x] not in node:
                return

            node = node[board[y][x]]

            temp = board[y][x]
            board[y][x] = ""

            for move in moves:
                dfs(y+move[0], x+move[1], node)
            board[y][x] = temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    dfs(i,j,trie)
        return answer
    
