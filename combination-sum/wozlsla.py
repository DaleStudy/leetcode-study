"""
# Intuition
중복을 허용하는 조합?

# Approach
- X
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result, nums = [], []

        def dfs(start, total):

            # 기저조건 1
            if total > target:
                return

            # 기저조건 2
            if total == target:  # sum to target 찾음
                result.append(nums[:])  # 복사본 추가

            for i in range(start, len(candidates)):
                num = candidates[i]
                nums.append(num)
                dfs(i, total + num)
                nums.pop()

        # 재귀함수 호출
        dfs(0, 0)

        return result
