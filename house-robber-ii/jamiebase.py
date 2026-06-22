"""
# Intuition
집이 원형으로 놓여있기 때문에 첫 번째 집을 터는 경우, 안 터는 경우일 때로 나누어 해를 구하고,
두 경우에서 최댓값 해를 구한다.

# Complexity
n은 nums의 길이라고 할 때,
- Time complexity: O(N)
- Space complexity: O(N)

"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # 첫 번째 집을 터는 경우
        dp1 = [0] * n
        dp1[0] = dp1[1] = nums[0]
        for i in range(2, n - 1):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])

        # 첫 번째 집을 안 터는 경우
        dp2 = [0] * n
        dp2[1] = nums[1]
        for j in range(2, n):
            dp2[j] = max(dp2[j - 2] + nums[j], dp2[j - 1])

        return max(max(dp1), max(dp2))
