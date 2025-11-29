'''
Approach
- target값에서 candidate 값을 빼고 그 누적합을 사용해야한다는 흐름은 파악했지지만 구현이 어려웠습니다.
-그래서 알고달레를 참고해서 최대한 이해하고 혼자 작성해보려고 했습니다....
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        for candidate in candidates:
            for num in range(candidate, target +1):
                for combination in dp[num - candidate]:
                    dp[num].append(combination + [candidate])
        return dp[target]
