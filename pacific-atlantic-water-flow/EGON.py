from typing import List
from unittest import TestCase, main


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        return self.solve_dfs(heights)

    """
    Runtime: 416 ms (Beats 11.61%)
    Time Complexity: O((r * c) ^ 2)
        - memo_pacific 생성에 O(r * c)
        - memo_atlantic 생성에 O(r * c)
        - heights의 모든 grid에 대해 조회하는데 O(r * c)
            - 조회하면서 시행하는 dfs 2회 조회하는데 2 * O(r * c), upper bound
        - heights의 모든 grid에 대해 조회하며 result 생성에 O(r * c)
        > O(r * c) + O(r * c) + O(r * c) * (2 * O(r * c)) + O(r * c) = 3 * O(r * c) + 2 * O((r * c) ^ 2) ~= O((r * c) ^ 2)

    Memory: 18.30 (Beats 37.99%)
    Space Complexity: O(1)
        - memo_pacific 생성에 O(r * c)
        - memo_atlantic 생성에 O(r * c)
        - dfs에서 stack의 최대 크기는 O(r * c), upper bound
            - dfs를 2회 사용하는데 * 2
        > O(r * c) + O(r * c) + 2 * O(r * c) = 4 * O(r * c) ~= O(r * c)
    """
    def solve_dfs(self, heights: List[List[int]]) -> List[List[int]]:
        MAX_R, MAX_C = len(heights), len(heights[0])
        DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def dfs(r: int, c: int, memo: List[List[any]]):
            stack = [[r, c]]
            while stack:
                curr_r, curr_c = stack.pop()
                for dir_r, dir_c in DIRS:
                    if not (0 <= curr_r + dir_r < MAX_R and 0 <= curr_c + dir_c < MAX_C):
                        continue

                    if heights[curr_r][curr_c] > heights[curr_r + dir_r][curr_c + dir_c]:
                        continue

                    if memo[curr_r][curr_c] is not None and memo[curr_r + dir_r][curr_c + dir_c] is None:
                        memo[curr_r + dir_r][curr_c + dir_c] = memo[curr_r][curr_c]
                        stack.append([curr_r + dir_r, curr_c + dir_c])

        memo_pacific = [[True if r == 0 or c == 0 else None for r in range(MAX_C)] for c in range(MAX_R)]
        memo_atlantic = [[True if r == MAX_R - 1 or c == MAX_C - 1 else None for c in range(MAX_C)] for r in range(MAX_R)]
        result = []
        for r in range(MAX_R):
            for c in range(MAX_C):
                r_pacific, c_pacific = r, c
                dfs(r_pacific, c_pacific, memo_pacific)

                r_atlantic, c_atlantic = MAX_R - r_pacific - 1, MAX_C - c_pacific - 1
                dfs(r_atlantic, c_atlantic, memo_atlantic)

        for r in range(MAX_R):
            for c in range(MAX_C):
                if memo_pacific[r][c] and memo_atlantic[r][c]:
                    result.append([r, c])

        return result


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        output = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        self.assertEqual(Solution().pacificAtlantic(heights), output)

    def test_2(self):
        heights = [[1]]
        output = [[0,0]]
        self.assertEqual(Solution().pacificAtlantic(heights), output)

    def test_3(self):
        heights = [[1,2,3],[8,9,4],[7,6,5]]
        output = [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        self.assertEqual(Solution().pacificAtlantic(heights), output)

    def test_4(self):
        heights = [[1,1],[1,1],[1,1]]
        output = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
        self.assertEqual(Solution().pacificAtlantic(heights), output)


if __name__ == '__main__':
    main()
