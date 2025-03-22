'''
시간 복잡도: O(m * n * 4^s) s = word 최대 길이
공간 복잡도: O(w)           w = 모든 단어에 포함된 문자 수의 합
'''
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root

            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            
            node['$'] = word

        def dfs(i, j, node, visited):
            if '$' in node:
                result.append(node['$'])
                del node['$']

            if not (0 <= i < m and 0 <= j < n) or (i, j) in visited:
                return
            
            char = board[i][j]
            if char not in node:
                return
            
            visited.add((i, j))

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(i + di, j + dj, node[char], visited)

            visited.remove((i, j))

        m, n = len(board), len(board[0])
        result = []

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, set())

        return result
