from typing import List
from unittest import TestCase, main
from collections import defaultdict


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.solveWithDFS(candidates, target)

    """
    Runtime: 2039 ms (Beats 5.01%)

    Memory: 16.81 MB (Beats 11.09%)
    """
    def solveWithDFS(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        stack = []
        visited = defaultdict(bool)
        for candidate in candidates:
            stack.append([[candidate], candidate])

        while stack:
            curr_combination, curr_sum = stack.pop()
            curr_visited_checker = tuple(sorted(curr_combination))

            if curr_sum == target and visited[curr_visited_checker] is False:
                visited[curr_visited_checker] = True
                result.append(curr_combination)

            if target < curr_sum:
                continue

            for candidate in candidates:
                post_combination, post_sum = curr_combination + [candidate], curr_sum + candidate
                stack.append([post_combination, post_sum])

        return result

    """
    Runtime: ?

    Memory: ?
    """
    def solveWithBackTracking(self, candidates: List[int], target: int) -> List[List[int]]:
        return []


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        output = [[2, 2, 3], [7]]
        self.assertEqual(Solution.combinationSum(Solution(), candidates, target), output)

    def test_2(self):
        candidates = [2, 3, 5]
        target = 8
        output = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(Solution.combinationSum(Solution(), candidates, target), output)

    def test_3(self):
        candidates = [2]
        target = 1
        output = []
        self.assertEqual(Solution.combinationSum(Solution(), candidates, target), output)


if __name__ == '__main__':
    main()
