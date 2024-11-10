from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        - Idea: i번째 집까지의 최대 금액은 두 가지 중 더 큰 값으로 결정된다.
            1. (i-2번째 집까지의 최대 금액) + i번째 집의 금액
            2. (i-1번째 집까지의 최대 금액)
            이를 이용해 동적 프로그래밍으로 각 집까지의 최대 금액을 계산한다.
            중간 결과를 저장할 배열을 만들고 순차적으로 값을 채우면, 맨 마지막 값이 전체 최대 금액이 된다.
        - Time Complexity: O(n). n은 집의 개수.
            모든 집을 한번씩 순회해야 하므로 O(n) 시간이 걸린다.
        - Space Complexity: O(n). n은 집의 개수.
            각 집까지의 최대 금액을 저장하기 위해 배열을 사용하므로 O(n) 만큼의 메모리가 필요하다.
        """
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
