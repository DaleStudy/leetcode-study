from typing import List
from unittest import TestCase, main


class Node:

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        curr_node.data = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        return self.solve_trie_dfs(board, words)

    """
    * Constraints:
        1. m == board.length
        2. n == board[i].length
        3. 1 <= m, n <= 12
        4. board[i][j] is a lowercase English letter.
        5. 1 <= words.length <= 3 * 104
        6. 1 <= words[i].length <= 10
        7. words[i] consists of lowercase English letters.
        8. All the strings of words are unique.

    Runtime: 6439 ms (Beats 26.38%)
    Time Complexity: O(R * C * (4 ^ max L))
        - word의 최대 길이를 max L, words의 길이를 K라 하면, trie에 words를 모두 insert하는데 O(max L * K), upper bound
        - board의 각 grid에서 조회하는데 O(R * C)
            - grid마다 dfs 호출하는데, dfs의 방향은 4곳이고, 호출 스택의 최대 깊이는 max L 이므로, * O(4 ^ max L)
        > O(max L * K) + O(R * C) * O(4 ^ max L) ~= O(R * C * (4 ^ max L))

    Memory: 19.04 MB (Beats 20.79%)
    Space Complexity: O(max L * K)
        - trie의 공간 복잡도는 O(max L * K), upper bound
        - board의 각 grid에서 dfs를 호출하고, dfs 호출 스택의 최대 깊이는 max L 이므로 O(max L)
        - result의 최대 크기는 words의 길이와 같으므로 O(K), upper bound
        > O(max L * K) + O(max L) + O(K) ~= O(max L * K)
    """
    def solve_trie_dfs(self, board: List[List[str]], words: List[str]) -> List[str]:
        MAX_R, MAX_C = len(board), len(board[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(curr: Node, r: int, c: int, path: str):
            nonlocal result

            if not (0 <= r < MAX_R and 0 <= c < MAX_C):
                return

            if board[r][c] == "#":
                return

            char = board[r][c]
            if char not in curr.children:
                return

            post = curr.children[char]
            if post.data:
                result.add(post.data)

            board[r][c] = "#"
            for dir_r, dir_c in DIRS:
                dfs(post, r + dir_r, c + dir_c, path + char)
            board[r][c] = char

        result = set()
        for r in range(MAX_R):
            for c in range(MAX_C):
                if board[r][c] in trie.root.children:
                    dfs(trie.root, r, c, "")

        return list(result)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        words = ["oath","pea","eat","rain"]
        output = ["eat","oath"]
        self.assertEqual(Solution.findWords(Solution(), board, words), output)

    def test_2(self):
        board = [["a","b"],["c","d"]]
        words = ["abcb"]
        output = []
        self.assertEqual(Solution.findWords(Solution(), board, words), output)


if __name__ == '__main__':
    main()
