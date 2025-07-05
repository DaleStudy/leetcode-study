"""
Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.

Time Complexity: O(W * N * 4^L)
- W는 words의 개수
- N은 board의 모든 cell (m * n)
- L은 word의 길이
- 각 단어마다 Word Search 1을 반복

Space Complexity: O(L)
- L은 word의 길이로, 재귀 호출 스택의 깊이

Word search 1과의 차이점:
- 단어 여러개를 동시에 찾아야 함
- 찾은 모든 단어들을 리스트로 반환해야 함

풀이방법:
- Word search 1과 동일한 방법 + set(words)로 중복 제거

노트:
- 시간초과로 통과 안 됨
- Trie 자료구조로 다시 풀어보기
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words = list(set(words))
        result = []

        def exist(word):
            rows, cols = len(board), len(board[0])

            def dfs(i, j, k):
                if k == len(word):
                    return True

                if (i < 0 or i >= rows or
                    j < 0 or j >= cols or
                    board[i][j] != word[k]):
                    return False

                temp = board[i][j]
                board[i][j] = '#'

                result = (dfs(i+1, j, k+1) or
                dfs(i-1, j, k+1) or
                dfs(i, j+1, k+1) or
                dfs(i, j-1, k+1))

                board[i][j] = temp
                return result

            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == word[0]:
                        if dfs(i, j, 0):
                            return True
            return False

        for word in words:
            if exist(word):
                result.append(word)
        return result
