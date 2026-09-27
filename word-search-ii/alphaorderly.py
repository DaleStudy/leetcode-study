"""
시간복잡도: O(w + m * n * 4^l)
  - w: 모든 단어 길이의 합 (트라이 구성)
  - m, n: 보드의 행, 열
  - l: 단어의 최대 길이 (각 칸에서 상하좌우 DFS)
공간복잡도: O(w + l)
  - w: 트라이와 정답 집합
  - l: DFS 재귀 깊이와 현재 경로의 방문 집합

단어를 트라이에 넣은 뒤, 보드의 각 칸에서 DFS로 이어지는 단어를 찾습니다.
이미 찾은 단어는 is_end를 끄고, 더 이상 이어지지 않는 노드는 트라이에서 지워
같은 접두사를 다시 탐색하지 않습니다.
"""
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = dict()

    def add_word(self, word: str):
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        # 이 글자에서 단어가 끝난다
        node.is_end = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        ROW, COL = len(board), len(board[0])
        # 상하좌우
        DIR = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        trie = TrieNode()
        for word in words:
            trie.add_word(word)

        def bound(row: int, col: int) -> bool:
            return 0 <= row < ROW and 0 <= col < COL

        # ans: 찾은 단어, visited: 현재 경로에서 지난 칸
        ans, visited = set(), set()

        def search(r: int, c: int, node: TrieNode, word: str):
            # 다음 글자가 트라이에 없거나, 같은 칸을 다시 밟으면 중단
            if board[r][c] not in node.children or (r, c) in visited:
                return

            visited.add((r, c))

            # 가지치기할 때 부모에서 현재 글자를 지우기 위해 보관
            parent = node
            ch = board[r][c]

            node = node.children[ch]
            word += ch

            if node.is_end:
                ans.add(word)
                # 같은 단어는 한 번만 찾는다
                node.is_end = False

            for dr, dc in DIR:
                tr, tc = r + dr, c + dc
                if not bound(tr, tc):
                    continue
                search(tr, tc, node, word)

            # 백트래킹: 이 칸을 다른 경로에서 다시 쓸 수 있게 되돌린다
            visited.remove((r, c))

            # 자식도 없고 여기서 끝나는 단어도 없으면 트라이에서 제거
            if not node.children and not node.is_end:
                del parent.children[ch]

        for r in range(ROW):
            for c in range(COL):
                search(r, c, trie, "")

        return list(ans)
