from typing import List
from unittest import TestCase, main


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.solveWithDFS(board, word)

    """
    Runtime: 5005 ms (Beats 27.48%)
    Time Complexity: O((MAX_R ** 2) * (MAX_C ** 2)), upper bound
        - 이중 for문 조회에 O(MAX_R * MAX_C)
        - node 하나당 조회하는 DIRS의 크기가 4이고, 최대 word의 길이만큼 반복하므로 O(4 * L)
            - 단 early return하므로 이는 upper bound
        > O(MAX_R * MAX_C) * O(4L) ~= O(MAX_R * MAX_C * L)

    Memory: 16.59 MB (Beats 69.71%)
    Space Complexity:
        - MAX_R * MAX_C 격자의 칸마다 stack이 생성될 수 있으므로 O(MAX_R * MAX_C)
        - node의 크기는 visited에 지배적이고(curr_word 무시 가정), visited의 크기는 최대 L
        > O(MAX_R * MAX_C) * O(L) ~= O(MAX_R * MAX_C * L)
    """
    def solveWithDFS(self, board: List[List[str]], word: str) -> bool:
        MAX_R, MAX_C, MAX_IDX = len(board), len(board[0]), len(word)
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        for r in range(MAX_R):
            for c in range(MAX_C):
                if board[r][c] == word[0]:
                    stack = [(r, c, 0, board[r][c], set([(r, c)]))]
                    while stack:
                        curr_r, curr_c, curr_idx, curr_word, curr_visited = stack.pop()

                        if curr_word == word:
                            return True

                        for dir_r, dir_c in DIRS:
                            post_r, post_c, post_idx = curr_r + dir_r, curr_c + dir_c, curr_idx + 1
                            if (post_r, post_c) in curr_visited:
                                continue
                            if not (0 <= post_r < MAX_R and 0 <= post_c < MAX_C):
                                continue
                            if not (post_idx < MAX_IDX and board[post_r][post_c] == word[post_idx]):
                                continue

                            post_visited = curr_visited.copy()
                            post_visited.add((post_r, post_c))
                            stack.append((post_r, post_c, post_idx, curr_word + word[post_idx], post_visited))

        return False


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        output = True
        self.assertEqual(Solution.exist(Solution(), board, word), output)

    def test_2(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        output = True
        self.assertEqual(Solution.exist(Solution(), board, word), output)

    def test_3(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        output = False
        self.assertEqual(Solution.exist(Solution(), board, word), output)

    def test_4(self):
        board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
        word = "ABCESEEEFS"
        output = True
        self.assertEqual(Solution.exist(Solution(), board, word), output)


if __name__ == '__main__':
    main()
