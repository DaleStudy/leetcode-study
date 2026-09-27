# M, N are dimensions of the board, W is the number of words, and L is the maximum length of a word.
# TC: O(W * L + M * N * 3^(L - 1)) - building Trie takes O(W * L); backtracking explores at most 3 directions after first step up to depth L
# SC: O(W * L) - Trie storage for all words and recursion stack depth up to L

from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r: int, c: int, parent: TrieNode):
            char = board[r][c]
            curr_node = parent.children.get(char)
            if not curr_node:
                return

            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None

            board[r][c] = "#"  # mark visited

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    if board[nr][nc] in curr_node.children:
                        dfs(nr, nc, curr_node)

            board[r][c] = char  # backtrack

            # Prune leaf nodes to accelerate search
            if not curr_node.children:
                del parent.children[char]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result
