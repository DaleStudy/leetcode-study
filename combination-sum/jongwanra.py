"""
[Problem]
https://leetcode.com/problems/combination-sum/

candidates: unique array of integers
return a list of all unique combinations of candidates == target
any order

하나의 숫자는 candidates에서 무제한으로 선택할 수 있다.
두 조합이 서로 다르다고 간주되는 조건은, 선택된 숫자 중 적어도 하나의 개수가 다를 때이다.
[Brainstorming]
DFS를 이용해서 Combination을 만든다.
종료조건: target == sum || target > sum

[Plan]
1. candidates를 오름차순 정렬
2. DFS

[Complexity]
N -> candidates.length
M -> approximately target divided by the smallest candidate. -> target / min(candidates)
Time: O(N^M)
Space: O(N + M)
  - 재귀 호출 스택: 깊이는 최대 target / min(candidates)
  - chosen: 재귀 스택 깊이 만큼 공간 차지
  - cache: 최악의 경우 answer와 같은 개수의 조합 저장 -> O(number of combinations)
"""

from typing import List


class Solution:
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        cache = set()
        answer = []
        chosen = []

        def dfs(sum: int) -> None:
            nonlocal target, candidates, cache, answer, chosen
            print(chosen)
            if sum > target:
                return
            if sum == target:
                copied_chosen = chosen[:]
                copied_chosen.sort()

                cache_key = tuple(copied_chosen)
                if cache_key in cache:
                    # print(f"already exists {cache_key} in cache")
                    return
                cache.add(cache_key)
                answer.append(copied_chosen)

            for candidate in candidates:
                chosen.append(candidate)
                dfs(sum + candidate)
                chosen.pop()

        dfs(0)
        return answer

    """
    중복 조합 방지 another solution
    ref: https://www.algodale.com/problems/combination-sum/

    [Complexity]
    N -> candidates.length
    M -> target / min(candidates)
    Time: O(N^M)
    Space: O(M)
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        combi = []

        def dfs(sum: int, start: int) -> None:
            nonlocal target, answer, combi, candidates

            if sum > target:
                return
            if sum == target:
                answer.append(combi[:])
                return

            for index in range(start, len(candidates)):
                candidate = candidates[index]
                combi.append(candidate)
                dfs(sum + candidate, index)
                combi.pop()

        dfs(0, 0)
        return answer


sol = Solution()
# print(sol.combinationSum([2,3,6,7], 7))
print(sol.combinationSum([2, 3, 5], 8))
# print(sol.combinationSum([2], 1))

