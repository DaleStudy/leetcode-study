# https://leetcode.com/problems/combination-sum/

from typing import List

class Solution:
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        [Complexity]
            - TC: O(n^{target/min(candidates)})
                - 재귀 호출 트리의 최대 height는 target/min(candidates) (중복 가능하므로)
                - 각 step에서 최대 n회 재귀 호출 (for i in range(idx, n))
            - SC: O(target/min(candidates)) (* res 제외)
                - recursion stack = 최대 O(target/min(candidates))
                - combi = 최대 O(target/min(candidates))

        [Approach]
            backtracking(idx = 현재 보고있는 원소의 인덱스, tot_sum = 현재까지의 합)으로 접근한다.
                - base condition: tot_sum이 target과 같으면 res에 추가하고, target 보다 크면 종료
                - recursion: 현재 보고있는 원소의 인덱스의 이후에 있는 원소들을 backtracking으로 검사
                             (* "same number may be chosen from candidates" 이므로!)
        """
        n = len(candidates)
        combi = []
        res = []

        def backtracking(idx, tot_sum):
            # base condition
            if tot_sum == target:
                res.append(combi[:])
                return
            if tot_sum > target:
                return

            # recur
            for i in range(idx, n):
                c = candidates[i]
                combi.append(c)
                backtracking(i, tot_sum + c)
                combi.pop()

        backtracking(0, 0)

        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        [Complexity]
            - TC: O(n^{target/min(candidates)})
            - SC: O(target/min(candidates)) (* res 제외)

        [Approach]
            기존 backtracking 풀이에 정렬을 추가해서 조금 더 최적화할 수 있다.
            즉, candidates를 정렬한 후, 매 단계에서 candidates[idx] > target - tot_sum 일 때도 종료한다.
            이론적으로 복잡도는 동일하나(TC의 경우, 정렬에 드는 O(nlogn) 보다 백트래킹에 드는 O(n^m)이 더 지배적), early stop이 가능해진다.
        """
        n = len(candidates)
        combi = []
        res = []

        candidates.sort()  # -- 정렬

        def backtracking(idx, tot_sum):
            # base condition
            if tot_sum == target:
                res.append(combi[:])
                return
            if tot_sum > target or candidates[idx] > target - tot_sum:  # -- optimize
                return

            # recur
            for i in range(idx, n):
                c = candidates[i]
                combi.append(c)
                backtracking(i, tot_sum + c)
                combi.pop()

        backtracking(0, 0)

        return res
