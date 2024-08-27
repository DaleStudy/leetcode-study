from typing import List
from unittest import TestCase, main
from collections import defaultdict


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.solveWithBackTracking(candidates, target)

    """
    Runtime: 2039 ms (Beats 5.01%)
    Time Complexity: O(c * c * log c)
        - 처음 stack의 크기는 c에 비례 O(c)
        - 중복 제거에 사용하는 변수인 curr_visited_checker 생성에 O(c' log c')
        - stack의 내부 로직에서 c에 비례한 for문을 순회하는데 O(c)
        > O(c) * O(c' log c') + O(c) * O(c) ~= O(c * c * log c)
    
    Memory: 16.81 MB (Beats 11.09%)
    Space Complexity: O(c * c)
        - curr_combination의 크기가 c에 비례  
        - stack의 크기는 curr_combination의 크기와 c에 비례
        > O(c * c)
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
    Runtime: 58 ms (Beats 32.30%)
    Time Complexity: O(c * c)
        - candidates 정렬에 O(log c)
        - 첫 depte에서 dfs 함수 호출에 O(c)
        - 그 후 candidates의 길이에 비례해서 재귀적으로 dfs를 호출하는데 O(c)
            - lower_bound_idx에 따라 range가 감소하기는 하나 일단은 비례 O(c')
        > O(log c) + O(c * c') ~= O(c * c), 단 c' <= c 이므로 이 복잡도는 upper bound
    Memory: 16.59 MB (Beats 75.00%)
    Space Complexity: O(c)
        - result를 제외하고 모두 nonlocal 변수를 call by reference로 참조
        - dfs 함수 호출마다 메모리가 증가하는데, 호출횟수는 candidates의 길이에 비례 O(c)
            - lower_bound_idx에 따라 range가 감소하기는 하나 일단은 비례
        > O(c), 단 이 복잡도는 upper bound
    """
    def solveWithBackTracking(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(stack: List[int], sum: int, lower_bound_idx: int):
            nonlocal result, candidates, target

            if target < sum:
                return
            elif sum < target:
                for idx in range(lower_bound_idx, len(candidates)):
                    dfs(stack + [candidates[idx]], sum + candidates[idx], idx)
            else:  # target == sum
                result.append(stack)
                return

        result = []
        candidates.sort()
        dfs([], 0, 0)
        return result


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
