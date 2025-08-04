# https://leetcode.com/problems/house-robber-ii/

from typing import List

class Solution:
    def rob_on(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            집들이 원을 이루고 있고 인접한 두 집을 모두 방문하면 안 되기 때문에, 다음과 같이 두 가지 상황으로 max money를 구한다.
            (원형이라는 점을 고려하지 않으면 첫 번째 집과 마지막 집을 모두 방문하게 될 수도 있기 때문)
                (1) 첫 번째 집을 제외
                (2) 마지막 집을 제외
            그리고 두 값 중 큰 값을 반환한다.

            dp[i] = nums[i]까지 확인했을 때의 max money
            dp[i] = max(dp[i - 1], dp[i - 2] + num)
        """
        n = len(nums)

        # early stop
        if n <= 3:
            return max(nums)

        dp1 = [0] * (n - 1)  # 마지막 집 제외: nums[0] ~ nums[n - 2]
        dp2 = [0] * (n - 1)  # 첫 번째 집 제외: nums[1] ~ nums[n - 1]

        # initialize
        dp1[0], dp2[0] = nums[0], nums[1]
        dp1[1], dp2[1] = max(dp1[0], nums[1]), max(dp2[0], nums[2])

        for i in range(2, n - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i + 1])

        return max(dp1[-1], dp2[-1])

    def rob(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            이전 O(n) space DP 풀이에서 dp[i] 값을 구하기 위해 dp[i - 1] & dp[i - 2] 값만 참고하므로,
            O(1) space로 optimize 할 수 있다.
        """
        n = len(nums)

        # early stop
        if n <= 3:
            return max(nums)

        # p2 = dp[i - 2], p1 = dp[i - 1]
        f_p2 = f_p1 = 0  # 마지막 집 제외: nums[0] ~ nums[n - 2]
        l_p2 = l_p1 = 0  # 첫 번째 집 제외: nums[1] ~ nums[n - 1]

        for i in range(n - 1):
            f_p2, f_p1 = f_p1, max(f_p1, f_p2 + nums[i])
            l_p2, l_p1 = l_p1, max(l_p1, l_p2 + nums[i + 1])

        return max(f_p1, l_p1)
