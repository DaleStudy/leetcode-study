# TC: O(n), nums의 원소를 하나씩 확인
# SC: O(n), 원소 갯수만큼 메모이제이션 배열
class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = [None] * len(nums)

        def explore(idx: int) -> int:
            if (idx >= len(nums)):
                return 0
            
            if (memo[idx] is not None):
                return memo[idx]
            
            rob_current = nums[idx] + explore(idx + 2)
            skip_current = explore(idx + 1)
            memo[idx] = max(rob_current, skip_current)
            return memo[idx]

        return explore(0)

