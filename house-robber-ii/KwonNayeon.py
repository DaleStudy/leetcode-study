"""
Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Time Complexity: O(n)

Space Complexity: O(n)

풀이방법:
1. 집이 하나만 있는 경우 → 그 집을 텀
2. 먼저 원형이 아닌 일반적인 House Robber 문제를 해결하는 함수를 구현함
3. 이 문제의 제약조건을 포함하기 위해:
  - 첫 번째 집을 털지 않는 경우 (nums[1:])
  - 마지막 집을 털지 않는 경우 (nums[:-1])
  - 둘 중 최댓값을 반환
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_simple(houses):
            if len(houses) == 1:
                return houses[0]
            elif len(houses) == 2:
                return max(houses[0], houses[1])

            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(dp[i-1], houses[i] + dp[i-2])

            return dp[-1]

        return max(rob_simple(nums[1:]), rob_simple(nums[:-1]))
