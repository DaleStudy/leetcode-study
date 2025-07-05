# https://leetcode.com/problems/word-search-ii/

from typing import List

"""#### [Approach 1] ####
[Complexity]
    (k = len(words), l = max(len(word) for word in words))
    - TC: O(m * n * 4 * 3^(l-1))
        - trie 구성: O(k * l) = O(total # of letters in words)
        - backtracking: 이론적으로 O(m * n * (4 * 3^(l-1)))
    - SC: O(k * l) (고정)
        - trie 저장: O(k * l) = O(total # of letters in words)
                    (word도 저장하므로 2배)
        - call stack: O(l)

[Approach]
    주어진 words에 대해 기본 trie를 구성하고,
    board 내의 문자들을 순회하며 해당 문자로 시작하는 단어가 trie에 있는지 backtracking으로 확인한다.

    이때, words = ["oa", "oaa"]인 경우에 res = ["oa", "oa", "oaa"]가 나오지 않도록 하기 위해서
    word를 찾은 경우 node.word = None으로 중복을 제거하는 로직이 필요하다. (혹은 res를 set()으로 기록)
"""

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res = []

        # 1. trie 구성
        trie = Trie()
        for word in words:
            trie.insert(word)

        # 2. board 내 문자를 순회하며 trie에서 찾기 (w. backtracking)
        def backtrack(r, c, node):
            # base condition
            if (
                    not (0 <= r < m and 0 <= c < n)  # (1) 범위를 벗어났거나
                    or board[r][c] == "#"  # (2) 이미 방문했거나
                    or board[r][c] not in node.children  # (3) 현재 node의 children에 문자가 없다면
            ):
                return

            # visit 처리
            curr_w, board[r][c] = board[r][c], "#"

            # trie 타고 내려가기
            node = node.children[curr_w]

            # 내려간 node가 word 라면 결과에 추가
            if node.word:
                res.append(node.word)
                node.word = None  # -- 중복 제거

            # recur
            backtrack(r - 1, c, node)
            backtrack(r + 1, c, node)
            backtrack(r, c - 1, node)
            backtrack(r, c + 1, node)

            # visit 처리 취소
            board[r][c] = curr_w

        for i in range(m):
            for j in range(n):
                backtrack(i, j, trie.root)

        return res


"""#### [Approach 2] ####
[Complexity]
    (k = len(words), l = max(len(word) for word in words))
    - TC: O(m * n * 4 * 3^(l-1))
        - trie 구성: O(k * l) = O(total # of letters in words)
        - backtracking: 이론적으로 O(m * n * (4 * 3^(l-1)))이나,
                        탐색 공간이 remove로 줄어들기 때문에 (4 * 3^(l-1)) 실제로는 경로가 빠르게 줄어듦
        - remove: O(k * l) (k개의 단어에 대해서)
    - SC: O(k * l) (점점 줄어듦)
        - trie 저장: O(k * l) = O(total # of letters in words)
                    (word도 저장하므로 2배) (실행 중에 줄어듦)
        - call stack: O(l)

[Approach]
    approach 1과 비교했을 때, trie.remove(node)를 통해 이미 찾은 단어의 경로를 trie에서 제거한다는 점이 다르다.
    따라서 이미 찾은 word의 경로는 더 이상 탐색하지 않으며, trie의 크기가 점차 줄어들어 탐색 공간도 줄어들게 된다.
    (TrieNode에 parent, char 추가)
"""

class TrieNode:
    def __init__(self, parent=None, char=None):
        self.children = {}
        self.word = None
        self.parent = parent  # for optimization
        self.char = char  # for optimization

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:  # node.children에 w가 없을 때만 새로 만들기
                node.children[w] = TrieNode(parent=node, char=w)
            node = node.children[w]
        node.word = word

    def remove(self, node):  # for optimization (이미 찾은 단어는 trie에서 없애기)
        # 중복 제거
        node.word = None

        # trie에서 현재 word를 제거 (단, child.children이 없어야 제거 가능)
        child, parent = node, node.parent
        while parent and len(child.children) == 0:
            del parent.children[child.char]
            child, parent = parent, parent.parent

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res = []

        # 1. trie 구성
        trie = Trie()
        for word in words:
            trie.insert(word)

        # 2. board 내 문자를 순회하며 trie에서 찾기 (w. backtracking)
        def backtrack(r, c, node):
            # base condition
            if (
                    not (0 <= r < m and 0 <= c < n)  # (1) 범위를 벗어났거나
                    or board[r][c] == "#"  # (2) 이미 방문했거나
                    or board[r][c] not in node.children  # (3) 현재 node의 children에 문자가 없다면
            ):
                return

            # visit 처리
            curr_w, board[r][c] = board[r][c], "#"

            # trie 타고 내려가기
            node = node.children[curr_w]

            # 내려간 node가 word 라면 결과에 추가
            if node.word:
                res.append(node.word)
                trie.remove(node)

            # recur
            backtrack(r - 1, c, node)
            backtrack(r + 1, c, node)
            backtrack(r, c - 1, node)
            backtrack(r, c + 1, node)

            # visit 처리 취소
            board[r][c] = curr_w

        for i in range(m):
            for j in range(n):
                backtrack(i, j, trie.root)

        return res
